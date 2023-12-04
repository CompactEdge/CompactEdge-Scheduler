from typing import Union

from utils.logger import Log as log

from ..vo.remote_control_sessions_vo import RemoteControlSessionsVo

from . import REMOTE_CONTROL_SESSION_INFO


class RemoteControlSessions():

    def __init__(self):
        self.remote_control_session_info: RemoteControlSessionsVo = REMOTE_CONTROL_SESSION_INFO
        
    def init(self) -> Union[int, str]:
        try:
            self.remote_control_session_info.server = ''
            self.remote_control_session_info.port = ''
            self.remote_control_session_info.username = ''
            self.remote_control_session_info.password = ''
            
        except KeyError as ex:
            log.error('RemoteControlSessions :: init ' + str(ex))

    def create(self, server='', port='22', username='', password=''):
        try:
            self.remote_control_session_info.server = server
            self.remote_control_session_info.port = port
            self.remote_control_session_info.username = username
            self.remote_control_session_info.password = password

        except KeyError as ex:
            log.error('RemoteControlSessions :: create ' + str(ex))
            
    def validate_sessions(self, vo: RemoteControlSessionsVo) -> bool:
        validate: bool
        
        try:
            validate = bool(vo.server and vo.port and vo.username and vo.password)
            
        except KeyError as ex:
            log.error('validate_sessions :: create ' + str(ex))
            
        return validate
    
    def get(self) -> RemoteControlSessionsVo:
        get_data: dict
        
        try:
            get_data = self.remote_control_session_info
            
        except KeyError as ex:
            get_data = {}
            log.error('RemoteControlSessions :: get :: ' + str(ex))
            
        return get_data