from dataclasses import dataclass


@dataclass
class RemoteControlParamikoVo():
    server: str
    port: str
    username: str
    password: str
    command: str
