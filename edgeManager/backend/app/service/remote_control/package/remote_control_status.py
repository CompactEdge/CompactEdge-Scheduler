from typing import Union

from utils.logger import Log as log

from .modules.remote_control_working import RemoteControlWorking
from .modules.remote_control_sessions import RemoteControlSessions

from .vo.remote_control_result_vo import RemoteControlResultVo
from .vo.remote_control_sessions_vo import RemoteControlSessionsVo


class RemoteControlStatus():

    def __init__(self):
        self.remote_control_working = RemoteControlWorking()
        self.remote_control_sessions = RemoteControlSessions()

    def find_by_working(self, service_type='') -> Union[int, dict]:
        find_by_working_code: int
        find_by_working_data: str

        try:
            find_by_working_code = 200
            find_by_working_data = self.remote_control_working.get()[
                service_type]

        except KeyError as ex:
            log.error('RemoteControlStatus :: find_by_working :: ' + str(ex))
            find_by_working_code = 500
            find_by_working_data = {}

        return find_by_working_code, find_by_working_data

    def init_working(self, service_type: str) -> RemoteControlResultVo:
        service_func = 'execute_command'
        service_name = 'init_working'

        init_working_data: RemoteControlResultVo

        self.remote_control_working.init()

        init_working_data = RemoteControlResultVo(
            service_code=200,
            service_type=service_type,
            service_func=service_func,
            service_name=service_name,
            service_validate=True,
            service_result='')

        return init_working_data

    def init_sessions(self, service_type: str) -> RemoteControlResultVo:
        service_func = 'execute_command'
        service_name = 'init_sessions'

        init_sessions_data: RemoteControlResultVo

        self.remote_control_sessions.init()

        init_sessions_data = RemoteControlResultVo(
            service_code=200,
            service_type=service_type,
            service_func=service_func,
            service_name=service_name,
            service_validate=True,
            service_result='')

        return init_sessions_data

    def create_sessions(self, **kwargs):
        get_sessions: RemoteControlSessionsVo
        validate_sessions: bool

        get_sessions = self.remote_control_sessions.get()
        validate_sessions = self.remote_control_sessions.validate_sessions(
            get_sessions)

        if not validate_sessions:
            self.remote_control_sessions.create(**kwargs)
