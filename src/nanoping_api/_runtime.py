from __future__ import annotations

import base64
import contextlib
import dataclasses
import datetime
import enum
import json
import math
import re
import socket
import types
import typing
import urllib.parse
from collections.abc import AsyncIterator, Awaitable, Callable, Generator, Iterator, Mapping, Sequence
from typing import Any, Generic, TypeVar

import httpx
import websockets.asyncio.client
import websockets.exceptions
import websockets.sync.client

T = TypeVar("T")
Req = TypeVar("Req")
Res = TypeVar("Res")

Json = dict[str, Any]


class Code(enum.IntEnum):
    """The status codes an API error can carry."""

    OK = 0
    CANCELLED = 1
    UNKNOWN = 2
    INVALID_ARGUMENT = 3
    DEADLINE_EXCEEDED = 4
    NOT_FOUND = 5
    ALREADY_EXISTS = 6
    PERMISSION_DENIED = 7
    RESOURCE_EXHAUSTED = 8
    FAILED_PRECONDITION = 9
    ABORTED = 10
    OUT_OF_RANGE = 11
    UNIMPLEMENTED = 12
    INTERNAL = 13
    UNAVAILABLE = 14
    DATA_LOSS = 15
    UNAUTHENTICATED = 16


class ApiError(Exception):
    """A call that failed.

    `code` says why, and `status` is the HTTP status of the response, or 0 when
    the error arrived on a stream or the node could not be reached.
    """

    def __init__(self, code: int, message: str, status: int = 0) -> None:
        super().__init__(message)
        try:
            self.code: Code | int = Code(code)
        except ValueError:
            self.code = code
        self.message = message
        self.status = status

    def __repr__(self) -> str:
        return f"ApiError(code={self.code!r}, message={self.message!r}, status={self.status})"


class ProtoEnum(enum.StrEnum):
    """An enum of the API. A value this version does not know is kept as it is."""

    @classmethod
    def _missing_(cls, value: object) -> ProtoEnum:
        member = str.__new__(cls, str(value))
        member._name_ = str(value)
        member._value_ = str(value)
        return member


@dataclasses.dataclass(frozen=True)
class Route:
    """One REST binding of a method.

    `body` is "*" for the whole request, the name of one request field, or ""
    for no body. Path parameters are named after the request fields they hold.
    """

    method: str
    path: str
    body: str
    path_params: tuple[tuple[str, str], ...] = dataclasses.field(init=False)
    body_field: str = dataclasses.field(init=False)

    def __post_init__(self) -> None:
        params = tuple((param, json_name(param)) for param in re.findall(r"\{([^}]+)\}", self.path))
        object.__setattr__(self, "path_params", params)
        object.__setattr__(self, "body_field", self.body if self.body in ("*", "") else json_name(self.body))


def json_name(attribute: str) -> str:
    """The JSON name of a message attribute, such as nodeId for node_id."""
    head, *rest = attribute.rstrip("_").split("_")
    return head + "".join(part[:1].upper() + part[1:] for part in rest)


_field_cache: dict[type, tuple[tuple[str, str, Any, Any], ...]] = {}


def _fields(cls: type) -> tuple[tuple[str, str, Any, Any], ...]:
    if cls in _field_cache:
        return _field_cache[cls]
    hints = typing.get_type_hints(cls)
    result = []
    for field in dataclasses.fields(cls):
        if field.default is not dataclasses.MISSING:
            default = field.default
        elif field.default_factory is not dataclasses.MISSING:
            default = field.default_factory()
        else:
            default = dataclasses.MISSING
        result.append((field.name, json_name(field.name), hints[field.name], default))
    _field_cache[cls] = tuple(result)
    return _field_cache[cls]


def _format_timestamp(value: datetime.datetime) -> str:
    return value.astimezone(datetime.UTC).isoformat().replace("+00:00", "Z")


def _encode(value: Any) -> Any:
    if dataclasses.is_dataclass(value) and not isinstance(value, type):
        return to_json(value)
    if isinstance(value, enum.Enum):
        return value.value
    if isinstance(value, bool | int | str):
        return value
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "Infinity" if value > 0 else "-Infinity"
        return value
    if isinstance(value, bytes):
        return base64.b64encode(value).decode()
    if isinstance(value, datetime.datetime):
        return _format_timestamp(value)
    if isinstance(value, Mapping):
        return {_encode_key(key): _encode(item) for key, item in value.items()}
    if isinstance(value, Sequence):
        return [_encode(item) for item in value]
    raise TypeError(f"cannot send a {type(value).__name__} to the API")


def _encode_key(key: Any) -> str:
    if isinstance(key, bool):
        return "true" if key else "false"
    return str(key)


def to_json(message: Any) -> Json:
    """The proto JSON of a message, leaving out fields that hold their default."""
    result: Json = {}
    for attribute, name, _, default in _fields(type(message)):
        value = getattr(message, attribute)
        if value is None or (default is not None and value == default):
            continue
        result[name] = _encode(value)
    return result


def _unwrap_optional(hint: Any) -> Any:
    if typing.get_origin(hint) in (typing.Union, types.UnionType):
        return next(arg for arg in typing.get_args(hint) if arg is not type(None))
    return hint


def _decode(hint: Any, value: Any) -> Any:
    hint = _unwrap_optional(hint)
    origin = typing.get_origin(hint)
    if origin is list:
        (item_hint,) = typing.get_args(hint)
        return [_decode(item_hint, item) for item in value]
    if origin is dict:
        key_hint, item_hint = typing.get_args(hint)
        return {_decode_key(key_hint, key): _decode(item_hint, item) for key, item in value.items()}
    if dataclasses.is_dataclass(hint):
        return from_json(typing.cast(type, hint), value)
    if hint is bool:
        return value is True or value == "true"
    if hint is int:
        return int(value)
    if hint is float:
        return float(value)
    if hint is bytes:
        return base64.b64decode(value + "=" * (-len(value) % 4), altchars=b"-_")
    if hint is datetime.datetime:
        return datetime.datetime.fromisoformat(value)
    if isinstance(hint, type) and issubclass(hint, enum.Enum):
        return hint(str(value))
    return value


def _decode_key(hint: Any, key: str) -> Any:
    if hint is int:
        return int(key)
    if hint is bool:
        return key == "true"
    return key


def from_json(cls: type[T], data: Mapping[str, Any]) -> T:
    """Reads a message from its proto JSON. Unknown fields are ignored."""
    values = {}
    for attribute, name, hint, _ in _fields(cls):
        value = data.get(name)
        if value is not None:
            values[attribute] = _decode(hint, value)
    return cls(**values)


def _is_set(value: Any) -> bool:
    return value is not None and value != ""


# Maps and lists of messages cannot be sent in a query string.
def _needs_body(request: Json, path_fields: set[str]) -> bool:
    return any(
        field not in path_fields
        and (isinstance(value, dict) or (isinstance(value, list) and any(isinstance(item, dict) for item in value)))
        for field, value in request.items()
    )


# Picks the first route whose path parameters are all set, preferring one that
# sends the whole request as the body when the request needs a body.
def _select_route(routes: Sequence[Route], request: Json) -> Route:
    usable = [route for route in routes if all(_is_set(request.get(field)) for _, field in route.path_params)]
    for route in usable:
        if route.body == "*" and _needs_body(request, {field for _, field in route.path_params}):
            return route
    return usable[0] if usable else routes[0]


def _append_query(query: list[tuple[str, str]], prefix: str, value: Any) -> None:
    if value is None:
        return
    if isinstance(value, list):
        for item in value:
            _append_query(query, prefix, item)
    elif isinstance(value, dict):
        for key, item in value.items():
            _append_query(query, f"{prefix}.{key}", item)
    elif isinstance(value, bool):
        query.append((prefix, "true" if value else "false"))
    else:
        query.append((prefix, str(value)))


def _error_from_status(status: Any, fallback: str, http_status: int = 0) -> ApiError:
    if not isinstance(status, dict):
        return ApiError(Code.UNKNOWN, fallback, http_status)
    return ApiError(status.get("code", Code.UNKNOWN), status.get("message") or fallback, http_status)


def _error_from_body(body: bytes | bytearray, reason: str, http_status: int) -> ApiError:
    try:
        status = json.loads(body)
    except ValueError:
        status = None
    return _error_from_status(status, reason, http_status)


def _error_from_transport(error: Exception) -> ApiError:
    if isinstance(error, httpx.TimeoutException):
        return ApiError(Code.DEADLINE_EXCEEDED, f"timed out: {error}")
    return ApiError(Code.UNAVAILABLE, f"could not reach the node: {error}")


def _error_from_handshake(error: Exception) -> ApiError:
    if isinstance(error, websockets.exceptions.InvalidStatus):
        response = error.response
        return _error_from_body(response.body or b"", response.reason_phrase, response.status_code)
    return ApiError(Code.UNAVAILABLE, f"could not open stream: {error}")


class _Requests:
    """Turns a call into the HTTP request of one of its routes."""

    def __init__(self, base_url: str, headers: Mapping[str, str] | None) -> None:
        self.base_url = base_url.rstrip("/")
        self.headers = dict(headers or {})

    def url(self, route: Route, request: Json, websocket: bool = False) -> str:
        path_fields = {field for _, field in route.path_params}
        path = route.path
        for param, field in route.path_params:
            path = path.replace(f"{{{param}}}", urllib.parse.quote(str(request.get(field, "")), safe=""))

        query: list[tuple[str, str]] = []
        if route.body != "*":
            for field, value in request.items():
                if field not in path_fields and field != route.body_field:
                    _append_query(query, field, value)

        base = "ws" + self.base_url.removeprefix("http") if websocket else self.base_url
        search = urllib.parse.urlencode(query)
        return base + path + (f"?{search}" if search else "")

    def body(self, route: Route, request: Json) -> bytes | None:
        if route.body == "":
            return None
        if route.body != "*":
            return json.dumps(request.get(route.body_field, {})).encode()
        path_fields = {field for _, field in route.path_params}
        return json.dumps({field: value for field, value in request.items() if field not in path_fields}).encode()

    def build(
        self,
        client: httpx.Client | httpx.AsyncClient,
        routes: Sequence[Route],
        message: Any,
        accept: str,
        stream: bool,
    ) -> httpx.Request:
        request = to_json(message)
        route = _select_route(routes, request)
        body = self.body(route, request)
        headers = {"Accept": accept}
        if body is not None:
            headers["Content-Type"] = "application/json"
        headers.update(self.headers)
        # A quiet stream is not a stalled one.
        timeout = client.timeout
        if stream:
            timeout = httpx.Timeout(connect=timeout.connect, read=None, write=timeout.write, pool=timeout.pool)
        return client.build_request(
            route.method, self.url(route, request), headers=headers, content=body, timeout=timeout
        )


# Parses server-sent events, yielding the data of each message and raising the
# status of an error event.
class _Events:
    def __init__(self) -> None:
        self.name = ""
        self.data: list[str] = []

    def line(self, line: str) -> Json | None:
        if line == "":
            name, data = self.name, "\n".join(self.data)
            self.name, self.data = "", []
            if not data:
                return None
            message = json.loads(data)
            if name == "error":
                raise _error_from_status(message, "stream failed")
            return typing.cast(Json, message)
        if line.startswith(":"):
            return None
        field, _, value = line.partition(":")
        value = value.removeprefix(" ")
        if field == "event":
            self.name = value
        elif field == "data":
            self.data.append(value)
        return None


def _shutdown(response: httpx.Response) -> None:
    stream = response.extensions.get("network_stream")
    sock = stream.get_extra_info("socket") if stream is not None else None
    if isinstance(sock, socket.socket):
        with contextlib.suppress(OSError):
            sock.shutdown(socket.SHUT_RDWR)


class ServerStream(Generic[T]):
    """A stream of messages sent as server-sent events.

    It is ready when the call returns, so no later message is missed. Read the
    messages with `for`: the loop ends when the stream ends and raises an
    ApiError when it fails. `close` stops it, also from another thread.
    """

    def __init__(self, response: httpx.Response, message_type: type[T]) -> None:
        self._response = response
        self._message_type = message_type
        self._closed = False
        self._ended = False

    def __iter__(self) -> Iterator[T]:
        events = _Events()
        try:
            for line in self._response.iter_lines():
                message = events.line(line)
                if message is not None:
                    yield from_json(self._message_type, message)
            self._ended = True
        except httpx.HTTPError as error:
            if not self._closed:
                raise ApiError(Code.UNAVAILABLE, f"stream failed: {error}") from error
        finally:
            self.close()

    def close(self) -> None:
        if not self._closed:
            self._closed = True
            # Wakes a read blocked in another thread.
            if not self._ended:
                _shutdown(self._response)
            self._response.close()

    def __enter__(self) -> ServerStream[T]:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


class AsyncServerStream(Generic[T]):
    """A stream of messages sent as server-sent events.

    `await` it, or enter it with `async with`, to open it: it is then ready, so
    no later message is missed. Read the messages with `async for`, which opens
    it first if needed: the loop ends when the stream ends and raises an
    ApiError when it fails.
    """

    def __init__(self, open: Callable[[], Awaitable[httpx.Response]], message_type: type[T]) -> None:
        self._open = open
        self._message_type = message_type
        self._response: httpx.Response | None = None

    async def _opened(self) -> httpx.Response:
        if self._response is None:
            self._response = await self._open()
        return self._response

    async def _ready(self) -> AsyncServerStream[T]:
        await self._opened()
        return self

    def __await__(self) -> Generator[Any, None, AsyncServerStream[T]]:
        return self._ready().__await__()

    async def __aenter__(self) -> AsyncServerStream[T]:
        return await self._ready()

    async def __aexit__(self, *_: object) -> None:
        await self.aclose()

    async def __aiter__(self) -> AsyncIterator[T]:
        response = await self._opened()
        events = _Events()
        try:
            async for line in response.aiter_lines():
                message = events.line(line)
                if message is not None:
                    yield from_json(self._message_type, message)
        except httpx.HTTPError as error:
            if not response.is_closed:
                raise ApiError(Code.UNAVAILABLE, f"stream failed: {error}") from error
        finally:
            await self.aclose()

    async def aclose(self) -> None:
        if self._response is not None:
            await self._response.aclose()


def _received(raw: str | bytes, message_type: type[T]) -> T | None:
    message = json.loads(raw)
    if message.get("error") is not None:
        raise _error_from_status(message["error"], "stream failed")
    if message.get("result") is not None:
        return from_json(message_type, message["result"])
    return None


class BidiStream(Generic[Req, Res]):
    """A stream in both directions over a WebSocket.

    Send requests with `send` and read responses with `for`. The loop ends when
    the stream closes and raises an ApiError when the stream fails. `close`
    stops it, also from another thread.
    """

    def __init__(self, connection: websockets.sync.client.ClientConnection, message_type: type[Res]) -> None:
        self._connection = connection
        self._message_type = message_type
        self._closed = False

    def send(self, request: Req) -> None:
        try:
            self._connection.send(json.dumps(to_json(request)))
        except websockets.exceptions.ConnectionClosed as error:
            raise ApiError(Code.UNAVAILABLE, f"stream closed: {error}") from error

    def __iter__(self) -> Iterator[Res]:
        try:
            for raw in self._connection:
                message = _received(raw, self._message_type)
                if message is not None:
                    yield message
        except websockets.exceptions.ConnectionClosedError as error:
            if not self._closed:
                raise ApiError(Code.UNAVAILABLE, f"stream failed: {error}") from error
        finally:
            self.close()

    def close(self) -> None:
        self._closed = True
        self._connection.close()

    def __enter__(self) -> BidiStream[Req, Res]:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


class AsyncBidiStream(Generic[Req, Res]):
    """A stream in both directions over a WebSocket.

    `await` it, or enter it with `async with`, to open it. Send requests with
    `send` and read responses with `async for`, which both open it first if
    needed. The loop ends when the stream closes and raises an ApiError when
    the stream fails.
    """

    def __init__(
        self,
        open: Callable[[], Awaitable[websockets.asyncio.client.ClientConnection]],
        message_type: type[Res],
    ) -> None:
        self._open = open
        self._message_type = message_type
        self._connection: websockets.asyncio.client.ClientConnection | None = None
        self._closed = False

    async def _opened(self) -> websockets.asyncio.client.ClientConnection:
        if self._connection is None:
            self._connection = await self._open()
        return self._connection

    async def _ready(self) -> AsyncBidiStream[Req, Res]:
        await self._opened()
        return self

    def __await__(self) -> Generator[Any, None, AsyncBidiStream[Req, Res]]:
        return self._ready().__await__()

    async def __aenter__(self) -> AsyncBidiStream[Req, Res]:
        return await self._ready()

    async def __aexit__(self, *_: object) -> None:
        await self.aclose()

    async def send(self, request: Req) -> None:
        connection = await self._opened()
        try:
            await connection.send(json.dumps(to_json(request)))
        except websockets.exceptions.ConnectionClosed as error:
            raise ApiError(Code.UNAVAILABLE, f"stream closed: {error}") from error

    async def __aiter__(self) -> AsyncIterator[Res]:
        connection = await self._opened()
        try:
            async for raw in connection:
                message = _received(raw, self._message_type)
                if message is not None:
                    yield message
        except websockets.exceptions.ConnectionClosedError as error:
            if not self._closed:
                raise ApiError(Code.UNAVAILABLE, f"stream failed: {error}") from error
        finally:
            await self.aclose()

    async def aclose(self) -> None:
        self._closed = True
        if self._connection is not None:
            await self._connection.close()


class Transport:
    """Sends the calls of the blocking client."""

    def __init__(
        self,
        base_url: str,
        headers: Mapping[str, str] | None,
        timeout: float | None,
        http_client: httpx.Client | None,
    ) -> None:
        self._requests = _Requests(base_url, headers)
        self._owns_client = http_client is None
        self._client = http_client or httpx.Client(timeout=timeout)

    def _send(self, routes: Sequence[Route], message: Any, accept: str, stream: bool = False) -> httpx.Response:
        request = self._requests.build(self._client, routes, message, accept, stream)
        try:
            response = self._client.send(request, stream=stream)
        except httpx.TransportError as error:
            raise _error_from_transport(error) from error
        if response.is_error:
            body = response.read()
            response.close()
            raise _error_from_body(body, response.reason_phrase, response.status_code)
        return response

    def unary(self, routes: Sequence[Route], message: Any, response_type: type[T]) -> T:
        return from_json(response_type, self._send(routes, message, "application/json").json())

    def text(self, routes: Sequence[Route], message: Any) -> str:
        return self._send(routes, message, "text/plain").text

    def server_stream(self, routes: Sequence[Route], message: Any, response_type: type[T]) -> ServerStream[T]:
        return ServerStream(self._send(routes, message, "text/event-stream", stream=True), response_type)

    def bidi_stream(self, route: Route, response_type: type[Res]) -> BidiStream[Any, Res]:
        url = self._requests.url(route, {}, websocket=True)
        try:
            connection = websockets.sync.client.connect(url, additional_headers=self._requests.headers)
        except (OSError, TimeoutError, websockets.exceptions.InvalidHandshake) as error:
            raise _error_from_handshake(error) from error
        return BidiStream(connection, response_type)

    def close(self) -> None:
        if self._owns_client:
            self._client.close()


class AsyncTransport:
    """Sends the calls of the asyncio client."""

    def __init__(
        self,
        base_url: str,
        headers: Mapping[str, str] | None,
        timeout: float | None,
        http_client: httpx.AsyncClient | None,
    ) -> None:
        self._requests = _Requests(base_url, headers)
        self._owns_client = http_client is None
        self._client = http_client or httpx.AsyncClient(timeout=timeout)

    async def _send(self, routes: Sequence[Route], message: Any, accept: str, stream: bool = False) -> httpx.Response:
        request = self._requests.build(self._client, routes, message, accept, stream)
        try:
            response = await self._client.send(request, stream=stream)
        except httpx.TransportError as error:
            raise _error_from_transport(error) from error
        if response.is_error:
            body = await response.aread()
            await response.aclose()
            raise _error_from_body(body, response.reason_phrase, response.status_code)
        return response

    async def unary(self, routes: Sequence[Route], message: Any, response_type: type[T]) -> T:
        response = await self._send(routes, message, "application/json")
        return from_json(response_type, response.json())

    async def text(self, routes: Sequence[Route], message: Any) -> str:
        return (await self._send(routes, message, "text/plain")).text

    def server_stream(self, routes: Sequence[Route], message: Any, response_type: type[T]) -> AsyncServerStream[T]:
        return AsyncServerStream(lambda: self._send(routes, message, "text/event-stream", stream=True), response_type)

    def bidi_stream(self, route: Route, response_type: type[Res]) -> AsyncBidiStream[Any, Res]:
        url = self._requests.url(route, {}, websocket=True)

        async def open() -> websockets.asyncio.client.ClientConnection:
            try:
                return await websockets.asyncio.client.connect(url, additional_headers=self._requests.headers)
            except (OSError, TimeoutError, websockets.exceptions.InvalidHandshake) as error:
                raise _error_from_handshake(error) from error

        return AsyncBidiStream(open, response_type)

    async def aclose(self) -> None:
        if self._owns_client:
            await self._client.aclose()
