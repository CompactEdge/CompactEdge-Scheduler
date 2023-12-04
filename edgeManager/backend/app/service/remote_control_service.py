from typing import Union

from utils.logger import Log as log

from .remote_control.package.vo.remote_control_result_vo import \
    RemoteControlResultVo
from .remote_control.remote_control import RemoteControl


class RemoteControlValidateService():

    def __init__(self):
        self.remote_control = RemoteControl()
        self.remote_control_common = self.remote_control.remote_control_common
        self.remote_control_docker = self.remote_control.remote_control_docker
        self.remote_control_k8s = self.remote_control.remote_control_k8s
        self.remote_control_status = self.remote_control.remote_control_status

    def __generate_with_validation_data(self, *args: RemoteControlResultVo) -> Union[int, dict]:
        generate_with_validation_data_result_code = 500
        generate_with_validation_data_result_validate = False
        generate_with_validation_data_result_data = {}

        try:
            args_service_codes = list()
            args_service_validates = list()
            args_service_datas = dict()

            for arg in args:
                service_code = arg.service_code
                service_name = arg.service_name
                service_validate = arg.service_validate

                args_service_codes.append(service_code)
                args_service_validates.append(service_validate)
                args_service_datas[service_name] = arg

            generate_with_validation_data_result_code = max(args_service_codes)
            generate_with_validation_data_result_validate = min(
                args_service_validates)
            generate_with_validation_data_result_data = args_service_datas

        except Exception as ex:
            log.error(ex)

        return generate_with_validation_data_result_code, generate_with_validation_data_result_validate, generate_with_validation_data_result_data

    def validate_node_health(self, service_type: str, **kwargs) -> Union[int, dict]:
        validate_node = self.remote_control_common.validate_node(
            service_type, **kwargs)
        validate_worker_node = self.remote_control_k8s.validate_worker_node(
            service_type, validate_node.service_result)
        validate_installed_apps = self.remote_control_common.validate_installed_apps(
            **kwargs)

        validate_node_health_code, validate_node_health_validate, validate_node_health_data = self.__generate_with_validation_data(
            validate_node,
            validate_worker_node,
            validate_installed_apps)

        if validate_node_health_validate:
            self.remote_control_status.create_sessions(**kwargs)

        return validate_node_health_code, validate_node_health_data

    def validate_working_progress_logs(self, **kwargs) -> Union[int, dict]:
        return self.remote_control_status.find_by_working(**kwargs)


class RemoteControlExecuteService():

    def __init__(self):
        self.remote_control = RemoteControl()
        self.remote_control_docker = self.remote_control.remote_control_docker
        self.remote_control_status = self.remote_control.remote_control_status
        self.remote_control_ubuntu = self.remote_control.remote_control_ubuntu
        self.remote_control_k8s = self.remote_control.remote_control_k8s

    def __generate_with_execute_data(self, *args: RemoteControlResultVo) -> Union[int, dict]:
        generate_with_execute_data_result_code = 500
        generate_with_execute_data_result_data = dict()

        try:
            args_service_codes = list()
            args_service_datas = dict()

            for index, value in enumerate(args):
                service_code = value.service_code
                service_name = value.service_name

                args_service_codes.append(service_code)
                args_service_datas[str(index)] = {service_name: value}

            generate_with_execute_data_result_code = max(args_service_codes)
            generate_with_execute_data_result_data = args_service_datas

        except Exception as ex:
            log.error(ex)

        return generate_with_execute_data_result_code, generate_with_execute_data_result_data

    def execute_join_k8s_worker_node(self, service_type: str) -> RemoteControlResultVo:
        execute_get_join_command: RemoteControlResultVo = self.remote_control_k8s.get_join_command(
            service_type)
        execute_join_worker_node: RemoteControlResultVo = self.remote_control_k8s.join_worker_node(
            service_type, execute_get_join_command.service_result)

        return self.__generate_with_execute_data(execute_get_join_command, execute_join_worker_node)

    def execute_install_k8s(self, service_type: str):
        self.remote_control_k8s.set_up_gpg_key()
        self.remote_control_k8s.set_up_repo_key()
        execute_update_k8s = self.remote_control_k8s.update_k8s(service_type)
        execute_install_k8s = self.remote_control_k8s.install_k8s(service_type)
        self.remote_control_k8s.mark_k8s()
        self.remote_control_k8s.daemon_reload_k8s()
        self.remote_control_k8s.restart_kubelet()
        self.remote_control_k8s.enable_kubelet()
        execute_status_k8s = self.remote_control_k8s.status_kubelet(
            service_type)

        return self.__generate_with_execute_data(execute_update_k8s, execute_install_k8s, execute_status_k8s)

    def execute_install_docker(self, service_type: str) -> Union[int, dict]:
        self.remote_control_docker.set_up_mkdir()
        self.remote_control_docker.set_up_gpg_key()
        self.remote_control_docker.set_up_repo_key()
        execute_update_docker = self.remote_control_docker.update_docker(
            service_type)
        execute_install_docker = self.remote_control_docker.install_docker(
            service_type)
        self.remote_control_docker.mark_docker()
        self.remote_control_docker.edit_cgroup_docker()
        self.remote_control_docker.daemon_reload_docker()
        self.remote_control_docker.restart_docker()
        self.remote_control_docker.enable_docker()
        execute_status_docker = self.remote_control_docker.status_docker(
            service_type)
        execute_status_cgroup = self.remote_control_docker.status_cgroup_docker(
            service_type)

        return self.__generate_with_execute_data(execute_update_docker, execute_install_docker, execute_status_docker, execute_status_cgroup)

    def execute_default_preferences_management(self, service_type: str) -> Union[int, dict]:
        self.remote_control_ubuntu.ufw_stop()
        self.remote_control_ubuntu.ufw_disable()
        execute_systemd = self.remote_control_ubuntu.ufw_status(service_type)

        self.remote_control_ubuntu.swap_off()
        self.remote_control_ubuntu.swap_remove()
        self.remote_control_ubuntu.swap_disable()
        execute_swap = self.remote_control_ubuntu.swap_validate(service_type)

        self.remote_control_ubuntu.ip_forward_alter()
        execute_ip_forward = self.remote_control_ubuntu.ip_forward_validate(
            service_type)

        self.remote_control_ubuntu.iptables_modprobe_overlay()
        self.remote_control_ubuntu.iptables_modprobe_br_netfilter()
        # lsmod 상태 조회 추가

        self.remote_control_ubuntu.iptables_bridge_nf_call_iptables_create()
        execute_iptables_bridge_nf_call_iptables_validate = self.remote_control_ubuntu.iptables_bridge_nf_call_iptables_validate(
            service_type)
        self.remote_control_ubuntu.iptables_k8s_conf_create()
        execute_iptables_k8s_conf_validate = self.remote_control_ubuntu.iptables_k8s_conf_validate(
            service_type)

        return self.__generate_with_execute_data(execute_systemd, execute_swap, execute_ip_forward, execute_iptables_bridge_nf_call_iptables_validate, execute_iptables_k8s_conf_validate)

    def execute_default_package_management(self, service_type: str) -> Union[int, dict]:
        execute_update_apt_data = self.remote_control_ubuntu.apt_update(
            service_type)
        execute_upgrade_apt_data = self.remote_control_ubuntu.apt_upgrade(
            service_type)
        execute_install_apt_data = self.remote_control_ubuntu.apt_install(
            service_type)

        return self.__generate_with_execute_data(execute_update_apt_data, execute_upgrade_apt_data, execute_install_apt_data)

    def execute_init_sessions(self) -> Union[int, dict]:
        init_sessions: Union[int, str]
        init_working: Union[int, str]

        service_type = 'execute_init_sessions'

        init_sessions = self.remote_control_status.init_sessions(service_type)
        init_working = self.remote_control_status.init_working(service_type)

        return self.__generate_with_execute_data(init_sessions, init_working)
