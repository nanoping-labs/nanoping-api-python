# Generated from the gRPC bridge protos and HTTP rules. Do not edit.

from __future__ import annotations

import dataclasses
import datetime
from collections.abc import Mapping, Sequence

from ._runtime import (
    AsyncBidiStream,
    AsyncServerStream,
    AsyncTransport,
    BidiStream,
    ProtoEnum,
    Route,
    ServerStream,
    Transport,
)

__all__ = [
    "Address",
    "AsyncBlueprintsClient",
    "AsyncConfigServiceClient",
    "AsyncHubClientServiceClient",
    "AsyncHubServerServiceClient",
    "AsyncLoggingServiceClient",
    "AsyncNetworkInstancesClient",
    "AsyncNetworksClient",
    "AsyncPipelinesServiceClient",
    "AsyncResourcesServiceClient",
    "AuthenticateByRequestRequest",
    "AuthenticateByRequestResponse",
    "AuthenticationByRequestAnswer",
    "AuthenticationByRequestRequest",
    "Blueprint",
    "BlueprintWrite",
    "BlueprintsClient",
    "BoolMetric",
    "Carrier",
    "Collection",
    "ConfigCompatability",
    "ConfigServiceClient",
    "ConnectionState",
    "Constant",
    "CreateBlueprintRequest",
    "CreateBlueprintResponse",
    "CreateNetworkRequest",
    "CreateNetworkResponse",
    "CreatePipelineRequest",
    "CreatePipelineResponse",
    "DefaultNetworkCarrier",
    "DefaultNetworkCarrierAddress",
    "DefaultNetworkCarriers",
    "DeleteBlueprintRequest",
    "DeleteBlueprintResponse",
    "DeleteNetworkRequest",
    "DeleteNetworkResponse",
    "DeletePipelineRequest",
    "DeletePipelineResponse",
    "DisconnectRequest",
    "DisconnectResponse",
    "DownloadAppLogFileRequest",
    "DownloadLogFileChunk",
    "DownloadLogFileRequest",
    "DownloadNetworkInstanceLogFileRequest",
    "DownloadNetworkLogFileRequest",
    "DownloadPipelineRunLogFileRequest",
    "Enum8Metric",
    "Enum8Metric_EnumValue",
    "Float32Metric",
    "Float64Metric",
    "Flow",
    "FlowsSample",
    "GetBlueprintRequest",
    "GetBlueprintResponse",
    "GetBlueprintsRequest",
    "GetBlueprintsResponse",
    "GetDefaultNetworkCarriersRequest",
    "GetDefaultNetworkCarriersResponse",
    "GetLocalNodeIdRequest",
    "GetLocalNodeIdResponse",
    "GetNetworkInstancesRequest",
    "GetNetworkInstancesResponse",
    "GetNetworkPipelinesRequest",
    "GetNetworkPipelinesResponse",
    "GetNetworkRequest",
    "GetNetworkResponse",
    "GetNetworksRequest",
    "GetNetworksResponse",
    "GetNodeRequest",
    "GetNodeResponse",
    "GetNodesRequest",
    "GetNodesResponse",
    "GetPipelineByIdRequest",
    "GetPipelineByIdResponse",
    "GetPipelineByNameRequest",
    "GetPipelineByNameResponse",
    "GetPipelineByRunIdRequest",
    "GetPipelineByRunIdResponse",
    "GetPipelinesRequest",
    "GetPipelinesResponse",
    "HubClientServiceClient",
    "HubNode",
    "HubServerServiceClient",
    "Int32Metric",
    "Int64Metric",
    "Kind",
    "Kpi",
    "Level",
    "LogFileChunk",
    "LogStreamMessages",
    "LoggingOpenLogStreamRequest",
    "LoggingOpenNetworkInstanceLogStreamRequest",
    "LoggingOpenNetworkLogStreamRequest",
    "LoggingServiceClient",
    "Message",
    "Messages",
    "Metric",
    "MetricsSample",
    "Network",
    "NetworkBlueprints",
    "NetworkInstance",
    "NetworkInstanceLogStreamMessages",
    "NetworkInstancesClient",
    "NetworkLogStreamMessages",
    "NetworkPipeline",
    "NetworksClient",
    "NetworksNode",
    "NetworksOpenNetworkInstanceLogStreamRequest",
    "NetworksOpenNetworkLogStreamRequest",
    "NodeMetadata",
    "NodeMetadataItem",
    "NodeService",
    "NodeType",
    "OpenAppLogStreamRequest",
    "OpenFlowsStreamRequest",
    "OpenMetricsStreamRequest",
    "OpenPipelineRunLogStreamRequest",
    "OpenTelemetryStreamRequest",
    "Options",
    "Pipeline",
    "PipelineOpenLogStreamRequest",
    "PipelinesServiceClient",
    "RemoveNodeRequest",
    "RemoveNodeResponse",
    "ResourcesServiceClient",
    "RestartPolicy",
    "RestartPolicyAlways",
    "RestartPolicyNever",
    "RestartPolicyOnFailure",
    "SetDefaultNetworkCarriersRequest",
    "SetDefaultNetworkCarriersResponse",
    "SetNodeRequest",
    "SetNodeResponse",
    "StartPipelineRequest",
    "StartPipelineResponse",
    "StartupPolicy",
    "StartupPolicyAuto",
    "StartupPolicyManual",
    "StopPipelineRequest",
    "StopPipelineResponse",
    "StreamConnectionStateRequest",
    "StreamConnectionStateResponse",
    "StreamNetworkInstanceCreateEvent",
    "StreamNetworkInstanceDeleteEvent",
    "StreamNetworkInstanceEvent",
    "StreamNetworkInstanceUpdateEvent",
    "StreamNetworkInstancesRequest",
    "StreamNetworkPipelineCreateEvent",
    "StreamNetworkPipelineDeleteEvent",
    "StreamNetworkPipelineEvent",
    "StreamNetworkPipelineUpdateEvent",
    "StreamNetworkPipelinesRequest",
    "StreamNetworksCreateEvent",
    "StreamNetworksDeleteEvent",
    "StreamNetworksEvent",
    "StreamNetworksRequest",
    "StreamNetworksUpdateEvent",
    "StreamNodesInitialResponse",
    "StreamNodesResponse",
    "StreamNodesUpdateResponse",
    "StreamPipelinesCreateEvent",
    "StreamPipelinesDeleteEvent",
    "StreamPipelinesEvent",
    "StreamPipelinesRequest",
    "StreamPipelinesUpdateEvent",
    "TelemetrySample",
    "ToggleNetworkPipelineRequest",
    "ToggleNetworkPipelineResponse",
    "UInt32Metric",
    "UInt64Metric",
    "UpdateBlueprintRequest",
    "UpdateBlueprintResponse",
    "UpdateNetworkRequest",
    "UpdateNetworkResponse",
    "UpdatePipelineRequest",
    "UpdatePipelineResponse",
]


class ConnectionState(ProtoEnum):
    """Connection state between a node and its hub server."""

    UNAUTHENTICATED = "UNAUTHENTICATED"
    """The node is not authenticated with a hub server."""
    DISCONNECTED = "DISCONNECTED"
    """The node is authenticated but not connected to the hub server."""
    CONNECTED = "CONNECTED"
    """The node is connected to the hub server."""


class NodeService(ProtoEnum):
    """Services a node can offer."""

    HUB_SERVER = "HUB_SERVER"
    """The node hosts a hub server."""
    RESOURCES = "RESOURCES"
    """The node offers resources."""
    LOGGING = "LOGGING"
    """The node offers logging."""
    PIPELINES = "PIPELINES"
    """The node can run pipelines."""


class Level(ProtoEnum):
    """Severity of a log message, from the most verbose to the most severe."""

    STATE = "STATE"
    """State information, the most verbose level."""
    DEBUG = "DEBUG"
    """Debugging details."""
    INFO = "INFO"
    """General information."""
    WARNING = "WARNING"
    """Something unexpected that did not stop the operation."""
    ERROR = "ERROR"
    """An operation failed."""
    FATAL = "FATAL"
    """A failure the process could not recover from."""


class Kind(ProtoEnum):
    """How the value of a metric changes over time."""

    GAUGE = "GAUGE"
    """The value can both increase and decrease, for example memory in use."""
    COUNTER = "COUNTER"
    """The value can only increase, for example a total byte count."""


class NodeType(ProtoEnum):
    """The role of a node in a network."""

    NODE_TYPE_CLIENT = "NODE_TYPE_CLIENT"
    """A client node."""
    NODE_TYPE_RELAY = "NODE_TYPE_RELAY"
    """The relay node, named by the network's `relay_node_id`."""


class ConfigCompatability(ProtoEnum):
    """Whether the node can run a pipeline configuration."""

    COMPATIBLE = "COMPATIBLE"
    """The node can run the configuration."""
    INCOMPATIBLE = "INCOMPATIBLE"
    """The configuration was made for a newer NanoPing version than the one running on
    the node.
    """


@dataclasses.dataclass(kw_only=True)
class AuthenticateByRequestRequest:
    """Request for authenticateByRequest."""

    hub_server_address: str = ""
    """HTTP or HTTPS address of the hub server. Example: `http://127.0.0.1:8769`"""


@dataclasses.dataclass(kw_only=True)
class AuthenticateByRequestResponse:
    """Response for authenticateByRequest. Empty on success."""


@dataclasses.dataclass(kw_only=True)
class AuthenticationByRequestAnswer:
    """An answer to an authentication by request, sent by the caller."""

    request_id: int = 0
    """Id of the request being answered, as received in the request."""
    accept: bool = False
    """True to accept the request, false to reject it."""


@dataclasses.dataclass(kw_only=True)
class AuthenticationByRequestRequest:
    """An authentication by request from a node that wants to authenticate with the hub
    server.
    """

    node: HubNode = dataclasses.field(default_factory=lambda: HubNode())
    """Information about the node asking to authenticate."""
    request_id: int = 0
    """Id of the request, used when answering it."""


@dataclasses.dataclass(kw_only=True)
class DefaultNetworkCarrier:
    """A carrier a node receives every time it joins a new network. Every setting is
    optional.
    """

    address: DefaultNetworkCarrierAddress | None = None
    """Address the carrier uses."""
    interface: str | None = None
    """Name of the network interface the carrier uses. Example: `eth0`"""
    bandwidth_priority: int | None = None
    """Bandwidth priority of the carrier. Example: `100`"""


@dataclasses.dataclass(kw_only=True)
class DefaultNetworkCarrierAddress:
    """Address of a default network carrier."""

    ip: str = ""
    """IP address of the carrier. Example: `192.168.1.20`"""
    port: int = 0
    """Port of the carrier. Example: `3425`"""
    external_ip: str | None = None
    """IP address the carrier is reachable at from outside, for example behind NAT.
    Example: `203.0.113.10`
    """


@dataclasses.dataclass(kw_only=True)
class DefaultNetworkCarriers:
    """A list of default network carriers."""

    carriers: list[DefaultNetworkCarrier] = dataclasses.field(default_factory=list)
    """The default network carriers."""


@dataclasses.dataclass(kw_only=True)
class DisconnectRequest:
    """Request for disconnect."""


@dataclasses.dataclass(kw_only=True)
class DisconnectResponse:
    """Response for disconnect."""


@dataclasses.dataclass(kw_only=True)
class GetDefaultNetworkCarriersRequest:
    """Request for getDefaultNetworkCarriers."""

    node_id: str = ""
    """Id of the node to read the default network carriers from."""


@dataclasses.dataclass(kw_only=True)
class GetDefaultNetworkCarriersResponse:
    """Response for getDefaultNetworkCarriers."""

    carriers: list[DefaultNetworkCarrier] = dataclasses.field(default_factory=list)
    """The default network carriers of the node. Empty when none are configured."""


@dataclasses.dataclass(kw_only=True)
class GetLocalNodeIdRequest:
    """Request for getLocalNodeId."""


@dataclasses.dataclass(kw_only=True)
class GetLocalNodeIdResponse:
    """Response for getLocalNodeId."""

    node_id: str = ""
    """Id of the node hosting the API."""
    is_authenticated: bool = False
    """True if the node holds a sign-in to a hub server. It may still be disconnected
    from it at the moment.
    """


@dataclasses.dataclass(kw_only=True)
class GetNodeRequest:
    """Request for getNode."""

    node_id: str = ""
    """Id of the node to get information about, for example the id returned by
    getLocalNodeId.
    """


@dataclasses.dataclass(kw_only=True)
class GetNodeResponse:
    """Response for getNode."""

    node: HubNode = dataclasses.field(default_factory=lambda: HubNode())
    """Information about the node."""


@dataclasses.dataclass(kw_only=True)
class GetNodesRequest:
    """Filters for listing the nodes of the hub server. All given filters must match for
    a node to be included.
    """

    metadata_filters: dict[str, NodeMetadataItem] = dataclasses.field(default_factory=dict)
    """Metadata filters keyed by metadata key. A node is included only if it has every
    key with an equal value of the same type. Leave empty to not filter by metadata.
    """
    service_filters: list[NodeService] = dataclasses.field(default_factory=list)
    """Service filters. A node is included only if it offers every listed service. Leave
    empty to not filter by service.
    """


@dataclasses.dataclass(kw_only=True)
class GetNodesResponse:
    """Response for getNodes."""

    nodes: list[HubNode] = dataclasses.field(default_factory=list)
    """The nodes matching the filters."""


@dataclasses.dataclass(kw_only=True)
class HubNode:
    """Information about a node."""

    id: str = ""
    """Unique id of the node."""
    name: str = ""
    """Human readable name of the node."""
    online: bool = False
    """Whether the node is currently online and connected to the hub server."""
    services: list[NodeService] = dataclasses.field(default_factory=list)
    """Services offered by the node."""
    metadata: NodeMetadata = dataclasses.field(default_factory=lambda: NodeMetadata())
    """Metadata of the node."""


@dataclasses.dataclass(kw_only=True)
class NodeMetadata:
    """User defined key/value metadata attached to a node."""

    items: dict[str, NodeMetadataItem] = dataclasses.field(default_factory=dict)
    """Metadata items keyed by name."""


@dataclasses.dataclass(kw_only=True)
class NodeMetadataItem:
    """A single metadata value of a node. Set exactly one of the value fields."""

    bytes_value: bytes | None = None
    """Raw bytes value."""
    string_value: str | None = None
    """Text value."""
    int_value: int | None = None
    """Signed 64-bit integer value."""
    uint_value: int | None = None
    """Unsigned 64-bit integer value."""
    double_value: float | None = None
    """64-bit floating point value."""
    float_value: float | None = None
    """32-bit floating point value."""
    bool_value: bool | None = None
    """Boolean value."""


@dataclasses.dataclass(kw_only=True)
class RemoveNodeRequest:
    """Request for removeNode."""

    node_id: str = ""
    """Id of the node to remove."""


@dataclasses.dataclass(kw_only=True)
class RemoveNodeResponse:
    """Response for removeNode."""


@dataclasses.dataclass(kw_only=True)
class SetDefaultNetworkCarriersRequest:
    """Request for setDefaultNetworkCarriers."""

    node_id: str = ""
    """Id of the node to set the default network carriers on."""
    carriers: DefaultNetworkCarriers | None = None
    """The new default network carriers, replacing the current ones. Leave unset to
    remove all default carriers.
    """


@dataclasses.dataclass(kw_only=True)
class SetDefaultNetworkCarriersResponse:
    """Response for setDefaultNetworkCarriers."""


@dataclasses.dataclass(kw_only=True)
class SetNodeRequest:
    """Request for setNode."""

    node_id: str = ""
    """Id of the node to change."""
    name: str = ""
    """New name of the node. Example: `edge-node-1`"""
    metadata: NodeMetadata = dataclasses.field(default_factory=lambda: NodeMetadata())
    """New metadata of the node. Replaces all existing metadata, so leaving it empty
    removes the metadata.
    """


@dataclasses.dataclass(kw_only=True)
class SetNodeResponse:
    """Response for setNode."""

    node: HubNode = dataclasses.field(default_factory=lambda: HubNode())
    """The node information after the change."""


@dataclasses.dataclass(kw_only=True)
class StreamConnectionStateRequest:
    """Request for streamConnectionState."""


@dataclasses.dataclass(kw_only=True)
class StreamConnectionStateResponse:
    """A connection state update."""

    state: ConnectionState = ConnectionState.UNAUTHENTICATED
    """The current connection state."""


@dataclasses.dataclass(kw_only=True)
class StreamNodesInitialResponse:
    """The nodes of the hub server when the stream opened."""

    nodes: list[HubNode] = dataclasses.field(default_factory=list)
    """The nodes matching the filters."""


@dataclasses.dataclass(kw_only=True)
class StreamNodesResponse:
    """A message on the streamNodes stream."""

    initial_response: StreamNodesInitialResponse | None = None
    """Sent once as the first message, with the nodes matching the filters when the
    stream opened.
    """
    update_response: StreamNodesUpdateResponse | None = None
    """Sent for every later change to a node."""


@dataclasses.dataclass(kw_only=True)
class StreamNodesUpdateResponse:
    """A change to a single node. Exactly one field is set, telling what changed."""

    connected_node: HubNode | None = None
    """The node connected to the hub server."""
    disconnected_node: HubNode | None = None
    """The node disconnected from the hub server."""
    authenticated_node: HubNode | None = None
    """The node was authenticated with the hub server."""
    deauthenticated_node: HubNode | None = None
    """The node was deauthenticated and removed from the hub server."""
    updated_metadata_node: HubNode | None = None
    """The node's metadata changed."""
    updated_name_node: HubNode | None = None
    """The node's name changed."""


@dataclasses.dataclass(kw_only=True)
class DownloadAppLogFileRequest:
    """Selects the node's application log file. Takes no parameters."""


@dataclasses.dataclass(kw_only=True)
class DownloadLogFileChunk:
    """One message of a log file download: either a piece of the file or an error."""

    error: str | None = None
    """Why the file could not be read, for example because it does not exist. No more
    chunks follow.
    """
    file_chunk: LogFileChunk | None = None
    """The next piece of the file."""


@dataclasses.dataclass(kw_only=True)
class DownloadLogFileRequest:
    """Downloads one log file from a node."""

    node_id: str = ""
    """ID of the node that holds the log file."""
    app_log_file_request: DownloadAppLogFileRequest | None = None
    """Download the node's application log."""
    pipeline_run_log_file_request: DownloadPipelineRunLogFileRequest | None = None
    """Download the log of a pipeline run."""
    network_log_file_request: DownloadNetworkLogFileRequest | None = None
    """Download the log of a network."""
    network_instance_log_file_request: DownloadNetworkInstanceLogFileRequest | None = None
    """Download the log of a network instance."""


@dataclasses.dataclass(kw_only=True)
class DownloadNetworkInstanceLogFileRequest:
    """Selects the log file of a network instance."""

    network_instance_id: str = ""
    """ID of the network instance. Must not be empty."""


@dataclasses.dataclass(kw_only=True)
class DownloadNetworkLogFileRequest:
    """Selects the log file of a network."""

    network_id: str = ""
    """ID of the network. Must not be empty."""


@dataclasses.dataclass(kw_only=True)
class DownloadPipelineRunLogFileRequest:
    """Selects the log file of a pipeline run."""

    pipeline_run_id: str = ""
    """ID of the pipeline run. Must not be empty."""


@dataclasses.dataclass(kw_only=True)
class LogFileChunk:
    """A piece of a log file."""

    content: bytes = b""
    """Raw file bytes, up to 64 KiB per chunk."""


@dataclasses.dataclass(kw_only=True)
class Message:
    """A single log entry."""

    timestamp: datetime.datetime | None = None
    """When the entry was logged."""
    level: Level = Level.STATE
    """Severity of the entry."""
    message: str = ""
    """The log text. Holds the whole raw line when no message could be extracted from
    it.
    """
    data: str = ""
    """The raw log line when it is valid JSON, so structured fields can be read from it.
    Empty otherwise.
    """


@dataclasses.dataclass(kw_only=True)
class Messages:
    """A batch of log entries, oldest first."""

    messages: list[Message] = dataclasses.field(default_factory=list)
    """The log entries."""


@dataclasses.dataclass(kw_only=True)
class OpenAppLogStreamRequest:
    """Selects the node's application log. Takes no parameters."""


@dataclasses.dataclass(kw_only=True)
class LoggingOpenLogStreamRequest:
    """Opens a stream of log messages from one log on a node."""

    node_id: str = ""
    """ID of the node whose log to stream."""
    options: Options = dataclasses.field(default_factory=lambda: Options())
    """Stream options. When unset, only new entries are sent."""
    app_log_stream_request: OpenAppLogStreamRequest | None = None
    """Stream the node's application log."""
    pipeline_run_log_stream_request: OpenPipelineRunLogStreamRequest | None = None
    """Stream the log of a pipeline run."""
    network_log_stream_request: LoggingOpenNetworkLogStreamRequest | None = None
    """Stream the log of a network."""
    network_instance_log_stream_request: LoggingOpenNetworkInstanceLogStreamRequest | None = None
    """Stream the log of a network instance."""


@dataclasses.dataclass(kw_only=True)
class LoggingOpenNetworkInstanceLogStreamRequest:
    """Selects the log of a network instance."""

    network_instance_id: str = ""
    """ID of the network instance. Must not be empty."""


@dataclasses.dataclass(kw_only=True)
class LoggingOpenNetworkLogStreamRequest:
    """Selects the log of a network."""

    network_id: str = ""
    """ID of the network. Must not be empty."""


@dataclasses.dataclass(kw_only=True)
class OpenPipelineRunLogStreamRequest:
    """Selects the log of a pipeline run."""

    pipeline_run_id: str = ""
    """ID of the pipeline run. Must not be empty."""


@dataclasses.dataclass(kw_only=True)
class Options:
    """Options for opening a log stream."""

    lines: int | None = None
    """The number of entries."""


@dataclasses.dataclass(kw_only=True)
class BoolMetric:
    """A metric holding a true or false value."""

    value: bool | None = None
    """The value. Unset when the metric has no value in this sample."""
    description: str = ""
    """Human-readable description of what the metric measures."""
    unit: str | None = None
    """The unit. Unset when the value has no unit."""


@dataclasses.dataclass(kw_only=True)
class Collection:
    """A group of related metrics, such as the memory metrics of a node."""

    path: str = ""
    """Path identifying the collection, for example `/system/memory`."""
    metrics: dict[str, Metric] = dataclasses.field(default_factory=dict)
    """The metrics in the collection, keyed by metric name."""


@dataclasses.dataclass(kw_only=True)
class Constant:
    """A metric whose value never changes, such as the CPU architecture."""

    uint64: int | None = None
    """An unsigned integer value."""
    int64: int | None = None
    """A signed integer value."""
    float64: float | None = None
    """A floating-point value."""
    boolean: bool | None = None
    """A true or false value."""
    string: str | None = None
    """A text value."""
    description: str = ""
    """Human-readable description of what the constant describes."""
    unit: str | None = None
    """The unit. Unset when the value has no unit."""


@dataclasses.dataclass(kw_only=True)
class Enum8Metric:
    """A metric holding one value out of a fixed set of named values."""

    value: int | None = None
    """The index. Unset when the metric has no value in this sample."""
    description: str = ""
    """Human-readable description of what the metric measures."""
    values: dict[int, Enum8Metric_EnumValue] = dataclasses.field(default_factory=dict)
    """The values the metric can take, keyed by index."""
    unit: str | None = None
    """The unit. Unset when the value has no unit."""


@dataclasses.dataclass(kw_only=True)
class Enum8Metric_EnumValue:
    """A named value the metric can take."""

    name: str = ""
    """Name of the value."""
    description: str | None = None
    """The description."""


@dataclasses.dataclass(kw_only=True)
class Float32Metric:
    """A metric holding a 32-bit floating-point value."""

    value: float | None = None
    """The value. Unset when the metric has no value in this sample."""
    description: str = ""
    """Human-readable description of what the metric measures."""
    kind: Kind = Kind.GAUGE
    """Whether the value can only increase or can also decrease."""
    unit: str | None = None
    """The unit, for example `bytes` or `percent`. Unset when the value has no unit."""
    min: float | None = None
    """The minimum. Unset when there is no known lower bound."""
    max: float | None = None
    """The maximum. Unset when there is no known upper bound."""


@dataclasses.dataclass(kw_only=True)
class Float64Metric:
    """A metric holding a 64-bit floating-point value."""

    value: float | None = None
    """The value. Unset when the metric has no value in this sample."""
    description: str = ""
    """Human-readable description of what the metric measures."""
    kind: Kind = Kind.GAUGE
    """Whether the value can only increase or can also decrease."""
    unit: str | None = None
    """The unit, for example `bytes` or `percent`. Unset when the value has no unit."""
    min: float | None = None
    """The minimum. Unset when there is no known lower bound."""
    max: float | None = None
    """The maximum. Unset when there is no known upper bound."""


@dataclasses.dataclass(kw_only=True)
class Int32Metric:
    """A metric holding a signed 32-bit integer value."""

    value: int | None = None
    """The value. Unset when the metric has no value in this sample."""
    description: str = ""
    """Human-readable description of what the metric measures."""
    kind: Kind = Kind.GAUGE
    """Whether the value can only increase or can also decrease."""
    unit: str | None = None
    """The unit, for example `bytes` or `percent`. Unset when the value has no unit."""
    min: int | None = None
    """The minimum. Unset when there is no known lower bound."""
    max: int | None = None
    """The maximum. Unset when there is no known upper bound."""


@dataclasses.dataclass(kw_only=True)
class Int64Metric:
    """A metric holding a signed 64-bit integer value."""

    value: int | None = None
    """The value. Unset when the metric has no value in this sample."""
    description: str = ""
    """Human-readable description of what the metric measures."""
    kind: Kind = Kind.GAUGE
    """Whether the value can only increase or can also decrease."""
    unit: str | None = None
    """The unit, for example `bytes` or `percent`. Unset when the value has no unit."""
    min: int | None = None
    """The minimum. Unset when there is no known lower bound."""
    max: int | None = None
    """The maximum. Unset when there is no known upper bound."""


@dataclasses.dataclass(kw_only=True)
class Metric:
    """A single metric. Exactly one of the fields is set, depending on the metric's
    type.
    """

    constant: Constant | None = None
    """A metric with a fixed value."""
    uint64: UInt64Metric | None = None
    """An unsigned 64-bit integer metric."""
    int64: Int64Metric | None = None
    """A signed 64-bit integer metric."""
    uint32: UInt32Metric | None = None
    """An unsigned 32-bit integer metric."""
    int32: Int32Metric | None = None
    """A signed 32-bit integer metric."""
    float64: Float64Metric | None = None
    """A 64-bit floating-point metric."""
    float32: Float32Metric | None = None
    """A 32-bit floating-point metric."""
    boolean: BoolMetric | None = None
    """A true or false metric."""
    enum8: Enum8Metric | None = None
    """A metric with one of a fixed set of named values."""


@dataclasses.dataclass(kw_only=True)
class UInt32Metric:
    """A metric holding an unsigned 32-bit integer value."""

    value: int | None = None
    """The value. Unset when the metric has no value in this sample."""
    description: str = ""
    """Human-readable description of what the metric measures."""
    kind: Kind = Kind.GAUGE
    """Whether the value can only increase or can also decrease."""
    unit: str | None = None
    """The unit, for example `bytes` or `percent`. Unset when the value has no unit."""
    min: int | None = None
    """The minimum. Unset when there is no known lower bound."""
    max: int | None = None
    """The maximum. Unset when there is no known upper bound."""


@dataclasses.dataclass(kw_only=True)
class UInt64Metric:
    """A metric holding an unsigned 64-bit integer value."""

    value: int | None = None
    """The value. Unset when the metric has no value in this sample."""
    description: str = ""
    """Human-readable description of what the metric measures."""
    kind: Kind = Kind.GAUGE
    """Whether the value can only increase or can also decrease."""
    unit: str | None = None
    """The unit, for example `bytes` or `percent`. Unset when the value has no unit."""
    min: int | None = None
    """The minimum. Unset when there is no known lower bound."""
    max: int | None = None
    """The maximum. Unset when there is no known upper bound."""


@dataclasses.dataclass(kw_only=True)
class Address:
    """The address of a carrier."""

    ip: str = ""
    """The IP address. Example: `192.168.1.20`"""
    port: int = 0
    """The port. Example: `3425`"""
    external_ip: str | None = None
    """The external IP address of the carrier. Example: `203.0.113.10`"""


@dataclasses.dataclass(kw_only=True)
class Blueprint:
    """A network blueprint."""

    name: str = ""
    """The name of the blueprint."""
    template: str = ""
    """The template that renders a pipeline configuration. Placeholders such as `{{
    .node.ip }}` are filled in with network and node parameters.
    """
    read_only: bool = False
    """Whether the blueprint is read-only. The built-in blueprints are read-only and
    cannot be updated or deleted.
    """


@dataclasses.dataclass(kw_only=True)
class BlueprintWrite:
    """The editable fields of a blueprint."""

    name: str = ""
    """The name of the blueprint. Example: `UDP relay`"""
    template: str = ""
    """The template that renders a pipeline configuration. Placeholders such as `{{
    .node.ip }}` are filled in with network and node parameters.
    """


@dataclasses.dataclass(kw_only=True)
class Carrier:
    """A connection a node uses to carry network traffic."""

    address: Address | None = None
    """The IP address and port of the carrier."""
    interface: str | None = None
    """The name of the network interface to use. Example: `eth0`"""
    bandwidth_priority: int | None = None
    """The bandwidth priority of the carrier."""


@dataclasses.dataclass(kw_only=True)
class CreateBlueprintRequest:
    """Request to create a blueprint."""

    blueprint: BlueprintWrite = dataclasses.field(default_factory=lambda: BlueprintWrite())
    """The blueprint to create. Required."""


@dataclasses.dataclass(kw_only=True)
class CreateBlueprintResponse:
    """The created blueprint."""

    id: str = ""
    """The generated ID of the blueprint."""
    blueprint: Blueprint = dataclasses.field(default_factory=lambda: Blueprint())
    """The created blueprint."""


@dataclasses.dataclass(kw_only=True)
class CreateNetworkRequest:
    """Request to create a network."""

    network: Network = dataclasses.field(default_factory=lambda: Network())
    """The network to create. Required."""


@dataclasses.dataclass(kw_only=True)
class CreateNetworkResponse:
    """The created network."""

    id: str = ""
    """The generated ID of the network."""
    network: Network = dataclasses.field(default_factory=lambda: Network())
    """The created network."""


@dataclasses.dataclass(kw_only=True)
class DeleteBlueprintRequest:
    """Request to delete a blueprint."""

    id: str = ""
    """The ID of the blueprint to delete."""


@dataclasses.dataclass(kw_only=True)
class DeleteBlueprintResponse:
    """Empty response to a blueprint deletion."""


@dataclasses.dataclass(kw_only=True)
class DeleteNetworkRequest:
    """Request to delete a network."""

    id: str = ""
    """The ID of the network to delete."""


@dataclasses.dataclass(kw_only=True)
class DeleteNetworkResponse:
    """Empty response to a network deletion."""


@dataclasses.dataclass(kw_only=True)
class GetBlueprintRequest:
    """Request for a single blueprint."""

    id: str = ""
    """The ID of the blueprint to fetch."""


@dataclasses.dataclass(kw_only=True)
class GetBlueprintResponse:
    """A blueprint and its ID."""

    id: str = ""
    """The ID of the blueprint."""
    blueprint: Blueprint = dataclasses.field(default_factory=lambda: Blueprint())
    """The blueprint."""


@dataclasses.dataclass(kw_only=True)
class GetBlueprintsRequest:
    """Request for all blueprints."""


@dataclasses.dataclass(kw_only=True)
class GetBlueprintsResponse:
    """All blueprints."""

    blueprints: list[GetBlueprintResponse] = dataclasses.field(default_factory=list)
    """The blueprints with their IDs."""


@dataclasses.dataclass(kw_only=True)
class GetNetworkInstancesRequest:
    """Request for the network instances on a node."""

    node_id: str = ""
    """The ID of the node to fetch network instances from."""


@dataclasses.dataclass(kw_only=True)
class GetNetworkInstancesResponse:
    """The network instances on a node."""

    network_instances: list[NetworkInstance] = dataclasses.field(default_factory=list)
    """The network instances of the node."""


@dataclasses.dataclass(kw_only=True)
class GetNetworkPipelinesRequest:
    """Request for the network instance pipelines on a node. Leave a filter unset to not
    filter on it.
    """

    node_id: str = ""
    """The ID of the node to fetch network instance pipelines from."""
    optional_network_id: str | None = None
    """Only return pipelines belonging to this network ID."""
    optional_instance_id: str | None = None
    """Only return pipelines belonging to this network instance ID."""
    optional_blueprint_id: str | None = None
    """Only return pipelines generated from this blueprint ID."""


@dataclasses.dataclass(kw_only=True)
class GetNetworkPipelinesResponse:
    """The matching network instance pipelines."""

    network_pipelines: list[NetworkPipeline] = dataclasses.field(default_factory=list)
    """The network instance pipelines."""


@dataclasses.dataclass(kw_only=True)
class GetNetworkRequest:
    """Request for a single network."""

    id: str = ""
    """The ID of the network to fetch."""


@dataclasses.dataclass(kw_only=True)
class GetNetworkResponse:
    """A network and its ID."""

    id: str = ""
    """The ID of the network."""
    network: Network = dataclasses.field(default_factory=lambda: Network())
    """The network."""


@dataclasses.dataclass(kw_only=True)
class GetNetworksRequest:
    """Request for all networks."""


@dataclasses.dataclass(kw_only=True)
class GetNetworksResponse:
    """All networks."""

    networks: list[GetNetworkResponse] = dataclasses.field(default_factory=list)
    """The networks with their IDs."""


@dataclasses.dataclass(kw_only=True)
class Network:
    """A virtual network connecting nodes through a central relay node."""

    name: str = ""
    """The name of the network. Must not be empty. Example: `Office network`"""
    subnet_cidr: str = ""
    """The IPv4 subnet, in CIDR notation, that node IP addresses are assigned from.
    Example: `100.65.254.0/24`
    """
    blueprints: NetworkBlueprints = dataclasses.field(default_factory=lambda: NetworkBlueprints())
    """The blueprints used to generate the network's pipelines."""
    parameters: str = ""
    """Parameters available to the network's blueprints, as a JSON object. May be empty.
    Example: `{ "raft_timeout": 9000, "loss_emulation_percentage": 1 }`
    """
    relay_node_id: str = ""
    """The node ID of the relay node. Must be the node that has networks enabled."""
    nodes: list[NetworksNode] = dataclasses.field(default_factory=list)
    """The nodes in the network, each with its assigned IP address and carriers."""


@dataclasses.dataclass(kw_only=True)
class NetworkBlueprints:
    """The blueprint IDs used for each role in a network. A blueprint left unset falls
    back to the default blueprint for that role configured on the networks node.
    """

    relay_blueprint: str | None = None
    """ID of the blueprint deployed to the relay node."""
    relay_client_blueprint: str | None = None
    """ID of the blueprint deployed to the relay node once for every client in the
    network.
    """
    client_blueprint: str | None = None
    """ID of the blueprint deployed to every node in the network."""


@dataclasses.dataclass(kw_only=True)
class NetworkInstance:
    """A network's instance on one node."""

    id: str = ""
    """The ID of the network instance."""
    network_id: str = ""
    """The ID of the network the instance belongs to."""
    network_name: str = ""
    """The name of the network the instance belongs to."""
    pipeline_ids: list[str] = dataclasses.field(default_factory=list)
    """The IDs of the pipelines managed by the network instance."""


@dataclasses.dataclass(kw_only=True)
class NetworkInstanceLogStreamMessages:
    """A batch of network instance log messages."""

    messages: list[Message] = dataclasses.field(default_factory=list)
    """The log messages."""


@dataclasses.dataclass(kw_only=True)
class NetworkLogStreamMessages:
    """A batch of network log messages."""

    messages: list[Message] = dataclasses.field(default_factory=list)
    """The log messages."""


@dataclasses.dataclass(kw_only=True)
class NetworkPipeline:
    """A pipeline generated for a network instance from one of the network's blueprints.
    """

    id: str = ""
    """The ID of this network instance pipeline record. Not the same as `pipeline_id`.
    """
    network_id: str = ""
    """The ID of the network the pipeline belongs to."""
    instance_id: str = ""
    """The ID of the network instance the pipeline belongs to."""
    blueprint_id: str = ""
    """The ID of the blueprint the pipeline was generated from."""
    pipeline_id: str = ""
    """The ID of the pipeline on the node."""
    pipeline_name: str = ""
    """The name of the pipeline."""
    enabled: bool = False
    """Whether the pipeline is enabled, meaning it should be running."""


@dataclasses.dataclass(kw_only=True)
class NetworksNode:
    """A node's membership in a network."""

    node_id: str = ""
    """The ID of the node."""
    node_ip: str = ""
    """The node's IP address in the network. Must be unique within the network and
    cannot be changed. Example: `100.65.254.2`
    """
    carriers: list[Carrier] = dataclasses.field(default_factory=list)
    """The carriers the node uses in the network. Each carrier of the relay node needs
    an `address`; each carrier of a client needs an `address` or an `interface`.
    """
    type: NodeType = NodeType.NODE_TYPE_CLIENT
    """The node's role, derived from the network's `relay_node_id`. Cannot be changed
    directly.
    """
    parameters: str = ""
    """Parameters for this node available to the blueprints, as a JSON object. May be
    empty.
    """


@dataclasses.dataclass(kw_only=True)
class NetworksOpenNetworkInstanceLogStreamRequest:
    """Request to stream the log of a network instance."""

    node_id: str = ""
    """The ID of the node the network instance runs on."""
    network_instance_id: str = ""
    """The ID of the network instance whose log to stream."""
    options: Options = dataclasses.field(default_factory=lambda: Options())
    """Log stream options, such as how many past lines to send first."""


@dataclasses.dataclass(kw_only=True)
class NetworksOpenNetworkLogStreamRequest:
    """Request to stream the log of a network."""

    network_id: str = ""
    """The ID of the network whose log to stream."""
    options: Options = dataclasses.field(default_factory=lambda: Options())
    """Log stream options, such as how many past lines to send first."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworkInstanceCreateEvent:
    """Sent when a network instance is created."""

    network_instance: NetworkInstance = dataclasses.field(default_factory=lambda: NetworkInstance())
    """The created network instance."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworkInstanceDeleteEvent:
    """Sent when a network instance is deleted."""

    network_instance: NetworkInstance = dataclasses.field(default_factory=lambda: NetworkInstance())
    """The deleted network instance."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworkInstanceEvent:
    """A change to a network instance."""

    create: StreamNetworkInstanceCreateEvent | None = None
    """A network instance was created."""
    update: StreamNetworkInstanceUpdateEvent | None = None
    """A network instance was updated."""
    delete: StreamNetworkInstanceDeleteEvent | None = None
    """A network instance was deleted."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworkInstanceUpdateEvent:
    """Sent when a network instance or one of its pipelines is updated."""

    network_instance: NetworkInstance = dataclasses.field(default_factory=lambda: NetworkInstance())
    """The network instance after the update."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworkInstancesRequest:
    """Request to stream network instance changes on a node."""

    node_id: str = ""
    """The ID of the node to stream network instances from."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworkPipelineCreateEvent:
    """Sent when a network instance pipeline is created."""

    network_pipeline: NetworkPipeline = dataclasses.field(default_factory=lambda: NetworkPipeline())
    """The created pipeline."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworkPipelineDeleteEvent:
    """Sent when a network instance pipeline is deleted."""

    network_pipeline: NetworkPipeline = dataclasses.field(default_factory=lambda: NetworkPipeline())
    """The deleted pipeline."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworkPipelineEvent:
    """A change to a network instance pipeline."""

    create: StreamNetworkPipelineCreateEvent | None = None
    """A pipeline was created."""
    update: StreamNetworkPipelineUpdateEvent | None = None
    """A pipeline was updated."""
    delete: StreamNetworkPipelineDeleteEvent | None = None
    """A pipeline was deleted."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworkPipelineUpdateEvent:
    """Sent when a network instance pipeline is updated."""

    network_pipeline: NetworkPipeline = dataclasses.field(default_factory=lambda: NetworkPipeline())
    """The pipeline after the update."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworkPipelinesRequest:
    """Request to stream network instance pipeline changes on a node."""

    node_id: str = ""
    """The ID of the node to stream network instance pipelines from."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworksCreateEvent:
    """Sent when a network is created."""

    network: Network = dataclasses.field(default_factory=lambda: Network())
    """The created network."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworksDeleteEvent:
    """Sent when a network is deleted."""

    network: Network = dataclasses.field(default_factory=lambda: Network())
    """The deleted network."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworksEvent:
    """A change to a network."""

    create: StreamNetworksCreateEvent | None = None
    """A network was created."""
    update: StreamNetworksUpdateEvent | None = None
    """A network was updated."""
    delete: StreamNetworksDeleteEvent | None = None
    """A network was deleted."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworksRequest:
    """Request to stream network changes."""


@dataclasses.dataclass(kw_only=True)
class StreamNetworksUpdateEvent:
    """Sent when a network is updated."""

    network: Network = dataclasses.field(default_factory=lambda: Network())
    """The network after the update."""


@dataclasses.dataclass(kw_only=True)
class ToggleNetworkPipelineRequest:
    """Request to toggle a network instance pipeline. Set exactly one of
    `optional_pipeline_id` and `optional_instance_pipeline_id`.
    """

    node_id: str = ""
    """The ID of the node the pipeline runs on."""
    optional_pipeline_id: str | None = None
    """The pipeline's `pipeline_id`."""
    optional_instance_pipeline_id: str | None = None
    """The pipeline's `id`."""


@dataclasses.dataclass(kw_only=True)
class ToggleNetworkPipelineResponse:
    """Empty response to a pipeline toggle."""


@dataclasses.dataclass(kw_only=True)
class UpdateBlueprintRequest:
    """Request to update a blueprint."""

    id: str = ""
    """The ID of the blueprint to update."""
    blueprint: BlueprintWrite = dataclasses.field(default_factory=lambda: BlueprintWrite())
    """The new name and template. Required."""


@dataclasses.dataclass(kw_only=True)
class UpdateBlueprintResponse:
    """The updated blueprint."""

    id: str = ""
    """The ID of the blueprint."""
    blueprint: Blueprint = dataclasses.field(default_factory=lambda: Blueprint())
    """The blueprint after the update."""


@dataclasses.dataclass(kw_only=True)
class UpdateNetworkRequest:
    """Request to update a network."""

    id: str = ""
    """The ID of the network to update."""
    network: Network = dataclasses.field(default_factory=lambda: Network())
    """The new settings of the network. Required. All fields replace the current values,
    except `nodes`: leave it empty to keep the nodes unchanged, or list every current
    node to edit their carriers and parameters.
    """


@dataclasses.dataclass(kw_only=True)
class UpdateNetworkResponse:
    """The updated network."""

    id: str = ""
    """The ID of the network."""
    network: Network = dataclasses.field(default_factory=lambda: Network())
    """The network after the update."""


@dataclasses.dataclass(kw_only=True)
class CreatePipelineRequest:
    """Request to create a pipeline."""

    node_id: str = ""
    """ID of the node to create the pipeline on."""
    name: str = ""
    """Name of the pipeline. Example: `UDP tunnel`"""
    json_config: str = ""
    """The pipeline configuration as a JSON string."""
    restart_policy: RestartPolicy = dataclasses.field(default_factory=lambda: RestartPolicy())
    """The restart policy of the pipeline. Leave unset to never restart."""
    startup_policy: StartupPolicy = dataclasses.field(default_factory=lambda: StartupPolicy())
    """The startup policy of the pipeline. Leave unset to start it manually only."""
    default_logging_level: Level | None = None
    """The default logging level."""
    node_reference_id: str | None = None
    """ID of the related node."""
    instructions_timeout: int | None = None
    """The timeout in seconds. Must be greater than 0. Example: `30`"""
    cpu_pin: int | None = None
    """Zero indexed CPU thread number. Must be lower than the node's thread count."""
    performance_mode: bool | None = None
    """True to run the pinned thread in performance mode."""


@dataclasses.dataclass(kw_only=True)
class CreatePipelineResponse:
    """The created pipeline."""

    pipeline: Pipeline = dataclasses.field(default_factory=lambda: Pipeline())
    """The new pipeline, including its generated `id`."""


@dataclasses.dataclass(kw_only=True)
class DeletePipelineRequest:
    """Request to delete a pipeline."""

    node_id: str = ""
    """ID of the node that hosts the pipeline."""
    id: str = ""
    """ID of the pipeline to delete."""


@dataclasses.dataclass(kw_only=True)
class DeletePipelineResponse:
    """Empty response, returned when the pipeline is deleted."""


@dataclasses.dataclass(kw_only=True)
class GetPipelineByIdRequest:
    """Request to get a pipeline by its ID."""

    node_id: str = ""
    """ID of the node that hosts the pipeline."""
    id: str = ""
    """ID of the pipeline."""


@dataclasses.dataclass(kw_only=True)
class GetPipelineByIdResponse:
    """The requested pipeline."""

    pipeline: Pipeline = dataclasses.field(default_factory=lambda: Pipeline())
    """The pipeline with the given ID."""


@dataclasses.dataclass(kw_only=True)
class GetPipelineByNameRequest:
    """Request to get a pipeline by its name."""

    node_id: str = ""
    """ID of the node that hosts the pipeline."""
    name: str = ""
    """Exact name of the pipeline. Example: `UDP tunnel`"""


@dataclasses.dataclass(kw_only=True)
class GetPipelineByNameResponse:
    """The requested pipeline."""

    pipeline: Pipeline = dataclasses.field(default_factory=lambda: Pipeline())
    """The pipeline with the given name."""


@dataclasses.dataclass(kw_only=True)
class GetPipelineByRunIdRequest:
    """Request to get the pipeline that a run belongs to."""

    node_id: str = ""
    """ID of the node that hosts the pipeline."""
    id: str = ""
    """ID of the run."""


@dataclasses.dataclass(kw_only=True)
class GetPipelineByRunIdResponse:
    """The pipeline that the run belongs to."""

    pipeline: Pipeline = dataclasses.field(default_factory=lambda: Pipeline())
    """The pipeline of the given run."""


@dataclasses.dataclass(kw_only=True)
class GetPipelinesRequest:
    """Request to list all pipelines."""

    node_id: str = ""
    """ID of the node to list the pipelines of."""


@dataclasses.dataclass(kw_only=True)
class GetPipelinesResponse:
    """All pipelines on the node."""

    pipelines: list[Pipeline] = dataclasses.field(default_factory=list)
    """The pipelines, in no particular order."""


@dataclasses.dataclass(kw_only=True)
class Kpi:
    """The value of one KPI defined in the pipeline configuration."""

    id: str = ""
    """ID of the KPI."""
    field: str = ""
    """Path of the KPI field this value was evaluated for, such as `value`."""
    error: str | None = None
    """The KPI could not be evaluated. Holds the error message."""
    none_value: bool | None = None
    """The KPI expression evaluated to no value."""
    unresolved: str | None = None
    """A metric the KPI uses could not be resolved. Holds the reason."""
    string_value: str | None = None
    """A text value."""
    uint64_value: int | None = None
    """An unsigned 64-bit integer value."""
    int64_value: int | None = None
    """A signed 64-bit integer value."""
    uint32_value: int | None = None
    """An unsigned 32-bit integer value."""
    int32_value: int | None = None
    """A signed 32-bit integer value."""
    float64_value: float | None = None
    """A 64-bit floating point value."""
    float32_value: float | None = None
    """A 32-bit floating point value."""
    bool_value: bool | None = None
    """A boolean value."""
    enum8_value: int | None = None
    """An 8-bit enum value, as its number."""


@dataclasses.dataclass(kw_only=True)
class LogStreamMessages:
    """A batch of log messages from a pipeline run."""

    messages: list[Message] = dataclasses.field(default_factory=list)
    """The log messages."""


@dataclasses.dataclass(kw_only=True)
class PipelineOpenLogStreamRequest:
    """Request to stream the logs of a pipeline run."""

    node_id: str = ""
    """ID of the node that hosts the run."""
    run_id: str = ""
    """ID of the run to stream logs from."""
    options: Options = dataclasses.field(default_factory=lambda: Options())
    """Stream options, such as how many past lines to send first. Leave unset to receive
    only new messages.
    """


@dataclasses.dataclass(kw_only=True)
class OpenTelemetryStreamRequest:
    """Request to stream the telemetry of a pipeline run."""

    node_id: str = ""
    """ID of the node that hosts the run."""
    run_id: str = ""
    """ID of the run to stream telemetry from."""


@dataclasses.dataclass(kw_only=True)
class Pipeline:
    """A pipeline is an executable composition of network components."""

    id: str = ""
    """ID of the pipeline."""
    name: str = ""
    """Name of the pipeline."""
    started: bool = False
    """Whether the pipeline is started."""
    current_run: str | None = None
    """ID of the current run."""
    json_config: str = ""
    """The pipeline configuration as a pretty-printed JSON string."""
    config_compatability: ConfigCompatability = ConfigCompatability.COMPATIBLE
    """Whether the node can run the configuration. Read-only."""
    restart_policy: RestartPolicy = dataclasses.field(default_factory=lambda: RestartPolicy())
    """The restart policy of the pipeline."""
    startup_policy: StartupPolicy = dataclasses.field(default_factory=lambda: StartupPolicy())
    """The startup policy of the pipeline."""
    default_logging_level: Level = Level.STATE
    """The default logging level of the pipeline."""
    node_reference_id: str | None = None
    """ID of the related node."""
    instructions_timeout: int = 0
    """Time in seconds before a pipeline instruction is considered timed out."""
    cpu_pin: int | None = None
    """Zero indexed CPU thread number."""
    performance_mode: bool = False
    """Whether the pinned CPU thread runs in performance mode."""


@dataclasses.dataclass(kw_only=True)
class RestartPolicy:
    """Decides whether a pipeline is restarted when its run ends. Unset means never."""

    never: RestartPolicyNever | None = None
    """Never restart the pipeline."""
    always: RestartPolicyAlways | None = None
    """Restart the pipeline each time its run ends."""
    on_failure: RestartPolicyOnFailure | None = None
    """Restart the pipeline only when its run fails."""


@dataclasses.dataclass(kw_only=True)
class RestartPolicyAlways:
    """Restart the pipeline each time its run ends."""

    max_restarts: int = 0
    """Maximum number of restarts. 0 means restart without limit."""


@dataclasses.dataclass(kw_only=True)
class RestartPolicyNever:
    """Never restart the pipeline when its run ends."""


@dataclasses.dataclass(kw_only=True)
class RestartPolicyOnFailure:
    """Restart the pipeline only when its run fails unexpectedly with a non-zero exit
    code.
    """

    max_restarts: int = 0
    """Maximum number of restarts. 0 means restart without limit."""


@dataclasses.dataclass(kw_only=True)
class StartPipelineRequest:
    """Request to start a pipeline."""

    node_id: str = ""
    """ID of the node that hosts the pipeline."""
    id: str | None = None
    """ID of the pipeline."""
    name: str | None = None
    """Exact name of the pipeline. Fails if more than one pipeline has this name.
    Example: `UDP tunnel`
    """


@dataclasses.dataclass(kw_only=True)
class StartPipelineResponse:
    """The run created by starting the pipeline."""

    run_id: str = ""
    """ID of the new run."""


@dataclasses.dataclass(kw_only=True)
class StartupPolicy:
    """Decides whether a pipeline starts by itself when the node's application starts.
    Unset means manual.
    """

    manual: StartupPolicyManual | None = None
    """Only start the pipeline when asked to."""
    auto: StartupPolicyAuto | None = None
    """Start the pipeline automatically when the application starts."""


@dataclasses.dataclass(kw_only=True)
class StartupPolicyAuto:
    """Start the pipeline automatically when the application starts."""


@dataclasses.dataclass(kw_only=True)
class StartupPolicyManual:
    """Do not start the pipeline automatically when the application starts."""


@dataclasses.dataclass(kw_only=True)
class StopPipelineRequest:
    """Request to stop a pipeline."""

    node_id: str = ""
    """ID of the node that hosts the pipeline."""
    id: str | None = None
    """ID of the pipeline."""
    name: str | None = None
    """Exact name of the pipeline. Fails if more than one pipeline has this name.
    Example: `UDP tunnel`
    """
    run_id: str | None = None
    """ID of the pipeline's current run."""


@dataclasses.dataclass(kw_only=True)
class StopPipelineResponse:
    """Empty response, returned when the stop is requested."""


@dataclasses.dataclass(kw_only=True)
class StreamPipelinesCreateEvent:
    """A pipeline was created."""

    pipeline: Pipeline = dataclasses.field(default_factory=lambda: Pipeline())
    """The created pipeline."""


@dataclasses.dataclass(kw_only=True)
class StreamPipelinesDeleteEvent:
    """A pipeline was deleted."""

    pipeline: Pipeline = dataclasses.field(default_factory=lambda: Pipeline())
    """The deleted pipeline, as it was before deletion."""


@dataclasses.dataclass(kw_only=True)
class StreamPipelinesEvent:
    """A single change to a pipeline."""

    create: StreamPipelinesCreateEvent | None = None
    """Sent when a pipeline is created."""
    update: StreamPipelinesUpdateEvent | None = None
    """Sent when a pipeline is changed, started or stopped."""
    delete: StreamPipelinesDeleteEvent | None = None
    """Sent when a pipeline is deleted."""


@dataclasses.dataclass(kw_only=True)
class StreamPipelinesRequest:
    """Request to stream pipeline changes."""

    node_id: str = ""
    """ID of the node to stream pipeline changes from."""


@dataclasses.dataclass(kw_only=True)
class StreamPipelinesUpdateEvent:
    """A pipeline was changed, started or stopped."""

    pipeline: Pipeline = dataclasses.field(default_factory=lambda: Pipeline())
    """The pipeline after the change."""


@dataclasses.dataclass(kw_only=True)
class TelemetrySample:
    """One telemetry sample of a pipeline run."""

    metric_collections: list[Collection] = dataclasses.field(default_factory=list)
    """The metrics of the run."""
    kpis: list[Kpi] = dataclasses.field(default_factory=list)
    """The KPI values of the run."""
    timestamp: datetime.datetime | None = None
    """When the sample was taken."""


@dataclasses.dataclass(kw_only=True)
class UpdatePipelineRequest:
    """Request to update a pipeline. All settings are replaced, so send the full set of
    values you want to keep.
    """

    node_id: str = ""
    """ID of the node that hosts the pipeline."""
    id: str = ""
    """ID of the pipeline to update."""
    name: str = ""
    """New name of the pipeline. Example: `UDP tunnel`"""
    json_config: str = ""
    """New pipeline configuration as a JSON string."""
    restart_policy: RestartPolicy = dataclasses.field(default_factory=lambda: RestartPolicy())
    """New restart policy of the pipeline. Unset means never restart."""
    startup_policy: StartupPolicy = dataclasses.field(default_factory=lambda: StartupPolicy())
    """New startup policy of the pipeline. Unset means start manually only."""
    default_logging_level: Level = Level.STATE
    """New default logging level of the pipeline. Unset means `STATE`, not the `INFO`
    default used on create.
    """
    instructions_timeout: int = 0
    """New time in seconds before a pipeline instruction is considered timed out. Must
    be greater than 0. Example: `30`
    """
    cpu_pin: int | None = None
    """Zero indexed CPU thread number. Must be lower than the node's thread count."""
    performance_mode: bool | None = None
    """True to run the pinned thread in performance mode."""
    node_reference_id: str | None = None
    """ID of the related node."""
    force_restart: bool = False
    """If true and the pipeline is running, the pipeline is restarted when the new
    configuration cannot be applied to the current run. The call then returns once
    the new run is running.
    """


@dataclasses.dataclass(kw_only=True)
class UpdatePipelineResponse:
    """The updated pipeline."""

    pipeline: Pipeline = dataclasses.field(default_factory=lambda: Pipeline())
    """The pipeline after the update."""


@dataclasses.dataclass(kw_only=True)
class Flow:
    """Traffic between two endpoints on one interface, tracked in both directions. A
    flow is dropped once it closes or has been idle for a while.
    """

    interface: str = ""
    """Name of the interface the flow was captured on."""
    protocol: str = ""
    """`TCP`, `UDP`, `ICMP`, or the IP protocol number for any other protocol."""
    source_ip: str = ""
    """IP address of the side that opened the flow, as far as the node can tell."""
    source_port: int = 0
    """Port on the source side. Zero for protocols without ports."""
    destination_ip: str = ""
    """IP address of the side the flow was opened towards."""
    destination_port: int = 0
    """Port on the destination side. Zero for protocols without ports."""
    sent_bytes: int = 0
    """Total bytes sent from source to destination."""
    sent_packets: int = 0
    """Total packets sent from source to destination."""
    received_bytes: int = 0
    """Total bytes sent from destination to source."""
    received_packets: int = 0
    """Total packets sent from destination to source."""
    bits_per_second: int = 0
    """Current throughput over both directions, in bits per second."""
    first_seen: datetime.datetime | None = None
    """When the first packet of the flow was captured."""
    last_seen: datetime.datetime | None = None
    """When the latest packet of the flow was captured."""


@dataclasses.dataclass(kw_only=True)
class FlowsSample:
    """The network flows of a node at one point in time."""

    timestamp: datetime.datetime | None = None
    """When the snapshot was taken."""
    flows: list[Flow] = dataclasses.field(default_factory=list)
    """Every flow the node currently tracks. Empty when none have been captured."""


@dataclasses.dataclass(kw_only=True)
class MetricsSample:
    """The resource metrics of a node at one point in time."""

    timestamp: datetime.datetime | None = None
    """When the sample was taken."""
    collections: list[Collection] = dataclasses.field(default_factory=list)
    """The metrics, grouped into collections such as `/system/memory` and
    `/system/disk`.
    """


@dataclasses.dataclass(kw_only=True)
class OpenFlowsStreamRequest:
    """Opens a stream of network flow snapshots."""

    node_id: str = ""
    """ID of the node to read flows from."""


@dataclasses.dataclass(kw_only=True)
class OpenMetricsStreamRequest:
    """Opens a stream of resource metrics."""

    node_id: str = ""
    """ID of the node to read metrics from."""


class BlueprintsClient:
    """A blueprint is a template that generates the pipeline configuration a node runs
    in a network. It uses [Go template syntax](https://pkg.go.dev/text/template), and
    placeholders such as the node's IP address and carriers are filled in for each
    node. Every network uses three blueprints: one for the relay node, one the relay
    runs for every client, and one for every client node. The built-in blueprints are
    read-only; create your own to change how networks carry traffic. Blueprints are
    stored on the connected node that has networks enabled, and calls wait until that
    node is connected.
    """

    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_blueprint(
        self,
        *,
        id: str = "",
    ) -> GetBlueprintResponse:
        """Get a single blueprint.

        Args:
            id: The ID of the blueprint to fetch.
        """
        return self._transport.unary(
            [Route("GET", "/v1/blueprints/{id}", "")],
            GetBlueprintRequest(id=id),
            GetBlueprintResponse,
        )

    def get_blueprints(self) -> GetBlueprintsResponse:
        """Get all blueprints, including the built-in read-only ones."""
        return self._transport.unary(
            [Route("GET", "/v1/blueprints", "")],
            GetBlueprintsRequest(),
            GetBlueprintsResponse,
        )

    def create_blueprint(
        self,
        *,
        blueprint: BlueprintWrite | None = None,
    ) -> CreateBlueprintResponse:
        """Create a blueprint and return it.

        Args:
            blueprint: The blueprint to create. Required.
        """
        return self._transport.unary(
            [Route("POST", "/v1/blueprints", "blueprint")],
            CreateBlueprintRequest(blueprint=blueprint or BlueprintWrite()),
            CreateBlueprintResponse,
        )

    def update_blueprint(
        self,
        *,
        id: str = "",
        blueprint: BlueprintWrite | None = None,
    ) -> UpdateBlueprintResponse:
        """Replace a blueprint and return the updated blueprint. Networks using the
        blueprint have their pipelines regenerated. Fails with a permission error for
        read-only blueprints.

        Args:
            id: The ID of the blueprint to update.
            blueprint: The new name and template. Required.
        """
        return self._transport.unary(
            [Route("PUT", "/v1/blueprints/{id}", "blueprint")],
            UpdateBlueprintRequest(id=id, blueprint=blueprint or BlueprintWrite()),
            UpdateBlueprintResponse,
        )

    def delete_blueprint(
        self,
        *,
        id: str = "",
    ) -> DeleteBlueprintResponse:
        """Delete a blueprint. Fails with a permission error for read-only blueprints.

        Args:
            id: The ID of the blueprint to delete.
        """
        return self._transport.unary(
            [Route("DELETE", "/v1/blueprints/{id}", "")],
            DeleteBlueprintRequest(id=id),
            DeleteBlueprintResponse,
        )


class ConfigServiceClient:
    """Settings stored in the configuration of a node. Use this service to read and
    change them on any node, such as the carriers a node uses by default when it
    joins a network.
    """

    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_default_network_carriers(
        self,
        *,
        node_id: str = "",
    ) -> GetDefaultNetworkCarriersResponse:
        """Get the default network carriers of a node. These are the carriers the node
        receives every time it joins a new network. Returns an empty list when none
        are configured.

        Args:
            node_id: Id of the node to read the default network carriers from.
        """
        return self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}/default-network-carriers", "")],
            GetDefaultNetworkCarriersRequest(node_id=node_id),
            GetDefaultNetworkCarriersResponse,
        )

    def set_default_network_carriers(
        self,
        *,
        node_id: str = "",
        carriers: DefaultNetworkCarriers | None = None,
    ) -> SetDefaultNetworkCarriersResponse:
        """Replace the default network carriers of a node. The new carriers apply to
        networks the node joins afterwards.

        Args:
            node_id: Id of the node to set the default network carriers on.
            carriers: The new default network carriers, replacing the current ones.
                Leave unset to remove all default carriers.
        """
        return self._transport.unary(
            [Route("PUT", "/v1/nodes/{node_id}/default-network-carriers", "carriers")],
            SetDefaultNetworkCarriersRequest(node_id=node_id, carriers=carriers),
            SetDefaultNetworkCarriersResponse,
        )


class HubClientServiceClient:
    """The hub client is the part of every node that connects it to a hub server, the
    control plane that lets connected nodes find and manage each other. Use this
    service to sign the node hosting the API in to a hub server, disconnect it,
    follow its connection state, and read or change the details of nodes.
    """

    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_local_node_id(self) -> GetLocalNodeIdResponse:
        """Get the ID of the node hosting the API, and whether it is authenticated with
        a hub server.
        """
        return self._transport.unary(
            [Route("GET", "/v1/hub-client/local-node-id", "")],
            GetLocalNodeIdRequest(),
            GetLocalNodeIdResponse,
        )

    def get_node(
        self,
        *,
        node_id: str = "",
    ) -> GetNodeResponse:
        """Get the details of a node. Fails with Unavailable when the node cannot be
        reached.

        Args:
            node_id: Id of the node to get information about, for example the id
                returned by getLocalNodeId.
        """
        return self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}", "")],
            GetNodeRequest(node_id=node_id),
            GetNodeResponse,
        )

    def set_node(
        self,
        *,
        node_id: str = "",
        name: str = "",
        metadata: NodeMetadata | None = None,
    ) -> SetNodeResponse:
        """Change the details of a node, replacing the current values. Fails with
        PermissionDenied when the node's configuration comes from a config file.

        Args:
            node_id: Id of the node to change.
            name: New name of the node. Example: `edge-node-1`
            metadata: New metadata of the node. Replaces all existing metadata, so
                leaving it empty removes the metadata.
        """
        return self._transport.unary(
            [Route("PUT", "/v1/nodes/{node_id}", "*")],
            SetNodeRequest(
                node_id=node_id,
                name=name,
                metadata=metadata or NodeMetadata(),
            ),
            SetNodeResponse,
        )

    def authenticate_by_request(
        self,
        *,
        hub_server_address: str = "",
    ) -> AuthenticateByRequestResponse:
        """Ask a hub server to authenticate the node hosting the API, and wait for the
        hub server to accept or reject the request. On success the node stays
        authenticated, also after a restart. Fails with AlreadyExists if the node is
        already authenticated, Unauthenticated if the request was rejected,
        DeadlineExceeded if the hub server did not answer in time, Unavailable if the
        hub server could not be reached, and NotFound if the hub server does not
        accept authentication by request.

        Args:
            hub_server_address: HTTP or HTTPS address of the hub server. Example:
                `http://127.0.0.1:8769`
        """
        return self._transport.unary(
            [Route("POST", "/v1/hub-client/authenticate-by-request", "*")],
            AuthenticateByRequestRequest(hub_server_address=hub_server_address),
            AuthenticateByRequestResponse,
        )

    def disconnect(self) -> DisconnectResponse:
        """Disconnect the node hosting the API from its hub server. The node always
        leaves, even if the hub server could not remove it from its list of nodes.
        """
        return self._transport.unary(
            [Route("POST", "/v1/hub-client/disconnect", "*")],
            DisconnectRequest(),
            DisconnectResponse,
        )

    def stream_connection_state(self) -> ServerStream[StreamConnectionStateResponse]:
        """Stream the connection state between the node hosting the API and its hub
        server. The current state is sent first, then a new message every time the
        state changes. The stream stays open until the caller closes it.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/hub-client/connection-state", "")],
            StreamConnectionStateRequest(),
            StreamConnectionStateResponse,
        )


class HubServerServiceClient:
    """A hub server is the control plane of a NanoPing setup: nodes authenticate with
    it, and every node on the same hub can find and manage the others. Use this
    service to list the nodes on the hub, follow them as they come and go, remove
    nodes, and approve or reject nodes that ask to join. The node hosting the API
    must host the hub server or be authenticated with one, otherwise calls fail with
    FailedPrecondition.
    """

    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_nodes(
        self,
        *,
        metadata_filters: Mapping[str, NodeMetadataItem] | None = None,
        service_filters: Sequence[NodeService] = (),
    ) -> GetNodesResponse:
        """Get the nodes authenticated with the hub server, optionally filtered.

        Args:
            metadata_filters: Metadata filters keyed by metadata key. A node is
                included only if it has every key with an equal value of the same type.
                Leave empty to not filter by metadata.
            service_filters: Service filters. A node is included only if it offers
                every listed service. Leave empty to not filter by service.
        """
        return self._transport.unary(
            [Route("GET", "/v1/nodes", ""), Route("POST", "/v1/nodes/search", "*")],
            GetNodesRequest(
                metadata_filters=dict(metadata_filters or {}),
                service_filters=list(service_filters),
            ),
            GetNodesResponse,
        )

    def remove_node(
        self,
        *,
        node_id: str = "",
    ) -> RemoveNodeResponse:
        """Remove a node from the hub server. This disconnects the node from the hub
        server and removes it from its networks.

        Args:
            node_id: Id of the node to remove.
        """
        return self._transport.unary(
            [Route("DELETE", "/v1/nodes/{node_id}", "")],
            RemoveNodeRequest(node_id=node_id),
            RemoveNodeResponse,
        )

    def stream_nodes(
        self,
        *,
        metadata_filters: Mapping[str, NodeMetadataItem] | None = None,
        service_filters: Sequence[NodeService] = (),
    ) -> ServerStream[StreamNodesResponse]:
        """Stream the nodes authenticated with the hub server. The matching nodes are
        sent first, followed by an update every time a node is authenticated,
        deauthenticated, connects, disconnects or changes its details. Updates are
        not filtered. The stream stays open until the caller closes it.

        Args:
            metadata_filters: Metadata filters keyed by metadata key. A node is
                included only if it has every key with an equal value of the same type.
                Leave empty to not filter by metadata.
            service_filters: Service filters. A node is included only if it offers
                every listed service. Leave empty to not filter by service.
        """
        return self._transport.server_stream(
            [
                Route("GET", "/v1/streams/nodes", ""),
                Route("POST", "/v1/streams/nodes", "*"),
            ],
            GetNodesRequest(
                metadata_filters=dict(metadata_filters or {}),
                service_filters=list(service_filters),
            ),
            StreamNodesResponse,
        )

    def authentication_by_requests(
        self,
    ) -> BidiStream[AuthenticationByRequestAnswer, AuthenticationByRequestRequest]:
        """Receive the authentication requests sent to the hub server on the node
        hosting the API, and accept or reject each one. Nothing is sent when the
        stream opens. A request is sent each time a node asks to authenticate, and
        the caller answers it by sending an answer for that request.
        """
        return self._transport.bidi_stream(
            Route("POST", "/v1/streams/hub-server/authentication-requests", "*"),
            AuthenticationByRequestRequest,
        )


class LoggingServiceClient:
    """Every node keeps logs: its application log, and a log for each pipeline run,
    network and network instance. Use this service to follow a log live or to
    download a complete log file, from any node.
    """

    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def open_log_stream(
        self,
        *,
        node_id: str = "",
        options: Options | None = None,
        app_log_stream_request: OpenAppLogStreamRequest | None = None,
        pipeline_run_log_stream_request: OpenPipelineRunLogStreamRequest | None = None,
        network_log_stream_request: LoggingOpenNetworkLogStreamRequest | None = None,
        network_instance_log_stream_request: LoggingOpenNetworkInstanceLogStreamRequest | None = None,
    ) -> ServerStream[Messages]:
        """Stream the log messages of one log on a node. The requested number of past
        entries is sent first, then new entries as they are written. Fails with an
        invalid argument error when the node is invalid or no log is chosen, and ends
        with an error when the log cannot be read or the node loses its connection.

        Args:
            node_id: ID of the node whose log to stream.
            options: Stream options. When unset, only new entries are sent.
            app_log_stream_request: Stream the node's application log.
            pipeline_run_log_stream_request: Stream the log of a pipeline run.
            network_log_stream_request: Stream the log of a network.
            network_instance_log_stream_request: Stream the log of a network
                instance.
        """
        return self._transport.server_stream(
            [Route("POST", "/v1/streams/nodes/{node_id}/logs", "*")],
            LoggingOpenLogStreamRequest(
                node_id=node_id,
                options=options or Options(),
                app_log_stream_request=app_log_stream_request,
                pipeline_run_log_stream_request=pipeline_run_log_stream_request,
                network_log_stream_request=network_log_stream_request,
                network_instance_log_stream_request=network_instance_log_stream_request,
            ),
            Messages,
        )

    def download_log_file(
        self,
        *,
        node_id: str = "",
        app_log_file_request: DownloadAppLogFileRequest | None = None,
        pipeline_run_log_file_request: DownloadPipelineRunLogFileRequest | None = None,
        network_log_file_request: DownloadNetworkLogFileRequest | None = None,
        network_instance_log_file_request: DownloadNetworkInstanceLogFileRequest | None = None,
    ) -> str:
        """Download one complete log file from a node as a series of chunks. Join the
        chunks in order to get the file. The stream ends when the whole file has been
        sent, or after an error chunk when the file could not be read.

        Returns the whole file as text.

        Args:
            node_id: ID of the node that holds the log file.
            app_log_file_request: Download the node's application log.
            pipeline_run_log_file_request: Download the log of a pipeline run.
            network_log_file_request: Download the log of a network.
            network_instance_log_file_request: Download the log of a network
                instance.
        """
        return self._transport.text(
            [Route("GET", "/v1/nodes/{node_id}/log-file", "")],
            DownloadLogFileRequest(
                node_id=node_id,
                app_log_file_request=app_log_file_request,
                pipeline_run_log_file_request=pipeline_run_log_file_request,
                network_log_file_request=network_log_file_request,
                network_instance_log_file_request=network_instance_log_file_request,
            ),
        )


class NetworkInstancesClient:
    """A network instance is a network's presence on one node: the pipelines generated
    for that node from the network's blueprints. Instances are created, updated and
    removed automatically when their network changes, so they cannot be managed
    directly. Use this service to see which networks a node takes part in, follow its
    network pipelines, turn them on or off, and read their logs. The node needs
    pipelines enabled.
    """

    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_network_instances(
        self,
        *,
        node_id: str = "",
    ) -> GetNetworkInstancesResponse:
        """Get all network instances on a node, each with its pipelines.

        Args:
            node_id: The ID of the node to fetch network instances from.
        """
        return self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}/network-instances", "")],
            GetNetworkInstancesRequest(node_id=node_id),
            GetNetworkInstancesResponse,
        )

    def stream_network_instances(
        self,
        *,
        node_id: str = "",
    ) -> ServerStream[StreamNetworkInstanceEvent]:
        """Stream changes to the network instances on a node. Nothing is sent when the
        stream opens; an event is sent each time an instance is created, updated or
        deleted, and an update is also sent when one of its pipelines changes. The
        stream ends if the connection to the node is lost.

        Args:
            node_id: The ID of the node to stream network instances from.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/nodes/{node_id}/network-instances", "")],
            StreamNetworkInstancesRequest(node_id=node_id),
            StreamNetworkInstanceEvent,
        )

    def get_network_pipelines(
        self,
        *,
        node_id: str = "",
        optional_network_id: str | None = None,
        optional_instance_id: str | None = None,
        optional_blueprint_id: str | None = None,
    ) -> GetNetworkPipelinesResponse:
        """Get the network instance pipelines on a node, optionally filtered. A pipeline
        must match every filter that is set.

        Args:
            node_id: The ID of the node to fetch network instance pipelines from.
            optional_network_id: Only return pipelines belonging to this network ID.
            optional_instance_id: Only return pipelines belonging to this network
                instance ID.
            optional_blueprint_id: Only return pipelines generated from this
                blueprint ID.
        """
        return self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}/network-pipelines", "")],
            GetNetworkPipelinesRequest(
                node_id=node_id,
                optional_network_id=optional_network_id,
                optional_instance_id=optional_instance_id,
                optional_blueprint_id=optional_blueprint_id,
            ),
            GetNetworkPipelinesResponse,
        )

    def stream_network_pipelines(
        self,
        *,
        node_id: str = "",
    ) -> ServerStream[StreamNetworkPipelineEvent]:
        """Stream changes to the network instance pipelines on a node. Nothing is sent
        when the stream opens; an event is sent each time a pipeline is created,
        updated or deleted. The stream ends if the connection to the node is lost.

        Args:
            node_id: The ID of the node to stream network instance pipelines from.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/nodes/{node_id}/network-pipelines", "")],
            StreamNetworkPipelinesRequest(node_id=node_id),
            StreamNetworkPipelineEvent,
        )

    def toggle_network_pipeline(
        self,
        *,
        node_id: str = "",
        optional_pipeline_id: str | None = None,
        optional_instance_pipeline_id: str | None = None,
    ) -> ToggleNetworkPipelineResponse:
        """Enable or disable a network instance pipeline on a node, which starts or
        stops the pipeline. Each call flips the current state. Fails with a not found
        error if no matching pipeline exists.

        Args:
            node_id: The ID of the node the pipeline runs on.
            optional_pipeline_id: The pipeline's `pipeline_id`.
            optional_instance_pipeline_id: The pipeline's `id`.
        """
        return self._transport.unary(
            [Route("POST", "/v1/nodes/{node_id}/network-pipelines/toggle", "*")],
            ToggleNetworkPipelineRequest(
                node_id=node_id,
                optional_pipeline_id=optional_pipeline_id,
                optional_instance_pipeline_id=optional_instance_pipeline_id,
            ),
            ToggleNetworkPipelineResponse,
        )

    def open_log_stream(
        self,
        *,
        node_id: str = "",
        network_instance_id: str = "",
        options: Options | None = None,
    ) -> ServerStream[NetworkInstanceLogStreamMessages]:
        """Stream the log messages of a network instance on a node. The requested number
        of past lines is sent first, then new messages as they are logged, until the
        connection to the node is lost.

        Args:
            node_id: The ID of the node the network instance runs on.
            network_instance_id: The ID of the network instance whose log to stream.
            options: Log stream options, such as how many past lines to send first.
        """
        return self._transport.server_stream(
            [
                Route("GET", "/v1/streams/nodes/{node_id}/network-instances/{network_instance_id}/logs", ""),
            ],
            NetworksOpenNetworkInstanceLogStreamRequest(
                node_id=node_id,
                network_instance_id=network_instance_id,
                options=options or Options(),
            ),
            NetworkInstanceLogStreamMessages,
        )


class NetworksClient:
    """A network is a virtual network that connects nodes as if they shared a local
    network, giving each node its own IP address. All traffic flows through a central
    relay node. When a network is created or changed, the pipelines each node needs
    are generated from the network's blueprints and deployed automatically. Use this
    service to create and change networks and to follow their changes and logs.
    Networks are stored on the connected node that has networks enabled, and calls
    wait until that node is connected.
    """

    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_network(
        self,
        *,
        id: str = "",
    ) -> GetNetworkResponse:
        """Get a single network.

        Args:
            id: The ID of the network to fetch.
        """
        return self._transport.unary(
            [Route("GET", "/v1/networks/{id}", "")],
            GetNetworkRequest(id=id),
            GetNetworkResponse,
        )

    def get_networks(self) -> GetNetworksResponse:
        """Get all networks."""
        return self._transport.unary(
            [Route("GET", "/v1/networks", "")],
            GetNetworksRequest(),
            GetNetworksResponse,
        )

    def create_network(
        self,
        *,
        network: Network | None = None,
    ) -> CreateNetworkResponse:
        """Create a network and return it. Every connected node is added to the network
        automatically and assigned the first free IP address in its subnet, so nodes
        given in the request are ignored.

        Args:
            network: The network to create. Required.
        """
        return self._transport.unary(
            [Route("POST", "/v1/networks", "network")],
            CreateNetworkRequest(network=network or Network()),
            CreateNetworkResponse,
        )

    def update_network(
        self,
        *,
        id: str = "",
        network: Network | None = None,
    ) -> UpdateNetworkResponse:
        """Replace the settings of an existing network and return the updated network.
        Nodes cannot be added or removed, and their IP address and role cannot be
        changed.

        Args:
            id: The ID of the network to update.
            network: The new settings of the network. Required. All fields replace
                the current values, except `nodes`: leave it empty to keep the nodes
                unchanged, or list every current node to edit their carriers and
                parameters.
        """
        return self._transport.unary(
            [Route("PUT", "/v1/networks/{id}", "network")],
            UpdateNetworkRequest(id=id, network=network or Network()),
            UpdateNetworkResponse,
        )

    def delete_network(
        self,
        *,
        id: str = "",
    ) -> DeleteNetworkResponse:
        """Delete a network.

        Args:
            id: The ID of the network to delete.
        """
        return self._transport.unary(
            [Route("DELETE", "/v1/networks/{id}", "")],
            DeleteNetworkRequest(id=id),
            DeleteNetworkResponse,
        )

    def stream_networks(self) -> ServerStream[StreamNetworksEvent]:
        """Stream changes to networks. Nothing is sent when the stream opens; an event
        is sent each time a network is created, updated or deleted. The stream ends
        if the connection to the networks node is lost.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/networks", "")],
            StreamNetworksRequest(),
            StreamNetworksEvent,
        )

    def open_log_stream(
        self,
        *,
        network_id: str = "",
        options: Options | None = None,
    ) -> ServerStream[NetworkLogStreamMessages]:
        """Stream the log messages of a network. The requested number of past lines is
        sent first, then new messages as they are logged, until the connection to the
        networks node is lost.

        Args:
            network_id: The ID of the network whose log to stream.
            options: Log stream options, such as how many past lines to send first.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/networks/{network_id}/logs", "")],
            NetworksOpenNetworkLogStreamRequest(
                network_id=network_id,
                options=options or Options(),
            ),
            NetworkLogStreamMessages,
        )


class PipelinesServiceClient:
    """A pipeline is the configuration a node runs to move traffic, connecting
    components such as UDP sockets, TUN interfaces and error correction encoders into
    a data flow. Each start of a pipeline creates a new run, with its own logs and
    telemetry. Use this service to create, change, start and stop pipelines on any
    node, and to follow their changes, logs and telemetry.
    """

    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_pipelines(
        self,
        *,
        node_id: str = "",
    ) -> GetPipelinesResponse:
        """Lists all pipelines on the node.

        Args:
            node_id: ID of the node to list the pipelines of.
        """
        return self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}/pipelines", "")],
            GetPipelinesRequest(node_id=node_id),
            GetPipelinesResponse,
        )

    def get_pipeline_by_id(
        self,
        *,
        node_id: str = "",
        id: str = "",
    ) -> GetPipelineByIdResponse:
        """Get one pipeline. Fails with a not found error if it does not exist.

        Args:
            node_id: ID of the node that hosts the pipeline.
            id: ID of the pipeline.
        """
        return self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}/pipelines/{id}", "")],
            GetPipelineByIdRequest(node_id=node_id, id=id),
            GetPipelineByIdResponse,
        )

    def get_pipeline_by_name(
        self,
        *,
        node_id: str = "",
        name: str = "",
    ) -> GetPipelineByNameResponse:
        """Get one pipeline by name. Fails with a not found error if no pipeline, or
        more than one, has that name.

        Args:
            node_id: ID of the node that hosts the pipeline.
            name: Exact name of the pipeline. Example: `UDP tunnel`
        """
        return self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}/pipelines-by-name/{name}", "")],
            GetPipelineByNameRequest(node_id=node_id, name=name),
            GetPipelineByNameResponse,
        )

    def get_pipeline_by_run_id(
        self,
        *,
        node_id: str = "",
        id: str = "",
    ) -> GetPipelineByRunIdResponse:
        """Get the pipeline that a run belongs to. An unknown run fails with a timeout
        error.

        Args:
            node_id: ID of the node that hosts the pipeline.
            id: ID of the run.
        """
        return self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}/pipeline-runs/{id}", "")],
            GetPipelineByRunIdRequest(node_id=node_id, id=id),
            GetPipelineByRunIdResponse,
        )

    def create_pipeline(
        self,
        *,
        node_id: str = "",
        name: str = "",
        json_config: str = "",
        restart_policy: RestartPolicy | None = None,
        startup_policy: StartupPolicy | None = None,
        default_logging_level: Level | None = None,
        node_reference_id: str | None = None,
        instructions_timeout: int | None = None,
        cpu_pin: int | None = None,
        performance_mode: bool | None = None,
    ) -> CreatePipelineResponse:
        """Create a pipeline from a JSON configuration and return it. The pipeline is
        not started. Fails with an invalid argument error if the configuration is
        invalid or the CPU pin is not a thread of the node.

        Args:
            node_id: ID of the node to create the pipeline on.
            name: Name of the pipeline. Example: `UDP tunnel`
            json_config: The pipeline configuration as a JSON string.
            restart_policy: The restart policy of the pipeline. Leave unset to never
                restart.
            startup_policy: The startup policy of the pipeline. Leave unset to start
                it manually only.
            default_logging_level: The default logging level.
            node_reference_id: ID of the related node.
            instructions_timeout: The timeout in seconds. Must be greater than 0.
                Example: `30`
            cpu_pin: Zero indexed CPU thread number. Must be lower than the node's
                thread count.
            performance_mode: True to run the pinned thread in performance mode.
        """
        return self._transport.unary(
            [Route("POST", "/v1/nodes/{node_id}/pipelines", "*")],
            CreatePipelineRequest(
                node_id=node_id,
                name=name,
                json_config=json_config,
                restart_policy=restart_policy or RestartPolicy(),
                startup_policy=startup_policy or StartupPolicy(),
                default_logging_level=default_logging_level,
                node_reference_id=node_reference_id,
                instructions_timeout=instructions_timeout,
                cpu_pin=cpu_pin,
                performance_mode=performance_mode,
            ),
            CreatePipelineResponse,
        )

    def update_pipeline(
        self,
        *,
        node_id: str = "",
        id: str = "",
        name: str = "",
        json_config: str = "",
        restart_policy: RestartPolicy | None = None,
        startup_policy: StartupPolicy | None = None,
        default_logging_level: Level = Level.STATE,
        instructions_timeout: int = 0,
        cpu_pin: int | None = None,
        performance_mode: bool | None = None,
        node_reference_id: str | None = None,
        force_restart: bool = False,
    ) -> UpdatePipelineResponse:
        """Replace the settings of a pipeline and return the updated pipeline. If the
        pipeline is running and its configuration changed, the new configuration is
        applied to the current run. If that is not possible, the call fails because
        the pipeline is running, unless a restart is forced.

        Args:
            node_id: ID of the node that hosts the pipeline.
            id: ID of the pipeline to update.
            name: New name of the pipeline. Example: `UDP tunnel`
            json_config: New pipeline configuration as a JSON string.
            restart_policy: New restart policy of the pipeline. Unset means never
                restart.
            startup_policy: New startup policy of the pipeline. Unset means start
                manually only.
            default_logging_level: New default logging level of the pipeline. Unset
                means `STATE`, not the `INFO` default used on create.
            instructions_timeout: New time in seconds before a pipeline instruction
                is considered timed out. Must be greater than 0. Example: `30`
            cpu_pin: Zero indexed CPU thread number. Must be lower than the node's
                thread count.
            performance_mode: True to run the pinned thread in performance mode.
            node_reference_id: ID of the related node.
            force_restart: If true and the pipeline is running, the pipeline is
                restarted when the new configuration cannot be applied to the current
                run. The call then returns once the new run is running.
        """
        return self._transport.unary(
            [Route("PUT", "/v1/nodes/{node_id}/pipelines/{id}", "*")],
            UpdatePipelineRequest(
                node_id=node_id,
                id=id,
                name=name,
                json_config=json_config,
                restart_policy=restart_policy or RestartPolicy(),
                startup_policy=startup_policy or StartupPolicy(),
                default_logging_level=default_logging_level,
                instructions_timeout=instructions_timeout,
                cpu_pin=cpu_pin,
                performance_mode=performance_mode,
                node_reference_id=node_reference_id,
                force_restart=force_restart,
            ),
            UpdatePipelineResponse,
        )

    def delete_pipeline(
        self,
        *,
        node_id: str = "",
        id: str = "",
    ) -> DeletePipelineResponse:
        """Delete a pipeline. Fails with a not found error if it does not exist.

        Args:
            node_id: ID of the node that hosts the pipeline.
            id: ID of the pipeline to delete.
        """
        return self._transport.unary(
            [Route("DELETE", "/v1/nodes/{node_id}/pipelines/{id}", "")],
            DeletePipelineRequest(node_id=node_id, id=id),
            DeletePipelineResponse,
        )

    def start_pipeline(
        self,
        *,
        node_id: str = "",
        id: str | None = None,
        name: str | None = None,
    ) -> StartPipelineResponse:
        """Start a pipeline and return its new run once it is running. Fails if the
        pipeline is unknown, already started, or does not reach the running state
        within 10 seconds.

        Args:
            node_id: ID of the node that hosts the pipeline.
            id: ID of the pipeline.
            name: Exact name of the pipeline. Fails if more than one pipeline has
                this name. Example: `UDP tunnel`
        """
        return self._transport.unary(
            [
                Route("POST", "/v1/nodes/{node_id}/pipelines/{id}/start", ""),
                Route("POST", "/v1/nodes/{node_id}/pipelines-by-name/{name}/start", ""),
            ],
            StartPipelineRequest(node_id=node_id, id=id, name=name),
            StartPipelineResponse,
        )

    def stop_pipeline(
        self,
        *,
        node_id: str = "",
        id: str | None = None,
        name: str | None = None,
        run_id: str | None = None,
    ) -> StopPipelineResponse:
        """Stop a pipeline, found by its ID, its name or its current run. Returns once
        the stop is requested, without waiting for the run to end. Fails if the
        pipeline is unknown or already stopped.

        Args:
            node_id: ID of the node that hosts the pipeline.
            id: ID of the pipeline.
            name: Exact name of the pipeline. Fails if more than one pipeline has
                this name. Example: `UDP tunnel`
            run_id: ID of the pipeline's current run.
        """
        return self._transport.unary(
            [
                Route("POST", "/v1/nodes/{node_id}/pipelines/{id}/stop", ""),
                Route("POST", "/v1/nodes/{node_id}/pipelines-by-name/{name}/stop", ""),
                Route("POST", "/v1/nodes/{node_id}/pipeline-runs/{run_id}/stop", ""),
            ],
            StopPipelineRequest(node_id=node_id, id=id, name=name, run_id=run_id),
            StopPipelineResponse,
        )

    def stream_pipelines(
        self,
        *,
        node_id: str = "",
    ) -> ServerStream[StreamPipelinesEvent]:
        """Stream changes to the pipelines of a node. Nothing is sent when the stream
        opens, so get the pipelines first for the current list. An event is sent each
        time a pipeline is created, updated or deleted, and when a pipeline starts or
        stops.

        Args:
            node_id: ID of the node to stream pipeline changes from.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/nodes/{node_id}/pipelines", "")],
            StreamPipelinesRequest(node_id=node_id),
            StreamPipelinesEvent,
        )

    def open_log_stream(
        self,
        *,
        node_id: str = "",
        run_id: str = "",
        options: Options | None = None,
    ) -> ServerStream[LogStreamMessages]:
        """Stream the log messages of a pipeline run. The requested number of past lines
        is sent first, then new messages as they are logged.

        Args:
            node_id: ID of the node that hosts the run.
            run_id: ID of the run to stream logs from.
            options: Stream options, such as how many past lines to send first.
                Leave unset to receive only new messages.
        """
        return self._transport.server_stream(
            [
                Route("GET", "/v1/streams/nodes/{node_id}/pipeline-runs/{run_id}/logs", ""),
            ],
            PipelineOpenLogStreamRequest(
                node_id=node_id,
                run_id=run_id,
                options=options or Options(),
            ),
            LogStreamMessages,
        )

    def open_telemetry_stream(
        self,
        *,
        node_id: str = "",
        run_id: str = "",
    ) -> ServerStream[TelemetrySample]:
        """Streams telemetry samples (metrics and KPI values) of a pipeline run at
        regular intervals while the run is active. The stream ends with an error when
        the run stops, when the run is unknown, or when the node disconnects.

        Args:
            node_id: ID of the node that hosts the run.
            run_id: ID of the run to stream telemetry from.
        """
        return self._transport.server_stream(
            [
                Route("GET", "/v1/streams/nodes/{node_id}/pipeline-runs/{run_id}/telemetry", ""),
            ],
            OpenTelemetryStreamRequest(node_id=node_id, run_id=run_id),
            TelemetrySample,
        )


class ResourcesServiceClient:
    """Live system information of a node: resource metrics such as CPU, memory, storage
    and network interface usage, and the network flows crossing its interfaces. Use
    this service to monitor the health and traffic of any node.
    """

    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def open_metrics_stream(
        self,
        *,
        node_id: str = "",
    ) -> ServerStream[MetricsSample]:
        """Stream the resource metrics of a node, such as CPU, memory, disk and network
        interface usage. A sample of the current metrics is sent when the stream
        opens. The stream stays open until the client closes it, and ends with an
        error if the node loses its connection.

        Args:
            node_id: ID of the node to read metrics from.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/nodes/{node_id}/metrics", "")],
            OpenMetricsStreamRequest(node_id=node_id),
            MetricsSample,
        )

    def open_flows_stream(
        self,
        *,
        node_id: str = "",
    ) -> ServerStream[FlowsSample]:
        """Stream a snapshot of the network flows crossing the interfaces of a node,
        about once a second, starting right away. The node only captures packets
        while someone watches its flows, so the first samples may be empty or
        incomplete.

        Args:
            node_id: ID of the node to read flows from.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/nodes/{node_id}/flows", "")],
            OpenFlowsStreamRequest(node_id=node_id),
            FlowsSample,
        )


class AsyncBlueprintsClient:
    """A blueprint is a template that generates the pipeline configuration a node runs
    in a network. It uses [Go template syntax](https://pkg.go.dev/text/template), and
    placeholders such as the node's IP address and carriers are filled in for each
    node. Every network uses three blueprints: one for the relay node, one the relay
    runs for every client, and one for every client node. The built-in blueprints are
    read-only; create your own to change how networks carry traffic. Blueprints are
    stored on the connected node that has networks enabled, and calls wait until that
    node is connected.
    """

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_blueprint(
        self,
        *,
        id: str = "",
    ) -> GetBlueprintResponse:
        """Get a single blueprint.

        Args:
            id: The ID of the blueprint to fetch.
        """
        return await self._transport.unary(
            [Route("GET", "/v1/blueprints/{id}", "")],
            GetBlueprintRequest(id=id),
            GetBlueprintResponse,
        )

    async def get_blueprints(self) -> GetBlueprintsResponse:
        """Get all blueprints, including the built-in read-only ones."""
        return await self._transport.unary(
            [Route("GET", "/v1/blueprints", "")],
            GetBlueprintsRequest(),
            GetBlueprintsResponse,
        )

    async def create_blueprint(
        self,
        *,
        blueprint: BlueprintWrite | None = None,
    ) -> CreateBlueprintResponse:
        """Create a blueprint and return it.

        Args:
            blueprint: The blueprint to create. Required.
        """
        return await self._transport.unary(
            [Route("POST", "/v1/blueprints", "blueprint")],
            CreateBlueprintRequest(blueprint=blueprint or BlueprintWrite()),
            CreateBlueprintResponse,
        )

    async def update_blueprint(
        self,
        *,
        id: str = "",
        blueprint: BlueprintWrite | None = None,
    ) -> UpdateBlueprintResponse:
        """Replace a blueprint and return the updated blueprint. Networks using the
        blueprint have their pipelines regenerated. Fails with a permission error for
        read-only blueprints.

        Args:
            id: The ID of the blueprint to update.
            blueprint: The new name and template. Required.
        """
        return await self._transport.unary(
            [Route("PUT", "/v1/blueprints/{id}", "blueprint")],
            UpdateBlueprintRequest(id=id, blueprint=blueprint or BlueprintWrite()),
            UpdateBlueprintResponse,
        )

    async def delete_blueprint(
        self,
        *,
        id: str = "",
    ) -> DeleteBlueprintResponse:
        """Delete a blueprint. Fails with a permission error for read-only blueprints.

        Args:
            id: The ID of the blueprint to delete.
        """
        return await self._transport.unary(
            [Route("DELETE", "/v1/blueprints/{id}", "")],
            DeleteBlueprintRequest(id=id),
            DeleteBlueprintResponse,
        )


class AsyncConfigServiceClient:
    """Settings stored in the configuration of a node. Use this service to read and
    change them on any node, such as the carriers a node uses by default when it
    joins a network.
    """

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_default_network_carriers(
        self,
        *,
        node_id: str = "",
    ) -> GetDefaultNetworkCarriersResponse:
        """Get the default network carriers of a node. These are the carriers the node
        receives every time it joins a new network. Returns an empty list when none
        are configured.

        Args:
            node_id: Id of the node to read the default network carriers from.
        """
        return await self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}/default-network-carriers", "")],
            GetDefaultNetworkCarriersRequest(node_id=node_id),
            GetDefaultNetworkCarriersResponse,
        )

    async def set_default_network_carriers(
        self,
        *,
        node_id: str = "",
        carriers: DefaultNetworkCarriers | None = None,
    ) -> SetDefaultNetworkCarriersResponse:
        """Replace the default network carriers of a node. The new carriers apply to
        networks the node joins afterwards.

        Args:
            node_id: Id of the node to set the default network carriers on.
            carriers: The new default network carriers, replacing the current ones.
                Leave unset to remove all default carriers.
        """
        return await self._transport.unary(
            [Route("PUT", "/v1/nodes/{node_id}/default-network-carriers", "carriers")],
            SetDefaultNetworkCarriersRequest(node_id=node_id, carriers=carriers),
            SetDefaultNetworkCarriersResponse,
        )


class AsyncHubClientServiceClient:
    """The hub client is the part of every node that connects it to a hub server, the
    control plane that lets connected nodes find and manage each other. Use this
    service to sign the node hosting the API in to a hub server, disconnect it,
    follow its connection state, and read or change the details of nodes.
    """

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_local_node_id(self) -> GetLocalNodeIdResponse:
        """Get the ID of the node hosting the API, and whether it is authenticated with
        a hub server.
        """
        return await self._transport.unary(
            [Route("GET", "/v1/hub-client/local-node-id", "")],
            GetLocalNodeIdRequest(),
            GetLocalNodeIdResponse,
        )

    async def get_node(
        self,
        *,
        node_id: str = "",
    ) -> GetNodeResponse:
        """Get the details of a node. Fails with Unavailable when the node cannot be
        reached.

        Args:
            node_id: Id of the node to get information about, for example the id
                returned by getLocalNodeId.
        """
        return await self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}", "")],
            GetNodeRequest(node_id=node_id),
            GetNodeResponse,
        )

    async def set_node(
        self,
        *,
        node_id: str = "",
        name: str = "",
        metadata: NodeMetadata | None = None,
    ) -> SetNodeResponse:
        """Change the details of a node, replacing the current values. Fails with
        PermissionDenied when the node's configuration comes from a config file.

        Args:
            node_id: Id of the node to change.
            name: New name of the node. Example: `edge-node-1`
            metadata: New metadata of the node. Replaces all existing metadata, so
                leaving it empty removes the metadata.
        """
        return await self._transport.unary(
            [Route("PUT", "/v1/nodes/{node_id}", "*")],
            SetNodeRequest(
                node_id=node_id,
                name=name,
                metadata=metadata or NodeMetadata(),
            ),
            SetNodeResponse,
        )

    async def authenticate_by_request(
        self,
        *,
        hub_server_address: str = "",
    ) -> AuthenticateByRequestResponse:
        """Ask a hub server to authenticate the node hosting the API, and wait for the
        hub server to accept or reject the request. On success the node stays
        authenticated, also after a restart. Fails with AlreadyExists if the node is
        already authenticated, Unauthenticated if the request was rejected,
        DeadlineExceeded if the hub server did not answer in time, Unavailable if the
        hub server could not be reached, and NotFound if the hub server does not
        accept authentication by request.

        Args:
            hub_server_address: HTTP or HTTPS address of the hub server. Example:
                `http://127.0.0.1:8769`
        """
        return await self._transport.unary(
            [Route("POST", "/v1/hub-client/authenticate-by-request", "*")],
            AuthenticateByRequestRequest(hub_server_address=hub_server_address),
            AuthenticateByRequestResponse,
        )

    async def disconnect(self) -> DisconnectResponse:
        """Disconnect the node hosting the API from its hub server. The node always
        leaves, even if the hub server could not remove it from its list of nodes.
        """
        return await self._transport.unary(
            [Route("POST", "/v1/hub-client/disconnect", "*")],
            DisconnectRequest(),
            DisconnectResponse,
        )

    def stream_connection_state(
        self,
    ) -> AsyncServerStream[StreamConnectionStateResponse]:
        """Stream the connection state between the node hosting the API and its hub
        server. The current state is sent first, then a new message every time the
        state changes. The stream stays open until the caller closes it.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/hub-client/connection-state", "")],
            StreamConnectionStateRequest(),
            StreamConnectionStateResponse,
        )


class AsyncHubServerServiceClient:
    """A hub server is the control plane of a NanoPing setup: nodes authenticate with
    it, and every node on the same hub can find and manage the others. Use this
    service to list the nodes on the hub, follow them as they come and go, remove
    nodes, and approve or reject nodes that ask to join. The node hosting the API
    must host the hub server or be authenticated with one, otherwise calls fail with
    FailedPrecondition.
    """

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_nodes(
        self,
        *,
        metadata_filters: Mapping[str, NodeMetadataItem] | None = None,
        service_filters: Sequence[NodeService] = (),
    ) -> GetNodesResponse:
        """Get the nodes authenticated with the hub server, optionally filtered.

        Args:
            metadata_filters: Metadata filters keyed by metadata key. A node is
                included only if it has every key with an equal value of the same type.
                Leave empty to not filter by metadata.
            service_filters: Service filters. A node is included only if it offers
                every listed service. Leave empty to not filter by service.
        """
        return await self._transport.unary(
            [Route("GET", "/v1/nodes", ""), Route("POST", "/v1/nodes/search", "*")],
            GetNodesRequest(
                metadata_filters=dict(metadata_filters or {}),
                service_filters=list(service_filters),
            ),
            GetNodesResponse,
        )

    async def remove_node(
        self,
        *,
        node_id: str = "",
    ) -> RemoveNodeResponse:
        """Remove a node from the hub server. This disconnects the node from the hub
        server and removes it from its networks.

        Args:
            node_id: Id of the node to remove.
        """
        return await self._transport.unary(
            [Route("DELETE", "/v1/nodes/{node_id}", "")],
            RemoveNodeRequest(node_id=node_id),
            RemoveNodeResponse,
        )

    def stream_nodes(
        self,
        *,
        metadata_filters: Mapping[str, NodeMetadataItem] | None = None,
        service_filters: Sequence[NodeService] = (),
    ) -> AsyncServerStream[StreamNodesResponse]:
        """Stream the nodes authenticated with the hub server. The matching nodes are
        sent first, followed by an update every time a node is authenticated,
        deauthenticated, connects, disconnects or changes its details. Updates are
        not filtered. The stream stays open until the caller closes it.

        Args:
            metadata_filters: Metadata filters keyed by metadata key. A node is
                included only if it has every key with an equal value of the same type.
                Leave empty to not filter by metadata.
            service_filters: Service filters. A node is included only if it offers
                every listed service. Leave empty to not filter by service.
        """
        return self._transport.server_stream(
            [
                Route("GET", "/v1/streams/nodes", ""),
                Route("POST", "/v1/streams/nodes", "*"),
            ],
            GetNodesRequest(
                metadata_filters=dict(metadata_filters or {}),
                service_filters=list(service_filters),
            ),
            StreamNodesResponse,
        )

    def authentication_by_requests(
        self,
    ) -> AsyncBidiStream[AuthenticationByRequestAnswer, AuthenticationByRequestRequest]:
        """Receive the authentication requests sent to the hub server on the node
        hosting the API, and accept or reject each one. Nothing is sent when the
        stream opens. A request is sent each time a node asks to authenticate, and
        the caller answers it by sending an answer for that request.
        """
        return self._transport.bidi_stream(
            Route("POST", "/v1/streams/hub-server/authentication-requests", "*"),
            AuthenticationByRequestRequest,
        )


class AsyncLoggingServiceClient:
    """Every node keeps logs: its application log, and a log for each pipeline run,
    network and network instance. Use this service to follow a log live or to
    download a complete log file, from any node.
    """

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    def open_log_stream(
        self,
        *,
        node_id: str = "",
        options: Options | None = None,
        app_log_stream_request: OpenAppLogStreamRequest | None = None,
        pipeline_run_log_stream_request: OpenPipelineRunLogStreamRequest | None = None,
        network_log_stream_request: LoggingOpenNetworkLogStreamRequest | None = None,
        network_instance_log_stream_request: LoggingOpenNetworkInstanceLogStreamRequest | None = None,
    ) -> AsyncServerStream[Messages]:
        """Stream the log messages of one log on a node. The requested number of past
        entries is sent first, then new entries as they are written. Fails with an
        invalid argument error when the node is invalid or no log is chosen, and ends
        with an error when the log cannot be read or the node loses its connection.

        Args:
            node_id: ID of the node whose log to stream.
            options: Stream options. When unset, only new entries are sent.
            app_log_stream_request: Stream the node's application log.
            pipeline_run_log_stream_request: Stream the log of a pipeline run.
            network_log_stream_request: Stream the log of a network.
            network_instance_log_stream_request: Stream the log of a network
                instance.
        """
        return self._transport.server_stream(
            [Route("POST", "/v1/streams/nodes/{node_id}/logs", "*")],
            LoggingOpenLogStreamRequest(
                node_id=node_id,
                options=options or Options(),
                app_log_stream_request=app_log_stream_request,
                pipeline_run_log_stream_request=pipeline_run_log_stream_request,
                network_log_stream_request=network_log_stream_request,
                network_instance_log_stream_request=network_instance_log_stream_request,
            ),
            Messages,
        )

    async def download_log_file(
        self,
        *,
        node_id: str = "",
        app_log_file_request: DownloadAppLogFileRequest | None = None,
        pipeline_run_log_file_request: DownloadPipelineRunLogFileRequest | None = None,
        network_log_file_request: DownloadNetworkLogFileRequest | None = None,
        network_instance_log_file_request: DownloadNetworkInstanceLogFileRequest | None = None,
    ) -> str:
        """Download one complete log file from a node as a series of chunks. Join the
        chunks in order to get the file. The stream ends when the whole file has been
        sent, or after an error chunk when the file could not be read.

        Returns the whole file as text.

        Args:
            node_id: ID of the node that holds the log file.
            app_log_file_request: Download the node's application log.
            pipeline_run_log_file_request: Download the log of a pipeline run.
            network_log_file_request: Download the log of a network.
            network_instance_log_file_request: Download the log of a network
                instance.
        """
        return await self._transport.text(
            [Route("GET", "/v1/nodes/{node_id}/log-file", "")],
            DownloadLogFileRequest(
                node_id=node_id,
                app_log_file_request=app_log_file_request,
                pipeline_run_log_file_request=pipeline_run_log_file_request,
                network_log_file_request=network_log_file_request,
                network_instance_log_file_request=network_instance_log_file_request,
            ),
        )


class AsyncNetworkInstancesClient:
    """A network instance is a network's presence on one node: the pipelines generated
    for that node from the network's blueprints. Instances are created, updated and
    removed automatically when their network changes, so they cannot be managed
    directly. Use this service to see which networks a node takes part in, follow its
    network pipelines, turn them on or off, and read their logs. The node needs
    pipelines enabled.
    """

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_network_instances(
        self,
        *,
        node_id: str = "",
    ) -> GetNetworkInstancesResponse:
        """Get all network instances on a node, each with its pipelines.

        Args:
            node_id: The ID of the node to fetch network instances from.
        """
        return await self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}/network-instances", "")],
            GetNetworkInstancesRequest(node_id=node_id),
            GetNetworkInstancesResponse,
        )

    def stream_network_instances(
        self,
        *,
        node_id: str = "",
    ) -> AsyncServerStream[StreamNetworkInstanceEvent]:
        """Stream changes to the network instances on a node. Nothing is sent when the
        stream opens; an event is sent each time an instance is created, updated or
        deleted, and an update is also sent when one of its pipelines changes. The
        stream ends if the connection to the node is lost.

        Args:
            node_id: The ID of the node to stream network instances from.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/nodes/{node_id}/network-instances", "")],
            StreamNetworkInstancesRequest(node_id=node_id),
            StreamNetworkInstanceEvent,
        )

    async def get_network_pipelines(
        self,
        *,
        node_id: str = "",
        optional_network_id: str | None = None,
        optional_instance_id: str | None = None,
        optional_blueprint_id: str | None = None,
    ) -> GetNetworkPipelinesResponse:
        """Get the network instance pipelines on a node, optionally filtered. A pipeline
        must match every filter that is set.

        Args:
            node_id: The ID of the node to fetch network instance pipelines from.
            optional_network_id: Only return pipelines belonging to this network ID.
            optional_instance_id: Only return pipelines belonging to this network
                instance ID.
            optional_blueprint_id: Only return pipelines generated from this
                blueprint ID.
        """
        return await self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}/network-pipelines", "")],
            GetNetworkPipelinesRequest(
                node_id=node_id,
                optional_network_id=optional_network_id,
                optional_instance_id=optional_instance_id,
                optional_blueprint_id=optional_blueprint_id,
            ),
            GetNetworkPipelinesResponse,
        )

    def stream_network_pipelines(
        self,
        *,
        node_id: str = "",
    ) -> AsyncServerStream[StreamNetworkPipelineEvent]:
        """Stream changes to the network instance pipelines on a node. Nothing is sent
        when the stream opens; an event is sent each time a pipeline is created,
        updated or deleted. The stream ends if the connection to the node is lost.

        Args:
            node_id: The ID of the node to stream network instance pipelines from.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/nodes/{node_id}/network-pipelines", "")],
            StreamNetworkPipelinesRequest(node_id=node_id),
            StreamNetworkPipelineEvent,
        )

    async def toggle_network_pipeline(
        self,
        *,
        node_id: str = "",
        optional_pipeline_id: str | None = None,
        optional_instance_pipeline_id: str | None = None,
    ) -> ToggleNetworkPipelineResponse:
        """Enable or disable a network instance pipeline on a node, which starts or
        stops the pipeline. Each call flips the current state. Fails with a not found
        error if no matching pipeline exists.

        Args:
            node_id: The ID of the node the pipeline runs on.
            optional_pipeline_id: The pipeline's `pipeline_id`.
            optional_instance_pipeline_id: The pipeline's `id`.
        """
        return await self._transport.unary(
            [Route("POST", "/v1/nodes/{node_id}/network-pipelines/toggle", "*")],
            ToggleNetworkPipelineRequest(
                node_id=node_id,
                optional_pipeline_id=optional_pipeline_id,
                optional_instance_pipeline_id=optional_instance_pipeline_id,
            ),
            ToggleNetworkPipelineResponse,
        )

    def open_log_stream(
        self,
        *,
        node_id: str = "",
        network_instance_id: str = "",
        options: Options | None = None,
    ) -> AsyncServerStream[NetworkInstanceLogStreamMessages]:
        """Stream the log messages of a network instance on a node. The requested number
        of past lines is sent first, then new messages as they are logged, until the
        connection to the node is lost.

        Args:
            node_id: The ID of the node the network instance runs on.
            network_instance_id: The ID of the network instance whose log to stream.
            options: Log stream options, such as how many past lines to send first.
        """
        return self._transport.server_stream(
            [
                Route("GET", "/v1/streams/nodes/{node_id}/network-instances/{network_instance_id}/logs", ""),
            ],
            NetworksOpenNetworkInstanceLogStreamRequest(
                node_id=node_id,
                network_instance_id=network_instance_id,
                options=options or Options(),
            ),
            NetworkInstanceLogStreamMessages,
        )


class AsyncNetworksClient:
    """A network is a virtual network that connects nodes as if they shared a local
    network, giving each node its own IP address. All traffic flows through a central
    relay node. When a network is created or changed, the pipelines each node needs
    are generated from the network's blueprints and deployed automatically. Use this
    service to create and change networks and to follow their changes and logs.
    Networks are stored on the connected node that has networks enabled, and calls
    wait until that node is connected.
    """

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_network(
        self,
        *,
        id: str = "",
    ) -> GetNetworkResponse:
        """Get a single network.

        Args:
            id: The ID of the network to fetch.
        """
        return await self._transport.unary(
            [Route("GET", "/v1/networks/{id}", "")],
            GetNetworkRequest(id=id),
            GetNetworkResponse,
        )

    async def get_networks(self) -> GetNetworksResponse:
        """Get all networks."""
        return await self._transport.unary(
            [Route("GET", "/v1/networks", "")],
            GetNetworksRequest(),
            GetNetworksResponse,
        )

    async def create_network(
        self,
        *,
        network: Network | None = None,
    ) -> CreateNetworkResponse:
        """Create a network and return it. Every connected node is added to the network
        automatically and assigned the first free IP address in its subnet, so nodes
        given in the request are ignored.

        Args:
            network: The network to create. Required.
        """
        return await self._transport.unary(
            [Route("POST", "/v1/networks", "network")],
            CreateNetworkRequest(network=network or Network()),
            CreateNetworkResponse,
        )

    async def update_network(
        self,
        *,
        id: str = "",
        network: Network | None = None,
    ) -> UpdateNetworkResponse:
        """Replace the settings of an existing network and return the updated network.
        Nodes cannot be added or removed, and their IP address and role cannot be
        changed.

        Args:
            id: The ID of the network to update.
            network: The new settings of the network. Required. All fields replace
                the current values, except `nodes`: leave it empty to keep the nodes
                unchanged, or list every current node to edit their carriers and
                parameters.
        """
        return await self._transport.unary(
            [Route("PUT", "/v1/networks/{id}", "network")],
            UpdateNetworkRequest(id=id, network=network or Network()),
            UpdateNetworkResponse,
        )

    async def delete_network(
        self,
        *,
        id: str = "",
    ) -> DeleteNetworkResponse:
        """Delete a network.

        Args:
            id: The ID of the network to delete.
        """
        return await self._transport.unary(
            [Route("DELETE", "/v1/networks/{id}", "")],
            DeleteNetworkRequest(id=id),
            DeleteNetworkResponse,
        )

    def stream_networks(self) -> AsyncServerStream[StreamNetworksEvent]:
        """Stream changes to networks. Nothing is sent when the stream opens; an event
        is sent each time a network is created, updated or deleted. The stream ends
        if the connection to the networks node is lost.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/networks", "")],
            StreamNetworksRequest(),
            StreamNetworksEvent,
        )

    def open_log_stream(
        self,
        *,
        network_id: str = "",
        options: Options | None = None,
    ) -> AsyncServerStream[NetworkLogStreamMessages]:
        """Stream the log messages of a network. The requested number of past lines is
        sent first, then new messages as they are logged, until the connection to the
        networks node is lost.

        Args:
            network_id: The ID of the network whose log to stream.
            options: Log stream options, such as how many past lines to send first.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/networks/{network_id}/logs", "")],
            NetworksOpenNetworkLogStreamRequest(
                network_id=network_id,
                options=options or Options(),
            ),
            NetworkLogStreamMessages,
        )


class AsyncPipelinesServiceClient:
    """A pipeline is the configuration a node runs to move traffic, connecting
    components such as UDP sockets, TUN interfaces and error correction encoders into
    a data flow. Each start of a pipeline creates a new run, with its own logs and
    telemetry. Use this service to create, change, start and stop pipelines on any
    node, and to follow their changes, logs and telemetry.
    """

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_pipelines(
        self,
        *,
        node_id: str = "",
    ) -> GetPipelinesResponse:
        """Lists all pipelines on the node.

        Args:
            node_id: ID of the node to list the pipelines of.
        """
        return await self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}/pipelines", "")],
            GetPipelinesRequest(node_id=node_id),
            GetPipelinesResponse,
        )

    async def get_pipeline_by_id(
        self,
        *,
        node_id: str = "",
        id: str = "",
    ) -> GetPipelineByIdResponse:
        """Get one pipeline. Fails with a not found error if it does not exist.

        Args:
            node_id: ID of the node that hosts the pipeline.
            id: ID of the pipeline.
        """
        return await self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}/pipelines/{id}", "")],
            GetPipelineByIdRequest(node_id=node_id, id=id),
            GetPipelineByIdResponse,
        )

    async def get_pipeline_by_name(
        self,
        *,
        node_id: str = "",
        name: str = "",
    ) -> GetPipelineByNameResponse:
        """Get one pipeline by name. Fails with a not found error if no pipeline, or
        more than one, has that name.

        Args:
            node_id: ID of the node that hosts the pipeline.
            name: Exact name of the pipeline. Example: `UDP tunnel`
        """
        return await self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}/pipelines-by-name/{name}", "")],
            GetPipelineByNameRequest(node_id=node_id, name=name),
            GetPipelineByNameResponse,
        )

    async def get_pipeline_by_run_id(
        self,
        *,
        node_id: str = "",
        id: str = "",
    ) -> GetPipelineByRunIdResponse:
        """Get the pipeline that a run belongs to. An unknown run fails with a timeout
        error.

        Args:
            node_id: ID of the node that hosts the pipeline.
            id: ID of the run.
        """
        return await self._transport.unary(
            [Route("GET", "/v1/nodes/{node_id}/pipeline-runs/{id}", "")],
            GetPipelineByRunIdRequest(node_id=node_id, id=id),
            GetPipelineByRunIdResponse,
        )

    async def create_pipeline(
        self,
        *,
        node_id: str = "",
        name: str = "",
        json_config: str = "",
        restart_policy: RestartPolicy | None = None,
        startup_policy: StartupPolicy | None = None,
        default_logging_level: Level | None = None,
        node_reference_id: str | None = None,
        instructions_timeout: int | None = None,
        cpu_pin: int | None = None,
        performance_mode: bool | None = None,
    ) -> CreatePipelineResponse:
        """Create a pipeline from a JSON configuration and return it. The pipeline is
        not started. Fails with an invalid argument error if the configuration is
        invalid or the CPU pin is not a thread of the node.

        Args:
            node_id: ID of the node to create the pipeline on.
            name: Name of the pipeline. Example: `UDP tunnel`
            json_config: The pipeline configuration as a JSON string.
            restart_policy: The restart policy of the pipeline. Leave unset to never
                restart.
            startup_policy: The startup policy of the pipeline. Leave unset to start
                it manually only.
            default_logging_level: The default logging level.
            node_reference_id: ID of the related node.
            instructions_timeout: The timeout in seconds. Must be greater than 0.
                Example: `30`
            cpu_pin: Zero indexed CPU thread number. Must be lower than the node's
                thread count.
            performance_mode: True to run the pinned thread in performance mode.
        """
        return await self._transport.unary(
            [Route("POST", "/v1/nodes/{node_id}/pipelines", "*")],
            CreatePipelineRequest(
                node_id=node_id,
                name=name,
                json_config=json_config,
                restart_policy=restart_policy or RestartPolicy(),
                startup_policy=startup_policy or StartupPolicy(),
                default_logging_level=default_logging_level,
                node_reference_id=node_reference_id,
                instructions_timeout=instructions_timeout,
                cpu_pin=cpu_pin,
                performance_mode=performance_mode,
            ),
            CreatePipelineResponse,
        )

    async def update_pipeline(
        self,
        *,
        node_id: str = "",
        id: str = "",
        name: str = "",
        json_config: str = "",
        restart_policy: RestartPolicy | None = None,
        startup_policy: StartupPolicy | None = None,
        default_logging_level: Level = Level.STATE,
        instructions_timeout: int = 0,
        cpu_pin: int | None = None,
        performance_mode: bool | None = None,
        node_reference_id: str | None = None,
        force_restart: bool = False,
    ) -> UpdatePipelineResponse:
        """Replace the settings of a pipeline and return the updated pipeline. If the
        pipeline is running and its configuration changed, the new configuration is
        applied to the current run. If that is not possible, the call fails because
        the pipeline is running, unless a restart is forced.

        Args:
            node_id: ID of the node that hosts the pipeline.
            id: ID of the pipeline to update.
            name: New name of the pipeline. Example: `UDP tunnel`
            json_config: New pipeline configuration as a JSON string.
            restart_policy: New restart policy of the pipeline. Unset means never
                restart.
            startup_policy: New startup policy of the pipeline. Unset means start
                manually only.
            default_logging_level: New default logging level of the pipeline. Unset
                means `STATE`, not the `INFO` default used on create.
            instructions_timeout: New time in seconds before a pipeline instruction
                is considered timed out. Must be greater than 0. Example: `30`
            cpu_pin: Zero indexed CPU thread number. Must be lower than the node's
                thread count.
            performance_mode: True to run the pinned thread in performance mode.
            node_reference_id: ID of the related node.
            force_restart: If true and the pipeline is running, the pipeline is
                restarted when the new configuration cannot be applied to the current
                run. The call then returns once the new run is running.
        """
        return await self._transport.unary(
            [Route("PUT", "/v1/nodes/{node_id}/pipelines/{id}", "*")],
            UpdatePipelineRequest(
                node_id=node_id,
                id=id,
                name=name,
                json_config=json_config,
                restart_policy=restart_policy or RestartPolicy(),
                startup_policy=startup_policy or StartupPolicy(),
                default_logging_level=default_logging_level,
                instructions_timeout=instructions_timeout,
                cpu_pin=cpu_pin,
                performance_mode=performance_mode,
                node_reference_id=node_reference_id,
                force_restart=force_restart,
            ),
            UpdatePipelineResponse,
        )

    async def delete_pipeline(
        self,
        *,
        node_id: str = "",
        id: str = "",
    ) -> DeletePipelineResponse:
        """Delete a pipeline. Fails with a not found error if it does not exist.

        Args:
            node_id: ID of the node that hosts the pipeline.
            id: ID of the pipeline to delete.
        """
        return await self._transport.unary(
            [Route("DELETE", "/v1/nodes/{node_id}/pipelines/{id}", "")],
            DeletePipelineRequest(node_id=node_id, id=id),
            DeletePipelineResponse,
        )

    async def start_pipeline(
        self,
        *,
        node_id: str = "",
        id: str | None = None,
        name: str | None = None,
    ) -> StartPipelineResponse:
        """Start a pipeline and return its new run once it is running. Fails if the
        pipeline is unknown, already started, or does not reach the running state
        within 10 seconds.

        Args:
            node_id: ID of the node that hosts the pipeline.
            id: ID of the pipeline.
            name: Exact name of the pipeline. Fails if more than one pipeline has
                this name. Example: `UDP tunnel`
        """
        return await self._transport.unary(
            [
                Route("POST", "/v1/nodes/{node_id}/pipelines/{id}/start", ""),
                Route("POST", "/v1/nodes/{node_id}/pipelines-by-name/{name}/start", ""),
            ],
            StartPipelineRequest(node_id=node_id, id=id, name=name),
            StartPipelineResponse,
        )

    async def stop_pipeline(
        self,
        *,
        node_id: str = "",
        id: str | None = None,
        name: str | None = None,
        run_id: str | None = None,
    ) -> StopPipelineResponse:
        """Stop a pipeline, found by its ID, its name or its current run. Returns once
        the stop is requested, without waiting for the run to end. Fails if the
        pipeline is unknown or already stopped.

        Args:
            node_id: ID of the node that hosts the pipeline.
            id: ID of the pipeline.
            name: Exact name of the pipeline. Fails if more than one pipeline has
                this name. Example: `UDP tunnel`
            run_id: ID of the pipeline's current run.
        """
        return await self._transport.unary(
            [
                Route("POST", "/v1/nodes/{node_id}/pipelines/{id}/stop", ""),
                Route("POST", "/v1/nodes/{node_id}/pipelines-by-name/{name}/stop", ""),
                Route("POST", "/v1/nodes/{node_id}/pipeline-runs/{run_id}/stop", ""),
            ],
            StopPipelineRequest(node_id=node_id, id=id, name=name, run_id=run_id),
            StopPipelineResponse,
        )

    def stream_pipelines(
        self,
        *,
        node_id: str = "",
    ) -> AsyncServerStream[StreamPipelinesEvent]:
        """Stream changes to the pipelines of a node. Nothing is sent when the stream
        opens, so get the pipelines first for the current list. An event is sent each
        time a pipeline is created, updated or deleted, and when a pipeline starts or
        stops.

        Args:
            node_id: ID of the node to stream pipeline changes from.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/nodes/{node_id}/pipelines", "")],
            StreamPipelinesRequest(node_id=node_id),
            StreamPipelinesEvent,
        )

    def open_log_stream(
        self,
        *,
        node_id: str = "",
        run_id: str = "",
        options: Options | None = None,
    ) -> AsyncServerStream[LogStreamMessages]:
        """Stream the log messages of a pipeline run. The requested number of past lines
        is sent first, then new messages as they are logged.

        Args:
            node_id: ID of the node that hosts the run.
            run_id: ID of the run to stream logs from.
            options: Stream options, such as how many past lines to send first.
                Leave unset to receive only new messages.
        """
        return self._transport.server_stream(
            [
                Route("GET", "/v1/streams/nodes/{node_id}/pipeline-runs/{run_id}/logs", ""),
            ],
            PipelineOpenLogStreamRequest(
                node_id=node_id,
                run_id=run_id,
                options=options or Options(),
            ),
            LogStreamMessages,
        )

    def open_telemetry_stream(
        self,
        *,
        node_id: str = "",
        run_id: str = "",
    ) -> AsyncServerStream[TelemetrySample]:
        """Streams telemetry samples (metrics and KPI values) of a pipeline run at
        regular intervals while the run is active. The stream ends with an error when
        the run stops, when the run is unknown, or when the node disconnects.

        Args:
            node_id: ID of the node that hosts the run.
            run_id: ID of the run to stream telemetry from.
        """
        return self._transport.server_stream(
            [
                Route("GET", "/v1/streams/nodes/{node_id}/pipeline-runs/{run_id}/telemetry", ""),
            ],
            OpenTelemetryStreamRequest(node_id=node_id, run_id=run_id),
            TelemetrySample,
        )


class AsyncResourcesServiceClient:
    """Live system information of a node: resource metrics such as CPU, memory, storage
    and network interface usage, and the network flows crossing its interfaces. Use
    this service to monitor the health and traffic of any node.
    """

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    def open_metrics_stream(
        self,
        *,
        node_id: str = "",
    ) -> AsyncServerStream[MetricsSample]:
        """Stream the resource metrics of a node, such as CPU, memory, disk and network
        interface usage. A sample of the current metrics is sent when the stream
        opens. The stream stays open until the client closes it, and ends with an
        error if the node loses its connection.

        Args:
            node_id: ID of the node to read metrics from.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/nodes/{node_id}/metrics", "")],
            OpenMetricsStreamRequest(node_id=node_id),
            MetricsSample,
        )

    def open_flows_stream(
        self,
        *,
        node_id: str = "",
    ) -> AsyncServerStream[FlowsSample]:
        """Stream a snapshot of the network flows crossing the interfaces of a node,
        about once a second, starting right away. The node only captures packets
        while someone watches its flows, so the first samples may be empty or
        incomplete.

        Args:
            node_id: ID of the node to read flows from.
        """
        return self._transport.server_stream(
            [Route("GET", "/v1/streams/nodes/{node_id}/flows", "")],
            OpenFlowsStreamRequest(node_id=node_id),
            FlowsSample,
        )


class _Services:
    blueprints: BlueprintsClient
    config: ConfigServiceClient
    hub_client: HubClientServiceClient
    hub_server: HubServerServiceClient
    logging: LoggingServiceClient
    network_instances: NetworkInstancesClient
    networks: NetworksClient
    pipelines: PipelinesServiceClient
    resources: ResourcesServiceClient

    def __init__(self, transport: Transport) -> None:
        self.blueprints = BlueprintsClient(transport)
        self.config = ConfigServiceClient(transport)
        self.hub_client = HubClientServiceClient(transport)
        self.hub_server = HubServerServiceClient(transport)
        self.logging = LoggingServiceClient(transport)
        self.network_instances = NetworkInstancesClient(transport)
        self.networks = NetworksClient(transport)
        self.pipelines = PipelinesServiceClient(transport)
        self.resources = ResourcesServiceClient(transport)


class _AsyncServices:
    blueprints: AsyncBlueprintsClient
    config: AsyncConfigServiceClient
    hub_client: AsyncHubClientServiceClient
    hub_server: AsyncHubServerServiceClient
    logging: AsyncLoggingServiceClient
    network_instances: AsyncNetworkInstancesClient
    networks: AsyncNetworksClient
    pipelines: AsyncPipelinesServiceClient
    resources: AsyncResourcesServiceClient

    def __init__(self, transport: AsyncTransport) -> None:
        self.blueprints = AsyncBlueprintsClient(transport)
        self.config = AsyncConfigServiceClient(transport)
        self.hub_client = AsyncHubClientServiceClient(transport)
        self.hub_server = AsyncHubServerServiceClient(transport)
        self.logging = AsyncLoggingServiceClient(transport)
        self.network_instances = AsyncNetworkInstancesClient(transport)
        self.networks = AsyncNetworksClient(transport)
        self.pipelines = AsyncPipelinesServiceClient(transport)
        self.resources = AsyncResourcesServiceClient(transport)
