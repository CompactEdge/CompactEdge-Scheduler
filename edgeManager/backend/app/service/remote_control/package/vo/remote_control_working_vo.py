from dataclasses import dataclass, field
from typing import Optional

from .remote_control_result_vo import RemoteControlResultVo


@dataclass
class ExecuteDefaultPreferencesManagement():
    ufw: RemoteControlResultVo
    swap: RemoteControlResultVo
    ip_forward: RemoteControlResultVo
    iptables: RemoteControlResultVo


@dataclass
class ExecuteDefaultPackageManagement():
    apt_update: RemoteControlResultVo
    apt_upgrade: RemoteControlResultVo
    apt_install: RemoteControlResultVo


@dataclass
class ValidateNodeHealthManagement():
    validate_node: RemoteControlResultVo
    validate_worker_node: RemoteControlResultVo
    validate_installed_apps: RemoteControlResultVo


@dataclass
class RemoteControlWorkingVo():
    validate_node_health_management: Optional[ValidateNodeHealthManagement] = field(
        init=False)
    execute_default_package_management: Optional[ExecuteDefaultPackageManagement] = field(
        init=False)
    execute_default_preferences_management: Optional[ExecuteDefaultPreferencesManagement] = field(
        init=False)
