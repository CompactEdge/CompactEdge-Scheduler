from .package.remote_control_common import RemoteControlCommon
from .package.remote_control_docker import RemoteControlDocker
from .package.remote_control_k8s import RemoteControlK8s
from .package.remote_control_status import RemoteControlStatus
from .package.remote_control_ubuntu import RemoteControlUbuntu


class RemoteControl():

    def __init__(self):
        self.remote_control_common = RemoteControlCommon()
        self.remote_control_docker = RemoteControlDocker()
        self.remote_control_k8s = RemoteControlK8s()
        self.remote_control_status = RemoteControlStatus()
        self.remote_control_ubuntu = RemoteControlUbuntu()
