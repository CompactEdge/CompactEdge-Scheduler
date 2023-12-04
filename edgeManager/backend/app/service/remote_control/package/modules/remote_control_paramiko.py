import time
import paramiko
from typing import Union

from utils.logger import Log as log

from .remote_control_working import RemoteControlWorking
from ..vo.remote_control_sessions_vo import RemoteControlSessionsVo
from ..vo.remote_control_paramiko_vo import RemoteControlParamikoVo

from . import REMOTE_CONTROL_SESSION_INFO, REMOTE_CONTROL_WORKING_INFO


class RemoteControlParamiko():

    def __init__(self):
        self.remote_control_session_info = REMOTE_CONTROL_SESSION_INFO
        self.remote_control_working_info = REMOTE_CONTROL_WORKING_INFO

        self.remote_control_working = RemoteControlWorking()

    def make_paramiko_vo(self, sessions_vo: RemoteControlSessionsVo, command: str) -> RemoteControlParamikoVo:
        remote_control_paramiko_vo: RemoteControlParamikoVo

        try:
            remote_control_paramiko_vo = RemoteControlParamikoVo(
                server=sessions_vo.server,
                port=sessions_vo.port,
                username=sessions_vo.username,
                password=sessions_vo.password,
                command=command)

        except KeyError as ex:
            log.error('RemoteControlParamiko :: make_paramiko_vo ::' + str(ex))

        return remote_control_paramiko_vo

    def make_command(self, command='', **kwargs: str) -> str:
        return command.format(**kwargs)

    def execute_invoke_shell(self, remote_control_paramiko_vo: RemoteControlParamikoVo, service_type: str, service_name: str) -> Union[int, str]:
        execute_invoke_shell_code: int
        execute_invoke_shell_data: str

        ssh_client: paramiko.SSHClient
        ssh_channel: paramiko.Channel

        try:
            service_func = 'execute_invoke_shell'

            server = remote_control_paramiko_vo.server
            port = remote_control_paramiko_vo.port
            username = remote_control_paramiko_vo.username
            password = remote_control_paramiko_vo.password
            command = remote_control_paramiko_vo.command

            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            ssh_client.connect(server, port, username, password)

            ssh_channel = ssh_client.invoke_shell()
            ssh_channel.settimeout(9999)
            ssh_channel.send(command)
            ssh_channel.send('exit\n')

            stdout = ''
            self.remote_control_working.create(
                service_type,
                service_name,
                {'service_func': service_func, 'service_result': stdout})

            limited_retry_count = 180
            while limited_retry_count >= 0:
                if ssh_channel.recv_ready():
                    stdout += ssh_channel.recv(1024).decode('utf-8')
                    self.remote_control_working.update(
                        service_type,
                        service_name,
                        {'service_func': service_func, 'service_result': stdout})

                    execute_invoke_shell_code = 200
                    execute_invoke_shell_data = stdout
                elif ssh_channel.exit_status_ready():
                    time.sleep(5)
                    break
                else:
                    time.sleep(1)
                    limited_retry_count -= 1

            stderr = ''
            while ssh_channel.recv_stderr_ready():
                time.sleep(1)
                stderr += ssh_channel.recv_stderr(1024).decode('utf-8')
                self.remote_control_working.update(
                    service_type,
                    service_name,
                    {'service_func': service_func, 'service_result': stderr})

                execute_invoke_shell_code = 200
                execute_invoke_shell_data = stderr

        except paramiko.SSHException as ex:
            execute_invoke_shell_code = 500
            execute_invoke_shell_data = str(ex)
            log.error('execute_invoke_shell :: ' + str(ex))
        except Exception as ex:
            execute_invoke_shell_code = 500
            execute_invoke_shell_data = str(ex)
            log.error('execute_invoke_shell :: ' + str(ex))
        finally:
            ssh_channel.close()
            ssh_client.close()

        return execute_invoke_shell_code, execute_invoke_shell_data

    def execute_command(self, remote_control_paramiko_vo: RemoteControlParamikoVo) -> Union[int, str]:
        execute_command_code: int
        execute_command_data: str

        try:
            server = remote_control_paramiko_vo.server
            port = remote_control_paramiko_vo.port
            username = remote_control_paramiko_vo.username
            password = remote_control_paramiko_vo.password
            command = remote_control_paramiko_vo.command

            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            ssh_client.connect(server, port, username, password)

            stdin, stdout, stderr = ssh_client.exec_command(command)

            lines = stdout.readlines()

            data = ''
            for line in lines:
                data += line

            execute_command_code = 200
            execute_command_data = data

        except paramiko.SSHException as ex:
            log.error('execute_command :: ' + str(ex))
            execute_command_code = 500
            execute_command_data = str(ex)
        except Exception as ex:
            log.error('execute_command :: ' + str(ex))
            execute_command_code = 500
            execute_command_data = str(ex)
        finally:
            ssh_client.close()

        return execute_command_code, execute_command_data
