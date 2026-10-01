# NanoPing API for Python

A typed client for the REST API of a [NanoPing](https://nanoping.com) node. It
covers every method of the API, with helpers for flows that take more than one
call, such as joining a hub. It has a blocking and an asyncio client, and needs
Python 3.11 or later.

This repository is generated from the NanoPing sources on every release, and
its version matches the NanoPing release it was made from. Changes made here
are overwritten by the next release.

## Install

```bash
pip install nanoping-api
```

## Use

```python
from nanoping_api import NanopingClient

client = NanopingClient("http://127.0.0.1:10565")

local = client.hub_client.get_local_node_id()
for update in client.hub_client.stream_connection_state():
    print(update.state)
```

`AsyncNanopingClient` has the same methods for asyncio, and its streams are
read with `async for`. Requests and responses are dataclasses, and the fields of
a request are passed as keyword arguments. A failed call raises an `ApiError`,
whose `code` says why, such as `Code.NOT_FOUND`.

## Examples

`examples` holds the program the
[HTTP REST guide](https://docs.nanoping.com/api/http-rest) is made from. It
joins a node to a hub and manages pipelines on both. Start the two nodes as the
comment in `examples/main.py` describes, then run

```bash
pip install nanoping-api
python examples/main.py --client http://127.0.0.1:10565 --server http://127.0.0.1:10566
```

The API is documented at https://docs.nanoping.com/api/reference.
