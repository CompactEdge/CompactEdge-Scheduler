
import time

from flask import current_app
from utils.logger import Log as log

from app.service import k8s_service
from .modules.remote_control_working import RemoteControlWorking
from .modules.remote_control_paramiko import RemoteControlParamiko

from .vo.remote_control_paramiko_vo import RemoteControlParamikoVo
from .vo.remote_control_result_vo import RemoteControlResultVo

from .meta import REMOTE_CONTROL_META
from .modules import REMOTE_CONTROL_SESSION_INFO


class RemoteControlK8s():

    def __init__(self):
        self.k8s_service = k8s_service
        self.remote_control_working = RemoteControlWorking()
        self.remote_control_paramiko = RemoteControlParamiko()

        self.k8s_versions = current_app.config["K8S_VERSIONS"]
        self.k8s_master_node_info = current_app.config["K8S_MASTER_NODE_INFO"]
        self.remote_control_apt_meta = REMOTE_CONTROL_META['remote_control_apt_meta']
        self.remote_control_k8s_meta = REMOTE_CONTROL_META['remote_control_k8s_meta']
        self.remote_contorl_systemd_meta = REMOTE_CONTROL_META['remote_contorl_systemd_meta']
        self.remote_control_session_info = REMOTE_CONTROL_SESSION_INFO

    def validate_worker_node(self, service_type: str, hostname: str) -> RemoteControlResultVo:
        validate_worker_node_data: RemoteControlResultVo

        try:
            service_func = 'execute_command'
            service_name = 'validate_worker_node'
            list_node_status = self.k8s_service.list_node_status()

            validate_worker_node_data = RemoteControlResultVo(
                service_code=200,
                service_type=service_type,
                service_func=service_func,
                service_name=service_name,
                service_validate=False not in list(
                    False if node_status['name'] == hostname else True for node_status in list_node_status),
                service_result=list(
                    '' if node_status['name'] != hostname else node_status['name'] for node_status in list_node_status)
            )

            self.remote_control_working.create(
                service_type, service_name, validate_worker_node_data)

        except KeyError as ex:
            log.error('validate_worker_node :: ' + str(ex))

        return validate_worker_node_data

    def set_up_gpg_key(self):
        try:
            set_up_gpg_key_meta = self.remote_control_k8s_meta['set_up_gpg_key']
            set_up_gpg_key_service_command = set_up_gpg_key_meta['service_command']
            set_up_gpg_key_service_name = 'set_up_gpg_key'

            set_up_gpg_key_command = self.remote_control_paramiko.make_command(
                command=set_up_gpg_key_service_command,
                password=self.remote_control_session_info.password)

            set_up_gpg_key_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=set_up_gpg_key_command)

            self.remote_control_paramiko.execute_command(
                set_up_gpg_key_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlK8s :: set_up_gpg_key :: ' + str(ex))

    def set_up_repo_key(self):
        try:
            set_up_repo_key_meta = self.remote_control_k8s_meta['set_up_repo_key']
            set_up_repo_key_service_command = set_up_repo_key_meta['service_command']
            set_up_repo_key_service_name = 'set_up_repo_key'

            set_up_repo_key_command = self.remote_control_paramiko.make_command(
                command=set_up_repo_key_service_command,
                password=self.remote_control_session_info.password)

            set_up_repo_key_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=set_up_repo_key_command)

            self.remote_control_paramiko.execute_command(
                set_up_repo_key_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlK8s :: set_up_repo_key :: ' + str(ex))

    def update_k8s(self, service_type: str) -> RemoteControlResultVo:
        update_k8s_result_vo: RemoteControlResultVo

        try:
            apt_update_meta = self.remote_control_apt_meta['apt_update']
            apt_update_service_func = apt_update_meta['service_func']
            apt_update_service_command = apt_update_meta['service_command']

            update_k8s_service_name = 'update_k8s'
            update_k8s_command = self.remote_control_paramiko.make_command(
                command=apt_update_service_command,
                password=self.remote_control_session_info.password)
            update_k8s_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=update_k8s_command)

            update_k8s_code, update_k8s_data = \
                self.remote_control_paramiko.execute_invoke_shell(
                    update_k8s_paramiko_vo, service_type, update_k8s_service_name)

            update_k8s_result_vo = RemoteControlResultVo(
                service_code=update_k8s_code,
                service_type=service_type,
                service_func=apt_update_service_func,
                service_name=update_k8s_service_name,
                service_validate=(False if update_k8s_code != 200 else True),
                service_result=update_k8s_data)

            # self.remote_control_working.create(service_type, update_k8s_service_name, update_k8s_result_vo)

        except KeyError as ex:
            log.error('RemoteControlK8s :: update_k8s :: ' + str(ex))

        return update_k8s_result_vo

    def install_k8s(self, service_type: str) -> RemoteControlResultVo:
        install_k8s_result_vo: RemoteControlResultVo

        try:
            apt_install_meta = self.remote_control_apt_meta['apt_install']
            apt_install_service_func = apt_install_meta['service_func']
            apt_install_service_command = apt_install_meta['service_command']

            install_k8s_meta_service_name = 'install_k8s'
            install_k8s_meta_apps = self.k8s_versions + ' --allow-change-held-packages'

            install_k8s_command = self.remote_control_paramiko.make_command(
                command=apt_install_service_command,
                password=self.remote_control_session_info.password,
                apps=install_k8s_meta_apps)

            install_k8s_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=install_k8s_command)

            install_k8s_code, install_k8s_data = self.remote_control_paramiko.execute_invoke_shell(
                install_k8s_paramiko_vo, service_type, install_k8s_meta_service_name)

            install_k8s_result_vo = RemoteControlResultVo(
                service_code=install_k8s_code,
                service_type=service_type,
                service_func=apt_install_service_func,
                service_name=install_k8s_meta_service_name,
                service_validate=(False if install_k8s_code != 200 else True),
                service_result=install_k8s_data)

            # self.remote_control_working.create(service_type, install_k8s_meta_service_name, install_k8s_result_vo)

        except KeyError as ex:
            log.error('RemoteControlK8s :: install_k8s :: ' + str(ex))

        return install_k8s_result_vo

    def mark_k8s(self):
        try:
            apt_mark_meta = self.remote_control_apt_meta['apt_mark']
            apt_mark_service_command = apt_mark_meta['service_command']

            mark_k8s_option = 'hold'
            mark_k8s_apps = 'kubelet kubeadm kubectl'

            mark_k8s_command = self.remote_control_paramiko.make_command(
                command=apt_mark_service_command,
                password=self.remote_control_session_info.password,
                option=mark_k8s_option,
                apps=mark_k8s_apps)

            mark_k8s_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=mark_k8s_command)

            self.remote_control_paramiko.execute_command(mark_k8s_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlK8s :: mark_k8s :: ' + str(ex))

    def daemon_reload_k8s(self):
        try:
            systemd_daemon_reload_meta = self.remote_contorl_systemd_meta['systemd_daemon_reload']
            systemd_daemon_reload_service_command = systemd_daemon_reload_meta['service_command']

            daemon_reload_k8s_command = self.remote_control_paramiko.make_command(
                command=systemd_daemon_reload_service_command,
                password=self.remote_control_session_info.password)

            daemon_reload_k8s_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=daemon_reload_k8s_command)

            self.remote_control_paramiko.execute_command(
                daemon_reload_k8s_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlK8s :: daemon_reload_k8s :: ' + str(ex))

    def restart_kubelet(self):
        try:
            systemd_restart_meta = self.remote_contorl_systemd_meta['systemd_restart']
            systemd_restart_service_command = systemd_restart_meta['service_command']

            restart_kubelet_app = 'kubelet'

            restart_kubelet_command = self.remote_control_paramiko.make_command(
                command=systemd_restart_service_command,
                password=self.remote_control_session_info.password,
                app=restart_kubelet_app)

            restart_kubelet_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=restart_kubelet_command)

            self.remote_control_paramiko.execute_command(
                restart_kubelet_paramiko_vo)
            time.sleep(10)

        except KeyError as ex:
            log.error('RemoteControlK8s :: restart_kubelet :: ' + str(ex))

    def enable_kubelet(self):
        try:
            systemd_enable_meta = self.remote_contorl_systemd_meta['systemd_enable']
            systemd_enable_service_command = systemd_enable_meta['service_command']

            enable_kubelet_app = 'kubelet'

            enable_kubelet_command = self.remote_control_paramiko.make_command(
                command=systemd_enable_service_command,
                password=self.remote_control_session_info.password,
                app=enable_kubelet_app)

            enable_kubelet_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=enable_kubelet_command)

            self.remote_control_paramiko.execute_command(
                enable_kubelet_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlK8s :: enable_kubelet :: ' + str(ex))

    def status_kubelet(self, service_type: str):
        status_kubelet_data: RemoteControlResultVo

        try:
            systemd_status_meta = self.remote_contorl_systemd_meta['systemd_status']
            systemd_status_service_func = systemd_status_meta['service_func']
            systemd_status_service_command = systemd_status_meta['service_command']

            status_kubelet_service_name = 'status_kubelet'
            status_kubelet_service_app = 'kubelet'
            status_kubelet_command = self.remote_control_paramiko.make_command(
                command=systemd_status_service_command,
                password=self.remote_control_session_info.password,
                app=status_kubelet_service_app)
            status_kubelet_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=status_kubelet_command)

            status_kubelet_code, status_kubelet_data = self.remote_control_paramiko.execute_command(
                status_kubelet_paramiko_vo)

            status_kubelet_data = RemoteControlResultVo(
                service_code=status_kubelet_code,
                service_type=service_type,
                service_func=systemd_status_service_func,
                service_name=status_kubelet_service_name,
                service_validate=bool(status_kubelet_data),
                service_result=status_kubelet_data)

            self.remote_control_working.create(
                service_type, status_kubelet_service_name, status_kubelet_data)

        except KeyError as ex:
            log.error('RemoteControlK8s :: status_kubelet :: ' + str(ex))

        return status_kubelet_data

    def get_join_command(self, service_type: str) -> RemoteControlResultVo:
        get_join_command_result_vo: RemoteControlResultVo

        try:
            get_join_command_meta = self.remote_control_k8s_meta['get_join_command']
            get_join_command_service_func = get_join_command_meta['service_func']
            get_join_command_service_command = get_join_command_meta['service_command']
            get_join_command_service_name = 'get_join_command'

            get_join_command_command = self.remote_control_paramiko.make_command(
                command=get_join_command_service_command,
                password=self.remote_control_session_info.password)

            get_join_command_paramiko_vo = RemoteControlParamikoVo(
                self.k8s_master_node_info['server'],
                self.k8s_master_node_info['port'],
                self.k8s_master_node_info['username'],
                self.k8s_master_node_info['password'],
                get_join_command_command)

            get_join_command_code, get_join_command_data = self.remote_control_paramiko.execute_command(
                get_join_command_paramiko_vo)

            get_join_command_result_vo = RemoteControlResultVo(
                service_code=get_join_command_code,
                service_type=service_type,
                service_func=get_join_command_service_func,
                service_name=get_join_command_service_name,
                service_validate=bool(get_join_command_data),
                service_result=get_join_command_data.replace('\n', ''))

            self.remote_control_working.create(
                service_type, get_join_command_service_name, get_join_command_result_vo)

        except KeyError as ex:
            log.error('RemoteControlK8s :: get_join_token :: ' + str(ex))

        return get_join_command_result_vo

    def join_worker_node(self, service_type: str, value: str) -> RemoteControlResultVo:
        join_worker_node_data: RemoteControlResultVo

        try:
            join_worker_node_meta = self.remote_control_k8s_meta['join_worker_node']
            join_worker_node_service_func = join_worker_node_meta['service_func']
            join_worker_node_service_command = join_worker_node_meta['service_command']
            join_worker_node_service_name = 'join_worker_node'

            join_worker_node_command = self.remote_control_paramiko.make_command(
                command=join_worker_node_service_command,
                password=self.remote_control_session_info.password,
                value=value)

            join_worker_node_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=join_worker_node_command)

            join_worker_node_code, join_worker_node_result = self.remote_control_paramiko.execute_invoke_shell(
                join_worker_node_vo, service_type, join_worker_node_service_name)

            join_worker_node_data = RemoteControlResultVo(
                service_code=join_worker_node_code,
                service_type=service_type,
                service_func=join_worker_node_service_func,
                service_name=join_worker_node_service_name,
                service_validate=bool(join_worker_node_result),
                service_result=join_worker_node_result)

            self.remote_control_working.create(
                service_type, join_worker_node_service_name, join_worker_node_data)

        except KeyError as ex:
            log.error('RemoteControlK8s :: join_worker_node :: ' + str(ex))

        return join_worker_node_data
