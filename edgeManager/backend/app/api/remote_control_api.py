from http import HTTPStatus

import app.model.remote_control_model as remote_control_model
from app.service.remote_control_service import (RemoteControlExecuteService,
                                                RemoteControlValidateService)
from flask import jsonify, make_response, request
from flask_restx import Resource

remote_control_ns = remote_control_model.ns


def get_service_type(url: str) -> str:
    return url.split('/')[-1]


@remote_control_ns.route("/init_sessions")
@remote_control_ns.doc("")
class InitSessions(Resource):

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.remote_control_execute_service = RemoteControlExecuteService()

    @remote_control_ns.response(200, """{ 'service_code': 200, 'service_type': '', 'service_name': '', 'service_validate': '', 'service_result': '' }""")
    def get(self):
        """ Init sessions """
        init_sessions_code, init_sessions_data = \
            self.remote_control_execute_service.execute_init_sessions()

        return make_response(jsonify(init_sessions_data), HTTPStatus(init_sessions_code))


@remote_control_ns.route("/working_progress_logs")
@remote_control_ns.doc("")
class WorkingProgressLogs(Resource):

    remote_control_working_progress_parser = remote_control_model.remote_control_working_progress_parser

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.remote_control_validate_service = RemoteControlValidateService()

    @remote_control_ns.expect(remote_control_working_progress_parser)
    @remote_control_ns.response(200, """{ 'service_code': 200, 'service_type': '', 'service_name': '', 'service_validate': '', 'service_result': '' }""")
    def get(self):
        """ Working progress """
        remote_control_working_progress_args = self.remote_control_working_progress_parser.parse_args()

        remote_control_working_progress_code, remote_control_working_progress_data = \
            self.remote_control_validate_service.validate_working_progress_logs(
                **remote_control_working_progress_args)

        return make_response(jsonify(remote_control_working_progress_data), HTTPStatus(remote_control_working_progress_code))


@remote_control_ns.route("/execute_join_k8s_worker_node")
@remote_control_ns.doc("")
class ExecuteJoinK8sWorkerNode(Resource):

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.remote_control_execute_service = RemoteControlExecuteService()

    @remote_control_ns.response(200, """{ 'service_code': 200, 'service_type': '', 'service_name': '', 'service_validate': '', 'service_result': '' }""")
    def get(self):
        """ Execute join k8s worker node """
        service_type = get_service_type(request.path)

        execute_join_k8s_worker_node_code, execute_join_k8s_worker_node_data = self.remote_control_execute_service.execute_join_k8s_worker_node(
            service_type)

        return make_response(jsonify(execute_join_k8s_worker_node_data), HTTPStatus(execute_join_k8s_worker_node_code))


@remote_control_ns.route("/execute_install_k8s")
@remote_control_ns.doc("")
class ExecuteInstallK8s(Resource):

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.remote_control_execute_service = RemoteControlExecuteService()

    @remote_control_ns.response(200, """{ 'service_code': 200, 'service_type': '', 'service_name': '', 'service_validate': '', 'service_result': '' }""")
    def get(self):
        """ Execute install k8s """
        service_type = get_service_type(request.path)

        execute_install_k8s_code, execute_install_k8s_data = self.remote_control_execute_service.execute_install_k8s(
            service_type)

        return make_response(jsonify(execute_install_k8s_data), HTTPStatus(execute_install_k8s_code))


@remote_control_ns.route("/execute_install_docker")
@remote_control_ns.doc("")
class ExecuteInstallDocker(Resource):

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.remote_control_execute_service = RemoteControlExecuteService()

    @remote_control_ns.response(200, """{ 'service_code': 200, 'service_type': '', 'service_name': '', 'service_validate': '', 'service_result': '' }""")
    def get(self):
        """ Execute install docker """
        service_type = get_service_type(request.path)

        execute_install_docker_code, execute_install_docker_data = self.remote_control_execute_service.execute_install_docker(
            service_type)

        return make_response(jsonify(execute_install_docker_data), HTTPStatus(execute_install_docker_code))


@remote_control_ns.route("/execute_default_preferences_management")
@remote_control_ns.doc("")
class ExecuteDefaultPreferencesManagement(Resource):

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.remote_control_validate_service = RemoteControlValidateService()
        self.remote_control_execute_service = RemoteControlExecuteService()

    @remote_control_ns.response(200, """{ 'service_code': 200, 'service_type': '', 'service_name': '', 'service_validate': '', 'service_result': '' }""")
    def get(self):
        """ Execute default preferences management """
        service_type = get_service_type(request.path)

        execute_preferences_code, execute_preferences_data = self.remote_control_execute_service.execute_default_preferences_management(
            service_type)

        return make_response(jsonify(execute_preferences_data), HTTPStatus(execute_preferences_code))


@remote_control_ns.route("/execute_default_package_management")
@remote_control_ns.doc("")
class ExecuteDefaultPackageManagement(Resource):

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.remote_control_execute_service = RemoteControlExecuteService()

    @remote_control_ns.expect()
    @remote_control_ns.response(200, """{ 'service_code': 200, 'service_type': '', 'service_name': '', 'service_validate': '', 'service_result': '' }""")
    def get(self):
        """ Execute default package management """
        service_type = get_service_type(request.path)

        execute_default_package_management_code, execute_default_package_management_data = \
            self.remote_control_execute_service.execute_default_package_management(
                service_type)

        return make_response(jsonify(execute_default_package_management_data), HTTPStatus(execute_default_package_management_code))


@remote_control_ns.route("/validate_node_health_management")
@remote_control_ns.doc("")
class ValidateNodeHealthManagement(Resource):

    node_health_management_parser = remote_control_model.node_health_management_parser

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.remote_control_validate_service = RemoteControlValidateService()

    @remote_control_ns.expect(node_health_management_parser)
    @remote_control_ns.response(200, """{ 'service_code': 200, 'service_type': '', 'service_name': '', 'service_validate': '', 'service_result': '' }""")
    def get(self):
        """ Node health management """
        service_type = get_service_type(request.path)
        node_health_management_args = self.node_health_management_parser.parse_args()

        validate_node_health_management_code, validate_node_health_management_data = \
            self.remote_control_validate_service.validate_node_health(
                service_type, **node_health_management_args)

        return make_response(jsonify(validate_node_health_management_data), HTTPStatus(validate_node_health_management_code))
