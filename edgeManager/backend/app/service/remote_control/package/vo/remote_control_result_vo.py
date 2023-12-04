from dataclasses import dataclass


@dataclass
class RemoteControlResultVo():
    service_code: int
    service_type: str
    service_func: str
    service_name: str
    service_validate: bool
    service_result: object
