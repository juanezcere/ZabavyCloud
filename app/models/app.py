from dataclasses import dataclass, field
from os import getcwd, name
from platform import release, system

from ..utils.datetime_utils import now, strftime


@dataclass
class App:
    name: str
    version: str = '1.0.0'
    title: str = 'Zabavy'
    author: str = 'Juanez'
    description: str = 'App description'
    summary: str = 'App summary'
    icon: str = 'zabavy.ico'
    platform: str = name
    system: str = system()
    release: str = release()
    path: str = getcwd()
    start: float = 0.0
    host: str = '0.0.0.0'
    port: str = 8000
    api_version: str = '1.0.0'
    web_version: str = '1.0.0'
    paths: dict = field(default_factory=dict)

    @property
    def log_file(self) -> str:
        date: str = strftime(date=now(), format='%Y%m%d%H%M%S')
        return f"{self.name}_{self.version}_{date}.log"
