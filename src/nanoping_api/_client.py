from __future__ import annotations

import inspect
from collections.abc import AsyncIterator, Awaitable, Callable, Iterator, Mapping
from typing import Self

import httpx

from ._generated import (
    AuthenticationByRequestAnswer,
    AuthenticationByRequestRequest,
    Message,
    Options,
    _AsyncServices,
    _Services,
)
from ._runtime import AsyncTransport, Transport

_EVERY_LINE = Options(lines=2**63 - 1)


class NanopingClient(_Services):
    """A blocking client for the REST API of a node.

    `base_url` is the address of the REST API, such as "http://127.0.0.1:10565",
    and `headers` are sent with every request. `timeout` limits each call, in
    seconds, but not the wait for the next message of a stream. By default a call
    waits as long as it takes. Pass `http_client` to send the calls with an
    httpx.Client of your own.
    """

    def __init__(
        self,
        base_url: str,
        *,
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
        http_client: httpx.Client | None = None,
    ) -> None:
        self._transport = Transport(base_url, headers, timeout, http_client)
        super().__init__(self._transport)

    def close(self) -> None:
        """Closes the connections of the client, unless they belong to `http_client`."""
        self._transport.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def join_hub(self, hub_server_address: str) -> None:
        """Joins the hub server at `hub_server_address` with the node hosting the API.

        Returns once the hub server approved the node. Raises an ApiError with
        Code.UNAUTHENTICATED when the request was rejected, Code.DEADLINE_EXCEEDED
        when nobody answered in time and Code.ALREADY_EXISTS when the node already
        is part of a hub.
        """
        self.hub_client.authenticate_by_request(hub_server_address=hub_server_address)

    def answer_join_requests(self, decide: Callable[[AuthenticationByRequestRequest], bool]) -> None:
        """Answers the nodes that ask to join the hub server hosted by the node hosting
        the API.

        `decide` is called for every request and returns whether the node may join.
        Runs until the stream ends or fails.
        """
        with self.hub_server.authentication_by_requests() as stream:
            for request in stream:
                stream.send(AuthenticationByRequestAnswer(request_id=request.request_id, accept=decide(request)))

    def run_pipeline(self, node_id: str, pipeline_id: str) -> Iterator[Message]:
        """Starts a pipeline and follows the log of the new run from its first line.

        The pipeline starts when the loop does. Yields each log message until the
        log stream ends or the loop stops, which closes the stream.
        """
        run = self.pipelines.start_pipeline(node_id=node_id, id=pipeline_id)
        with self.pipelines.open_log_stream(node_id=node_id, run_id=run.run_id, options=_EVERY_LINE) as stream:
            for batch in stream:
                yield from batch.messages


class AsyncNanopingClient(_AsyncServices):
    """An asyncio client for the REST API of a node.

    `base_url` is the address of the REST API, such as "http://127.0.0.1:10565",
    and `headers` are sent with every request. `timeout` limits each call, in
    seconds, but not the wait for the next message of a stream. By default a call
    waits as long as it takes. Pass `http_client` to send the calls with an
    httpx.AsyncClient of your own.
    """

    def __init__(
        self,
        base_url: str,
        *,
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        self._transport = AsyncTransport(base_url, headers, timeout, http_client)
        super().__init__(self._transport)

    async def aclose(self) -> None:
        """Closes the connections of the client, unless they belong to `http_client`."""
        await self._transport.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.aclose()

    async def join_hub(self, hub_server_address: str) -> None:
        """Joins the hub server at `hub_server_address` with the node hosting the API.

        Returns once the hub server approved the node. Raises an ApiError with
        Code.UNAUTHENTICATED when the request was rejected, Code.DEADLINE_EXCEEDED
        when nobody answered in time and Code.ALREADY_EXISTS when the node already
        is part of a hub.
        """
        await self.hub_client.authenticate_by_request(hub_server_address=hub_server_address)

    async def answer_join_requests(
        self, decide: Callable[[AuthenticationByRequestRequest], bool | Awaitable[bool]]
    ) -> None:
        """Answers the nodes that ask to join the hub server hosted by the node hosting
        the API.

        `decide` is called for every request and returns, or resolves to, whether
        the node may join. Runs until the stream ends or fails, or the task is
        cancelled.
        """
        async with self.hub_server.authentication_by_requests() as stream:
            async for request in stream:
                accept = decide(request)
                if inspect.isawaitable(accept):
                    accept = await accept
                await stream.send(AuthenticationByRequestAnswer(request_id=request.request_id, accept=accept))

    async def run_pipeline(self, node_id: str, pipeline_id: str) -> AsyncIterator[Message]:
        """Starts a pipeline and follows the log of the new run from its first line.

        The pipeline starts when the loop does. Yields each log message until the
        log stream ends or the loop stops, which closes the stream.
        """
        run = await self.pipelines.start_pipeline(node_id=node_id, id=pipeline_id)
        async with self.pipelines.open_log_stream(node_id=node_id, run_id=run.run_id, options=_EVERY_LINE) as stream:
            async for batch in stream:
                for message in batch.messages:
                    yield message
