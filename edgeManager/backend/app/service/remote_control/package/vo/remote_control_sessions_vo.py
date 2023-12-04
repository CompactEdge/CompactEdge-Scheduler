from dataclasses import dataclass, field


@dataclass
class RemoteControlSessionsVo():
    server: str = field(init=False, default='')
    port: str = field(init=False, default='')
    username: str = field(init=False, default='')
    password: str = field(init=False, default='')
