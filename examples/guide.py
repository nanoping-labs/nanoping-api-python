"""The code of the HTTP REST guide in the NanoPing docs. Each step of the guide is
one function, and run runs them in order."""

import asyncio
from collections.abc import Callable
from dataclasses import dataclass

from nanoping_api import (
    ApiError,
    AsyncNanopingClient,
    AsyncServerStream,
    Code,
    HubNode,
    Level,
    NodeMetadata,
    NodeMetadataItem,
    NodeService,
    RestartPolicy,
    RestartPolicyOnFailure,
    StreamPipelinesEvent,
)
from pipeline_config import PIPELINE_CONFIG

Output = Callable[[str], None]


@dataclass
class Addresses:
    """Addresses of the two nodes the guide uses: a client node that joins the hub,
    and the node hosting the hub server."""

    client: str
    """REST API of the client node, e.g. "http://127.0.0.1:10565"."""
    server: str
    """REST API of the hub server node, e.g. "http://127.0.0.1:10566"."""
    server_http: str
    """HTTP address of the hub server node, e.g. "http://127.0.0.1:8769"."""


async def set_node_information(client: AsyncNanopingClient, out: Output) -> None:
    """Names the client node and gives it metadata that other nodes on the hub can
    filter on."""
    local = await client.hub_client.get_local_node_id()

    response = await client.hub_client.set_node(
        node_id=local.node_id,
        name="My NanoPing Client",
        metadata=NodeMetadata(
            items={
                "type": NodeMetadataItem(string_value="my-type"),
                "location": NodeMetadataItem(string_value="Denmark, Aalborg"),
            }
        ),
    )

    out(f'Named node {response.node.id} "{response.node.name}"')


async def watch_connection_state(client: AsyncNanopingClient, out: Output) -> None:
    """Prints the connection state of the client node every time it changes, until
    the task is cancelled."""
    async for update in client.hub_client.stream_connection_state():
        out(f"Connection state: {update.state}")


async def accept_join_requests(server: AsyncNanopingClient) -> None:
    """Accepts every node that asks to join the hub server, until the task is
    cancelled."""
    await server.answer_join_requests(lambda request: True)


async def join_the_hub(client: AsyncNanopingClient, server_http_address: str, out: Output) -> None:
    """Joins the client node to the hub server. The call waits until the hub server
    accepted or rejected the request. A node that already is part of the hub stays
    so."""
    try:
        await client.join_hub(server_http_address)
        out("Joined the hub")
    except ApiError as error:
        if error.code == Code.ALREADY_EXISTS:
            out("Already part of the hub")
            return
        if error.code == Code.UNAUTHENTICATED:
            raise RuntimeError("The hub server rejected the node") from error
        raise


async def print_nodes(client: AsyncNanopingClient, out: Output) -> None:
    """Prints the nodes on the hub: all of them, the ones with metadata "type" set
    to "my-type", and the ones running pipelines."""
    everything = await client.hub_server.get_nodes()
    out("All nodes:")
    for node in everything.nodes:
        out(f"  {node.name}")

    my_type = await client.hub_server.get_nodes(
        metadata_filters={"type": NodeMetadataItem(string_value="my-type")},
    )
    out("Nodes with type my-type:")
    for node in my_type.nodes:
        out(f"  {node.name}")

    out("Nodes running pipelines:")
    for node in await pipeline_nodes(client):
        out(f"  {node.name}")


async def pipeline_nodes(client: AsyncNanopingClient) -> list[HubNode]:
    """Returns the nodes on the hub that run pipelines."""
    response = await client.hub_server.get_nodes(service_filters=[NodeService.PIPELINES])
    return response.nodes


async def watch_pipelines(
    client: AsyncNanopingClient, node: HubNode
) -> AsyncServerStream[StreamPipelinesEvent]:
    """Opens a stream of the changes to the pipelines on the node. It returns once
    the stream is ready, so no change made after it returns is missed."""
    return await client.pipelines.stream_pipelines(node_id=node.id)


async def print_pipeline_events(
    events: AsyncServerStream[StreamPipelinesEvent], node: HubNode, out: Output
) -> None:
    """Prints an event every time a pipeline on the node is created, updated or
    deleted, until the task is cancelled."""
    async for event in events:
        if event.create:
            out(f'  Event on {node.name}: created "{event.create.pipeline.name}"')
        elif event.update:
            out(f'  Event on {node.name}: updated "{event.update.pipeline.name}"')
        elif event.delete:
            out(f'  Event on {node.name}: deleted "{event.delete.pipeline.name}"')


async def manage_pipeline(client: AsyncNanopingClient, node_id: str, out: Output) -> None:
    """Creates a pipeline on the node, renames it, reads it back and deletes it
    again."""
    created = await client.pipelines.create_pipeline(
        node_id=node_id,
        name="My First Pipeline",
        json_config=PIPELINE_CONFIG,
        restart_policy=RestartPolicy(on_failure=RestartPolicyOnFailure(max_restarts=3)),
        default_logging_level=Level.DEBUG,
    )
    pipeline = created.pipeline
    out(f'  Created "{pipeline.name}"')

    # An update replaces every setting, so send the current ones along with the
    # new name.
    updated = await client.pipelines.update_pipeline(
        node_id=node_id,
        id=pipeline.id,
        name="My Renamed Pipeline",
        json_config=pipeline.json_config,
        restart_policy=pipeline.restart_policy,
        startup_policy=pipeline.startup_policy,
        default_logging_level=pipeline.default_logging_level,
        instructions_timeout=pipeline.instructions_timeout,
    )
    out(f'  Renamed to "{updated.pipeline.name}"')

    fetched = await client.pipelines.get_pipeline_by_id(node_id=node_id, id=pipeline.id)
    out(f'  Read back "{fetched.pipeline.name}"')

    await client.pipelines.delete_pipeline(node_id=node_id, id=pipeline.id)
    out(f'  Deleted "{fetched.pipeline.name}"')


async def run(addresses: Addresses, out: Output) -> None:
    """Connects to both nodes and runs every step of the guide."""
    async with (
        AsyncNanopingClient(addresses.client) as client,
        AsyncNanopingClient(addresses.server) as server,
    ):
        background: list[asyncio.Task[None]] = []
        try:
            background.append(asyncio.create_task(watch_connection_state(client, out)))
            await set_node_information(client, out)

            background.append(asyncio.create_task(accept_join_requests(server)))
            await join_the_hub(client, addresses.server_http, out)

            await print_nodes(client, out)

            for node in await pipeline_nodes(client):
                out(f"Managing a pipeline on {node.name}")
                events = await watch_pipelines(client, node)
                background.append(asyncio.create_task(print_pipeline_events(events, node, out)))
                await manage_pipeline(client, node.id, out)
        finally:
            for task in background:
                task.cancel()
            await asyncio.gather(*background, return_exceptions=True)
