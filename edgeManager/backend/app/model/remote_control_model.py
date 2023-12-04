from flask_restx import Namespace

ns = Namespace("RemoteControl api", description="Remote control system")


remote_control_working_progress_parser = ns.parser()
remote_control_working_progress_parser.add_argument(
        "service_type",
        location="args",
        type=str,
        required=True,
        # default='validate_node_health_management',
        help="""
                1. validate_node_health_management
                2. execute_default_package_management
                3. execute_default_preferences_management
                4. execute_install_docker
                5. execute_install_k8s
                """)


node_health_management_parser = ns.parser()
node_health_management_parser.add_argument(
        "server",
        location="args",
        type=str,
        required=True,
        # default='10.7.20.104',
        help="""
                1. 10.7.20.104
                """)
node_health_management_parser.add_argument(
        "port",
        location="args",
        type=str,
        required=True,
        # default='22',
        help="""
                1. 22
                """)
node_health_management_parser.add_argument(
        "username",
        location="args",
        type=str,
        required=True,
        # default='wiz',
        help="""
                1. wiz
                """)
node_health_management_parser.add_argument(
        "password",
        location="args",
        type=str,
        required=True,
        # default='qwe123',
        help="""
                1. qwe123
                """)