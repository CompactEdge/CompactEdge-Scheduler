from http import HTTPStatus

import app.model.monitoring_model as monitoring_model
from app.service.monitoring_service import KubernetesMonitoringService
from flask import jsonify, make_response
from flask_restx import Namespace, Resource

ns = Namespace("Monitoring api", description="Monitoring system")



@ns.route("/module_info/<string:resource_name>")
@ns.doc("")
class ModuleInfoResourcesMonitoring(Resource):

    module_info_ps = monitoring_model.getModuleInfoParser()

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.k8s_monitoring_service = KubernetesMonitoringService()

    @ns.expect(module_info_ps)
    @ns.response(200, "{ \"status\": [], \"status_code\": [], \"data\": {} }")
    def get(self, resource_name):
        """ Kubernetes Pod Resources """
        module_info_args = self.module_info_ps.parse_args()

        meta_name = {"meta_name": "ModuleInfoMonitoring"}
        meta_items = {
            "cpu": ["CPU Speed", "CPU Usage"],
            "memory": ["Memory Usage", "Memory Size"],
            "disk": ["Disk Usage", "Disk Response Time"],
            "network": ["Network Usage", "Network Speed"]
        }
        print("----------------")
        print(module_info_args["node"])
        variable_values = module_info_args["node"]

        result_data = self.k8s_monitoring_service.find_by_module_info(
            meta_name, meta_items[resource_name], variable_values)

        return make_response(jsonify(result_data), HTTPStatus(200 if len(result_data.keys()) > 0 else 500))


@ns.route("/module_info")
@ns.doc("")
class ModuleInfoMonitoring(Resource):

    module_info_ps = monitoring_model.getModuleInfoParser()

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.k8s_monitoring_service = KubernetesMonitoringService()

    @ns.expect(module_info_ps)
    @ns.response(200, "{ \"status\": [], \"status_code\": [], \"data\": {} }")
    def get(self):
        """ Kubernetes Pod Resources """
        module_info_args = self.module_info_ps.parse_args()
        meta_name = {"meta_name": "ModuleInfoMonitoring"}
        meta_data = self.k8s_monitoring_service.find_by_monitoring_meta_datas(
            meta_name)
        meta_items = meta_data["data"]["result"]
        variable_values = module_info_args["node"]

        result_data = self.k8s_monitoring_service.find_by_module_info(
            meta_name, meta_items, variable_values)

        return make_response(jsonify(result_data), HTTPStatus(200 if len(result_data.keys()) > 0 else 500))


@ns.route("/rabbitmq_monitoring")
@ns.doc("")
class RabbitmqMonitoring(Resource):

    rabbitmq_monitoring_ps = monitoring_model.getRabbitmqMonitoringParser()

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.k8s_monitoring_service = KubernetesMonitoringService()

    @ns.expect(rabbitmq_monitoring_ps)
    @ns.response(200, "{ \"status\": [], \"status_code\": [], \"data\": {} }")
    def get(self):
        """ Kubernetes RabbitMQ Resources """
        rabbitmq_monitoring_args = self.rabbitmq_monitoring_ps.parse_args()
        result_data = self.k8s_monitoring_service.find_by_monitoring_query_range(
            rabbitmq_monitoring_args)

        return make_response(jsonify(result_data), HTTPStatus(max(result_data["status_code"])))


@ns.route("/pod_monitoring")
@ns.doc("")
class PodMonitoring(Resource):

    pod_monitoring_ps = monitoring_model.getPodMonitoringParser()

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.k8s_monitoring_service = KubernetesMonitoringService()

    @ns.expect(pod_monitoring_ps)
    @ns.response(200, "{ \"status\": [], \"status_code\": [], \"data\": {} }")
    def get(self):
        """ Kubernetes Pod Resources """
        pod_monitoring_args = self.pod_monitoring_ps.parse_args()
        result_data = self.k8s_monitoring_service.find_by_monitoring_query_range(
            pod_monitoring_args)

        return make_response(jsonify(result_data), HTTPStatus(max(result_data["status_code"])))


@ns.route("/gpu_monitoring")
@ns.doc("")
class GpuMonitoring(Resource):

    gpu_monitoring_ps = monitoring_model.getGPUMonitoringParser()

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.k8s_monitoring_service = KubernetesMonitoringService()

    @ns.expect(gpu_monitoring_ps)
    @ns.response(200, "{ \"status\": [], \"status_code\": [], \"data\": {} }")
    def get(self):
        """ Gpu Compute Resources """
        gpu_monitoring_args = self.gpu_monitoring_ps.parse_args()
        result_data = self.k8s_monitoring_service.find_by_monitoring_query_range(
            gpu_monitoring_args)

        return make_response(jsonify(result_data), HTTPStatus(max(result_data["status_code"])))


@ns.route("/node_monitoring")
@ns.doc("")
class NodeMonitoring(Resource):

    node_monitoring_ps = monitoring_model.getNodeMonitoringParser()

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.k8s_monitoring_service = KubernetesMonitoringService()

    @ns.expect(node_monitoring_ps)
    @ns.response(200, "{ \"status\": [], \"status_code\": [], \"data\": {} }")
    def get(self):
        """ Node Compute Resources """
        node_monitoring_args = self.node_monitoring_ps.parse_args()
        result_data = self.k8s_monitoring_service.find_by_monitoring_query_range(
            node_monitoring_args)

        return make_response(jsonify(result_data), HTTPStatus(max(result_data["status_code"])))


@ns.route("/cluster_monitoring")
@ns.doc("")
class ClusterMonitoring(Resource):

    cluster_monitoring_ps = monitoring_model.getClusterMonitoringParser()

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.k8s_monitoring_service = KubernetesMonitoringService()

    @ns.expect(cluster_monitoring_ps)
    @ns.response(200, "{ \"status\": [], \"status_code\": [], \"data\": {} }")
    def get(self):
        """ Cluster Compute Resources """
        cluster_monitoring_args = self.cluster_monitoring_ps.parse_args()
        result_data = self.k8s_monitoring_service.find_by_monitoring_query_range(
            cluster_monitoring_args)

        return make_response(jsonify(result_data), HTTPStatus(max(result_data["status_code"])))


@ns.route("/variable_values")
@ns.doc("")
class VariableValues(Resource):

    variable_values_ps = monitoring_model.getVariableValuesParser()

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.k8s_monitoring_service = KubernetesMonitoringService()

    @ns.expect(variable_values_ps)
    @ns.response(200, "{ \"status\": [], \"status_code\": [], \"data\": {} }")
    def get(self):
        """ Monitoring variable values """
        variable_values_args = self.variable_values_ps.parse_args()
        result_data = self.k8s_monitoring_service.find_by_monitoring_variable_values(
            variable_values_args)

        return make_response(jsonify(result_data), HTTPStatus(max(result_data["status_code"])))


@ns.route("/meta_datas")
@ns.doc("")
class MetaDatas(Resource):

    meta_datas_ps = monitoring_model.getMetaDatasParser()

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.k8s_monitoring_service = KubernetesMonitoringService()

    @ns.expect(meta_datas_ps)
    @ns.response(200, "{ \"status\": [], \"status_code\": [], \"data\": {} }")
    def get(self):
        """ Monitoring meta datas """
        meta_datas_args = self.meta_datas_ps.parse_args()
        result_data = self.k8s_monitoring_service.find_by_monitoring_meta_datas(
            meta_datas_args)

        return make_response(jsonify(result_data), HTTPStatus(max(result_data["status_code"])))
