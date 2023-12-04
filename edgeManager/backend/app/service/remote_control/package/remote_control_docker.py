import json
import time
from flask import current_app

from utils.logger import Log as log

from .modules.remote_control_working import RemoteControlWorking
from .modules.remote_control_paramiko import RemoteControlParamiko

from .vo.remote_control_result_vo import RemoteControlResultVo
from .vo.remote_control_paramiko_vo import RemoteControlParamikoVo

from .meta import REMOTE_CONTROL_META
from .modules import REMOTE_CONTROL_SESSION_INFO


class RemoteControlDocker():

    def __init__(self):
        self.remote_control_working = RemoteControlWorking()
        self.remote_control_paramiko = RemoteControlParamiko()

        self.docker_versions = current_app.config["DOCKER_VERSIONS"]
        self.remote_control_apt_meta = REMOTE_CONTROL_META['remote_control_apt_meta']
        self.remote_control_docker_meta = REMOTE_CONTROL_META['remote_control_docker_meta']
        self.remote_contorl_systemd_meta = REMOTE_CONTROL_META['remote_contorl_systemd_meta']
        self.remote_control_session_info = REMOTE_CONTROL_SESSION_INFO

    def set_up_mkdir(self):
        try:
            set_up_mkdir_meta = self.remote_control_docker_meta['set_up_mkdir']
            set_up_mkdir_service_command = set_up_mkdir_meta['service_command']

            set_up_mkdir_command = self.remote_control_paramiko.make_command(
                command=set_up_mkdir_service_command,
                password=self.remote_control_session_info.password)

            set_up_mkdir_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=set_up_mkdir_command)

            self.remote_control_paramiko.execute_command(
                set_up_mkdir_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlDocker :: set_up_mkdir :: ' + str(ex))

    def set_up_gpg_key(self):
        try:
            set_up_gpg_key_meta = self.remote_control_docker_meta['set_up_gpg_key']
            set_up_gpg_key_service_command = set_up_gpg_key_meta['service_command']

            set_up_gpg_key_command = self.remote_control_paramiko.make_command(
                command=set_up_gpg_key_service_command,
                password=self.remote_control_session_info.password)

            set_up_gpg_key_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=set_up_gpg_key_command)

            self.remote_control_paramiko.execute_command(
                set_up_gpg_key_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlDocker :: set_up_gpg_key :: ' + str(ex))

    def set_up_repo_key(self):
        try:
            set_up_repo_key_meta = self.remote_control_docker_meta['set_up_repo_key']
            set_up_repo_key_service_command = set_up_repo_key_meta['service_command']

            set_up_repo_key_command = self.remote_control_paramiko.make_command(
                command=set_up_repo_key_service_command,
                password=self.remote_control_session_info.password)

            set_up_repo_key_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=set_up_repo_key_command)

            self.remote_control_paramiko.execute_command(
                set_up_repo_key_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlDocker :: set_up_repo_key :: ' + str(ex))

    def update_docker(self, service_type: str) -> RemoteControlResultVo:
        update_docker_result_vo: RemoteControlResultVo

        try:
            apt_update_meta = self.remote_control_apt_meta['apt_update']
            apt_update_service_func = apt_update_meta['service_func']
            apt_update_service_command = apt_update_meta['service_command']

            update_docker_service_name = 'update_docker'
            update_docker_command = self.remote_control_paramiko.make_command(
                command=apt_update_service_command,
                password=self.remote_control_session_info.password)
            update_docker_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=update_docker_command)

            update_docker_code, update_docker_data = \
                self.remote_control_paramiko.execute_invoke_shell(
                    update_docker_paramiko_vo, service_type, update_docker_service_name)

            update_docker_result_vo = RemoteControlResultVo(
                service_code=update_docker_code,
                service_type=service_type,
                service_func=apt_update_service_func,
                service_name=update_docker_service_name,
                service_validate=(
                    False if update_docker_code != 200 else True),
                service_result=update_docker_data)

            # self.remote_control_working.create(service_type, update_docker_service_name, update_docker_result_vo)

        except KeyError as ex:
            log.error('RemoteControldocker :: update_docker :: ' + str(ex))

        return update_docker_result_vo

    def install_docker(self, service_type: str) -> RemoteControlResultVo:
        install_docker_result_vo: RemoteControlResultVo

        try:
            apt_install_meta = self.remote_control_apt_meta['apt_install']
            apt_install_service_func = apt_install_meta['service_func']
            apt_install_service_command = apt_install_meta['service_command']

            install_docker_service_name = 'install_docker'
            install_docker_apps = self.docker_versions

            install_docker_command = self.remote_control_paramiko.make_command(
                command=apt_install_service_command,
                password=self.remote_control_session_info.password,
                apps=install_docker_apps)

            install_docker_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=install_docker_command)

            install_docker_code, install_docker_data = self.remote_control_paramiko.execute_invoke_shell(
                install_docker_paramiko_vo, service_type, install_docker_service_name)

            install_docker_result_vo = RemoteControlResultVo(
                service_code=install_docker_code,
                service_type=service_type,
                service_func=apt_install_service_func,
                service_name=install_docker_service_name,
                service_validate=(
                    False if install_docker_code != 200 else True),
                service_result=install_docker_data)

            # self.remote_control_working.create(service_type, install_docker_service_name, install_docker_result_vo)

        except KeyError as ex:
            log.error('RemoteControlDocker :: install_docker :: ' + str(ex))

        return install_docker_result_vo

    def mark_docker(self):
        try:
            apt_mark_meta = self.remote_control_apt_meta['apt_mark']
            apt_mark_service_command = apt_mark_meta['service_command']

            mark_docker_option = 'hold'
            mark_docker_app = 'docker.io'

            mark_docker_command = self.remote_control_paramiko.make_command(
                command=apt_mark_service_command,
                password=self.remote_control_session_info.password,
                option=mark_docker_option,
                apps=mark_docker_app)

            mark_docker_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=mark_docker_command)

            self.remote_control_paramiko.execute_command(
                mark_docker_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlDocker :: mark_docker :: ' + str(ex))

    def edit_cgroup_docker(self):
        try:
            edit_cgroup_docker_meta = self.remote_control_docker_meta['edit_cgroup_docker']
            edit_cgroup_docker_service_func = edit_cgroup_docker_meta['service_func']
            edit_cgroup_docker_service_command = edit_cgroup_docker_meta['service_command']
            edit_cgroup_docker_service_value = edit_cgroup_docker_meta['service_value']
            edit_cgroup_docker_name = 'edit_cgroup_docker'

            value = json.dumps(edit_cgroup_docker_service_value,
                               indent=2).replace('\"', '\\\"')

            edit_cgroup_docker_command = self.remote_control_paramiko.make_command(
                command=edit_cgroup_docker_service_command,
                password=self.remote_control_session_info.password,
                value=value)

            edit_cgroup_docker_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=edit_cgroup_docker_command)

            self.remote_control_paramiko.execute_command(
                edit_cgroup_docker_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlDocker :: edit_cgroup_docker :: ' + str(ex))

    def daemon_reload_docker(self):
        try:
            systemd_daemon_reload_meta = self.remote_contorl_systemd_meta['systemd_daemon_reload']
            systemd_daemon_reload_service_command = systemd_daemon_reload_meta['service_command']

            daemon_reload_docker_command = self.remote_control_paramiko.make_command(
                command=systemd_daemon_reload_service_command,
                password=self.remote_control_session_info.password)

            daemon_reload_docker_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=daemon_reload_docker_command)

            self.remote_control_paramiko.execute_command(
                daemon_reload_docker_vo)

        except KeyError as ex:
            log.error('RemoteControlDocker :: daemon_reload_docker :: ' + str(ex))

    def restart_docker(self):
        try:
            systemd_restart_meta = self.remote_contorl_systemd_meta['systemd_restart']
            systemd_restart_service_command = systemd_restart_meta['service_command']

            restart_docker_app = 'docker'

            restart_docker_command = self.remote_control_paramiko.make_command(
                command=systemd_restart_service_command,
                password=self.remote_control_session_info.password,
                app=restart_docker_app)

            restart_docker_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=restart_docker_command)

            self.remote_control_paramiko.execute_command(
                restart_docker_paramiko_vo)
            time.sleep(10)

        except KeyError as ex:
            log.error('RemoteControlDocker :: restart_docker :: ' + str(ex))

    def enable_docker(self):
        try:
            systemd_enable_meta = self.remote_contorl_systemd_meta['systemd_enable']
            systemd_enable_service_command = systemd_enable_meta['service_command']

            enable_docker_app = 'docker'

            enable_docker_command = self.remote_control_paramiko.make_command(
                command=systemd_enable_service_command,
                password=self.remote_control_session_info.password,
                app=enable_docker_app)

            enable_docker_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=enable_docker_command)

            self.remote_control_paramiko.execute_command(
                enable_docker_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlDocker :: enable_docker :: ' + str(ex))

    def status_docker(self, service_type: str) -> RemoteControlResultVo:
        status_docker_result_vo: RemoteControlResultVo

        try:
            systemd_docker_meta = self.remote_contorl_systemd_meta['systemd_status']
            systemd_docker_service_func = systemd_docker_meta['service_func']
            systemd_docker_service_command = systemd_docker_meta['service_command']

            status_docker_service_name = 'status_docker'
            status_docker_app = 'docker'

            status_docker_command = self.remote_control_paramiko.make_command(
                command=systemd_docker_service_command,
                password=self.remote_control_session_info.password,
                app=status_docker_app)

            status_docker_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=status_docker_command)

            status_docker_code, status_docker_data = self.remote_control_paramiko.execute_command(
                status_docker_paramiko_vo)

            status_docker_result_vo = RemoteControlResultVo(
                service_code=status_docker_code,
                service_type=service_type,
                service_func=systemd_docker_service_func,
                service_name=status_docker_service_name,
                service_validate='Active: active (running)' in status_docker_data,
                service_result=status_docker_data)

            self.remote_control_working.create(
                service_type, status_docker_service_name, status_docker_result_vo)

        except KeyError as ex:
            log.error('RemoteControlDocker :: status_docker :: ' + str(ex))

        return status_docker_result_vo

    def status_cgroup_docker(self, service_type: str) -> RemoteControlResultVo:
        status_cgroup_docker_result_vo: RemoteControlResultVo

        try:
            status_cgroup_docker_meta = self.remote_control_docker_meta['status_cgroup_docker']

            status_cgroup_docker_service_func = status_cgroup_docker_meta['service_func']
            status_cgroup_docker_service_command = status_cgroup_docker_meta['service_command']
            status_cgroup_docker_service_name = 'status_cgroup_docker'

            status_cgroup_docker_command = self.remote_control_paramiko.make_command(
                command=status_cgroup_docker_service_command,
                password=self.remote_control_session_info.password)

            remote_control_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=status_cgroup_docker_command)

            status_cgroup_docker_code, status_cgroup_docker_data = self.remote_control_paramiko.execute_command(
                remote_control_paramiko_vo)

            status_cgroup_docker_result_vo = RemoteControlResultVo(
                service_code=status_cgroup_docker_code,
                service_type=service_type,
                service_func=status_cgroup_docker_service_func,
                service_name=status_cgroup_docker_service_name,
                service_validate='Cgroup Driver: systemd' in status_cgroup_docker_data,
                service_result=status_cgroup_docker_data)

            self.remote_control_working.create(
                service_type, status_cgroup_docker_service_name, status_cgroup_docker_result_vo)

        except KeyError as ex:
            log.error('RemoteControlDocker :: status_cgroup_docker :: ' + str(ex))

        return status_cgroup_docker_result_vo
