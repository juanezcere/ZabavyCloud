from dataclasses import dataclass, field
from os import name

from .utils.datetime_utils import now, strftime
from .utils.path_utils import getcwd
from .utils.platform_utils import release, system


@dataclass
class App:
    name: str
    title: str = 'Zabavy'
    icon: str = 'zabavy.ico'
    author: str = 'Juanez'
    version: str = '1.0.0'
    description: str = 'App description'
    summary: str = 'App summary'
    platform: str = name
    system: str = system()
    release: str = release()
    path: str = getcwd()
    host: str = '0.0.0.0'
    api_version: str = '1.0.0'
    api_port: int = 8000
    web_version: str = '1.0.0'
    web_port: int = 3000
    start: float = 0.0
    paths: dict = field(default_factory=dict)

    @property
    def log_file(self) -> str:
        date: str = strftime(date=now(), fmt='%Y%m%d%H%M%S')
        return f"{self.name}_{self.version}_{date}.log"
