from datetime import datetime, timedelta

from app.api import monitoring_api
from flask_restx import Namespace

now = datetime.now()
start_time = str((now - timedelta(hours=9, minutes=30)
                  ).strftime("%Y-%m-%dT%H:%M:%S.000Z")
                 )
end_time = str((now - timedelta(hours=9)
                ).strftime("%Y-%m-%dT%H:%M:%S.000Z")
               )
step_time = "60s"


def getNs() -> Namespace:

    return monitoring_api.ns

def getModuleInfoParser():
    parser = getNs().parser()
    parser.add_argument(
        "node",
        location="args",
        type=str,
        # default="worker3",
        required=True,
        help="""
            1. worker3
            """
    )

    return parser

def getRabbitmqMonitoringParser():
    parser = getNs().parser()
    parser.add_argument(
        "start_time", location="args", type=str, required=True, help=start_time)
    parser.add_argument(
        "end_time", location="args", type=str, required=True, help=end_time)
    parser.add_argument(
        "step_time", location="args", type=str, required=True, help=step_time)
    parser.add_argument(
        "expr_type",
        location="args",
        type=str,
        default="RabbitmqMonitoring",
        required=True,
        choices=["RabbitmqMonitoring"],
        help="""
            1. RabbitmqMonitoring
            """
    )
    parser.add_argument(
        "expr_name",
        location="args",
        type=str,
        default="Publishers",
        required=True,
        choices=[
            "Publishers",
            "Consumers",
            "Channels",
            "Nodes",
            "Messages Published",
            "Messages Delivered",
            "Total Messages Published",
            "Total Messages Delivered"
        ],
        help="""
            1. Publishers
            2. Consumers
            3. Channels
            4. Nodes
            5. Messages Published
            6. Messages Delivered
            7. Total Messages Published
            8. Total Messages Delivered
            """
    )
    parser.add_argument(
        "variable_key",
        location="args",
        type=str,
        # default="namespace",
        required=True,
        choices=[
            "namespace"
        ],
        help="""
            1. namespace
            """
    )
    parser.add_argument(
        "variable_values",
        location="args",
        type=str,
        # default="monitoring",
        required=True,
        help="""
            1. rabbitmq-system
            """
    )

    return parser


def getPodMonitoringParser():
    parser = getNs().parser()
    parser.add_argument(
        "start_time", location="args", type=str, required=True, help=start_time)
    parser.add_argument(
        "end_time", location="args", type=str, required=True, help=end_time)
    parser.add_argument(
        "step_time", location="args", type=str, required=True, help=step_time)
    parser.add_argument(
        "expr_type",
        location="args",
        type=str,
        default="PodMonitoring",
        required=True,
        choices=["PodMonitoring"],
        help="""
                    1. PodMonitoring
                    """)
    parser.add_argument(
        "expr_name",
        location="args",
        type=str,
        # default="CPU Usage",
        required=True,
        choices=[
            "CPU Usage",
            "Memory Usage (w/o cache)",
            "Receive Bandwidth",
            "Transmit Bandwidth",
            "Rate of Received Packets",
            "Rate of Transmitted Packets",
            "Rate of Received Packets Dropped",
            "Rate of Transmitted Packets Dropped",
            "IOPS(Reads+Writes)",
            "ThroughPut(Read+Write)"
        ],
        help="""
            1. CPU Usage
            2. Memory Usage (w/o cache)
            3. Receive Bandwidth
            4. Transmit Bandwidth
            5. Rate of Received Packets
            6. Rate of Transmitted Packets
            7. Rate of Received Packets Dropped
            8. Rate of Transmitted Packets Dropped
            9. IOPS(Reads+Writes)
            10. ThroughPut(Read+Write)
            """
    )
    parser.add_argument(
        "variable_key",
        location="args",
        type=str,
        # default="namespace",
        required=True,
        choices=[
            "namespace"
        ],
        help="""
            1. namespace
            """
    )
    parser.add_argument(
        "variable_values",
        location="args",
        type=str,
        # default="monitoring",
        required=True,
        help="""
            1. monitoring
            2. monitoring|mongodb
            """
    )

    return parser


def getGPUMonitoringParser():
    parser = getNs().parser()
    parser.add_argument(
        "start_time", location="args", type=str, required=True, help=start_time)
    parser.add_argument(
        "end_time", location="args", type=str, required=True, help=end_time)
    parser.add_argument(
        "step_time", location="args", type=str, required=True, help=step_time)
    parser.add_argument(
        "expr_type",
        location="args",
        type=str,
        default="GpuMonitoring",
        required=True,
        choices=["GpuMonitoring"],
        help="""
            1. GpuMonitoring
            """
    )
    parser.add_argument(
        "expr_name",
        location="args",
        type=str,
        # default="GPU Temperature",
        required=True,
        choices=[
            "GPU Temperature",
            "GPU Power Usage",
            "GPU Memory Clocks",
            "GPU SM Clocks",
            "GPU Mem Copy Utilization",
            "GPU Framebuffer Mem Used",
            "GPU Framebuffer Mem Free"
        ],
        help="""
            1. GPU Temperature
            2. GPU Power Usage
            3. GPU Memory Clocks
            4. GPU SM Clocks
            5. GPU Mem Copy Utilization
            6. GPU Framebuffer Mem Used
            7. GPU Framebuffer Mem Free
            """
    )
    parser.add_argument(
        "variable_key",
        location="args",
        type=str,
        # default="instance",
        required=True,
        choices=["instance"],
        help="""
            1. instance
            """
    )
    parser.add_argument(
        "variable_values",
        location="args",
        type=str,
        # default="worker3",
        required=True,
        help="""
            1. worker3
            """
    )

    return parser


def getNodeMonitoringParser():
    parser = getNs().parser()
    parser.add_argument(
        "start_time", location="args", type=str, required=True, help=start_time)
    parser.add_argument(
        "end_time", location="args", type=str, required=True, help=end_time)
    parser.add_argument(
        "step_time", location="args", type=str, required=True, help=step_time)
    parser.add_argument(
        "expr_type",
        location="args",
        type=str,
        default="NodeMonitoring",
        required=True,
        choices=["NodeMonitoring"],
        help="""
            1. NodeMonitoring
            """
    )
    parser.add_argument(
        "expr_name",
        location="args",
        type=str,
        # default="CPU Usage",
        required=True,
        choices=[
            "CPU Usage",
            "Core Usage",
            "Load Average",
            "Memory Usage",
            "Disk I/O Read",
            "Disk I/O Write",
            "Disk Space Usage",
            "Disk Usage Percent",
            "Network Received",
            "Network Transmitted"
        ],
        help="""
            1. CPU Usage
            2. Core Usage
            3. Load Average
            4. Memory Usage
            5. Disk I/O Read
            6. Disk I/O Write
            7. Disk Space Usage
            8. Disk Usage Percent
            9. Network Received
            10. Network Transmitted
            """
    )
    parser.add_argument(
        "variable_key",
        location="args",
        type=str,
        # default="instance",
        required=True,
        choices=["instance"],
        help="""
            1. instance
            """
    )
    parser.add_argument(
        "variable_values",
        location="args",
        type=str,
        # default="master1",
        required=True,
        help="""
            1. master1
            """
    )

    return parser


def getClusterMonitoringParser():
    parser = getNs().parser()
    parser.add_argument(
        "start_time", location="args", type=str, required=True, help=start_time)
    parser.add_argument(
        "end_time", location="args", type=str, required=True, help=end_time)
    parser.add_argument(
        "step_time", location="args", type=str, required=True, help=step_time)
    parser.add_argument(
        "expr_type",
        location="args",
        type=str,
        default="ClusterMonitoring",
        required=True,
        choices=["ClusterMonitoring"],
        help="""
            1. ClusterMonitoring
            """
    )
    parser.add_argument(
        "expr_name",
        location="args",
        type=str,
        # default="CPU Usage",
        required=True,
        choices=[
            "CPU Usage",
            "Load Average",
            "Memory Usage",
            "Disk I/O Read",
            "Disk I/O Write",
            "Disk Space Usage",
            "Network Received",
            "Network Transmitted"
        ],
        help="""
            1. CPU Usage
            2. Load Average
            3. Memory Usage
            5. Disk I/O Read
            6. Disk I/O Write
            7. Disk Space Usage
            8. Network Received
            9. Network Transmitted
            """
    )
    parser.add_argument(
        "variable_key",
        location="args",
        type=str,
        default="instance",
        required=True,
        # choices=["instance"],
        help="""
            1. instance
            """
    )
    parser.add_argument(
        "variable_values",
        location="args",
        type=str,
        # default="master1|worker1|worker2",
        required=True,
        help="""
            1. master1
            2. master1|worker1|worker2
            """
    )

    return parser


def getVariableValuesParser():
    parser = getNs().parser()
    parser.add_argument(
        "variable_type",
        location="args",
        type=str,
        # default="ClusterMonitoring",
        required=True,
        choices=[
            "ClusterMonitoring",
            "NodeMonitoring",
            "PodMonitoring"
        ])
    parser.add_argument(
        "variable_key",
        location="args",
        type=str,
        # default="Instance",
        required=True,
        choices=[
            "Instance",
            "Namespace"
        ])

    return parser


def getMetaDatasParser():
    parser = getNs().parser()
    parser.add_argument(
        "meta_name",
        location="args",
        type=str,
        # default="ClusterMonitoring",
        required=True,
        choices=[
            "ClusterMonitoring",
            "NodeMonitoring",
            "PodMonitoring"
        ])

    return parser


# datetime_range_model = ns.model(
#         "datetime_range_model",
#         {
#             "start_time": fields.DateTime(required=True),
#             "end_time": fields.DateTime(required=True)
#         },
#         Required=True)

# query_string_model = ns.model(
#         "query_string_model",
#         {
#             "type": fields.String(description="", required=True, example="namespace"),
#             "value": fields.String(description="", required=True, example="monitoring")
#         },
#         Required=True)

# monitoring_model = ns.model(
#         "monitoring_model",
#         {
#             "datetime_range": fields.Nested(datetime_range_model, required=True),
#             "query_string": fields.Nested(query_string_model, required=True)
#         },
#         Required=True)
