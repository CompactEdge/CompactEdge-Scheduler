from typing import Union

from utils.logger import Log as log

from . import REMOTE_CONTROL_WORKING_INFO


class RemoteControlWorking():

    def __init__(self):
        self.remote_control_working_info: dict = REMOTE_CONTROL_WORKING_INFO

    def init(self):
        try:
            self.remote_control_working_info.clear()

        except KeyError as ex:
            log.error('RemoteControlWorking :: init :: ' + str(ex))

    def update(self, service_type, service_name, data):
        try:
            service_index = str(
                len(self.remote_control_working_info[service_type].keys())-1)

            self.remote_control_working_info[service_type][service_index][service_name] = data

            # print(self.remote_control_working_info[service_type])

        except KeyError as ex:
            log.error('RemoteControlWorking :: update :: ' + str(ex))

    def create(self, service_type, service_name, data):
        try:
            remote_control_working_info_keys = self.remote_control_working_info.keys()
            if service_type not in remote_control_working_info_keys:
                self.remote_control_working_info[service_type] = {}

            service_index = str(len(self.remote_control_working_info[service_type].keys()))

            self.remote_control_working_info[service_type][service_index] = {
                service_name: data
            }

            # self.remote_control_working_info[service_type][service_index][service_name] = data

        except KeyError as ex:
            log.error('RemoteControlWorking :: create :: ' + str(ex))

    def get(self) -> Union[int, dict]:
        get_data: dict

        try:
            get_data = self.remote_control_working_info

        except KeyError as ex:
            get_data = {}
            log.error('RemoteControlWorking :: get :: ' + str(ex))

        return get_data
