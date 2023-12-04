import time
from utils.logger import Log as log

from .modules.remote_control_paramiko import RemoteControlParamiko
from .modules.remote_control_working import RemoteControlWorking

from .vo.remote_control_result_vo import RemoteControlResultVo
from .vo.remote_control_paramiko_vo import RemoteControlParamikoVo

from .meta import REMOTE_CONTROL_META


class RemoteControlCommon():

    def __init__(self):
        self.service_type = 'validate_node_health_management'

        self.remote_control_working = RemoteControlWorking()
        self.remote_control_paramiko = RemoteControlParamiko()

        self.remote_control_common_meta = REMOTE_CONTROL_META['remote_control_common_meta']
        self.remote_contorl_systemd_meta = REMOTE_CONTROL_META['remote_contorl_systemd_meta']

    def validate_node(self, service_type: str, server='', port='', username='', password='') -> RemoteControlResultVo:
        validate_node_data: RemoteControlResultVo

        try:
            validate_node_meta = self.remote_control_common_meta['validate_node']

            service_type = self.service_type
            service_func = validate_node_meta['service_func']
            service_name = 'validate_node'
            service_command = validate_node_meta['service_command']

            validate_node_paramiko_vo: RemoteControlParamikoVo = RemoteControlParamikoVo(
                server=server,
                port=port,
                username=username,
                password=password,
                command=self.remote_control_paramiko.make_command(
                    command=service_command, password=password)
            )

            commnad_exec_code, command_exec_result = self.remote_control_paramiko.execute_command(
                validate_node_paramiko_vo)
            hostname = command_exec_result.replace('\n', '')

            validate_node_data = RemoteControlResultVo(
                service_code=commnad_exec_code,
                service_type=service_type,
                service_func=service_func,
                service_name=service_name,
                service_validate=False if not command_exec_result else True,
                service_result=hostname
            )

            self.remote_control_working.create(
                service_type, service_name, validate_node_data)

        except KeyError as ex:
            log.error('validate_node :: ' + str(ex))

        return validate_node_data

    def validate_installed_apps(self, server='', port='', username='', password='') -> RemoteControlResultVo:
        validate_installed_apps_data: RemoteControlResultVo

        try:
            apps = ['docker', 'kubelet']

            systemd_status_meta = self.remote_contorl_systemd_meta['systemd_status']

            service_type = self.service_type
            service_func = systemd_status_meta['service_func']
            service_name = 'validate_installed_apps'
            service_command = systemd_status_meta['service_command']

            command_exec_list = list()
            for app in apps:
                validate_installed_apps_paramiko_vo = RemoteControlParamikoVo(
                    server=server,
                    port=port,
                    username=username,
                    password=password,
                    command=self.remote_control_paramiko.make_command(
                        command=service_command, password=password, app=app)
                )

                commnad_exec_code, command_exec_result = self.remote_control_paramiko.execute_command(
                    validate_installed_apps_paramiko_vo)

                command_exec_list.append({
                    'app_code': commnad_exec_code,
                    'app_type': '',
                    'app_name': app,
                    'app_validate': True if not command_exec_result else False,
                    'app_result': command_exec_result
                })

                time.sleep(0.1)

            validate_installed_apps_data = RemoteControlResultVo(
                service_code=200,
                service_type=service_type,
                service_func=service_func,
                service_name=service_name,
                service_validate=False not in list(
                    x['app_validate'] for x in command_exec_list),
                service_result=command_exec_list
            )

            self.remote_control_working.create(
                service_type, service_name, validate_installed_apps_data)

        except Exception as ex:
            log.error(ex)

        return validate_installed_apps_data
