from ..utils.builder_utils import Builder
from .factory import RepositoryFactory
from .repository import Repository
from .file import File


builder: Builder | None = None
factory: RepositoryFactory = RepositoryFactory()
repositories: dict[str, Repository] = {}


def get(name: str) -> Repository:
    global repositories
    if name in repositories:
        return repositories[name]
    return None


def create(repository: str, name: str) -> Builder:
    global builder
    builder = factory.create(factory_type=repository)
    builder.name(name)
    return builder


def set_file(name: str, file: File) -> Builder:
    global builder
    if builder.name == name:
        builder.path(file.path)
        builder.ext(file.ext)
    return builder


def set_host(name: str, host: str = 'localhost', port: int = 27017) -> Builder:
    global builder
    if builder.name == name:
        builder.host(host)
        builder.port(port)
    return builder


def set_auth(name: str, username: str = '', password: str = '') -> Builder:
    global builder
    if builder.name == name:
        builder.username(username)
        builder.password(password)
    return builder


def set_database(name: str, database: str) -> Builder:
    global builder
    if builder.name == name:
        builder.database(database)
    return builder


def set_url(name: str, url: str) -> Builder:
    global builder
    if builder.name == name:
        builder.url(url)
    return builder


def set_headers(name: str, headers: dict) -> Builder:
    global builder
    if builder.name == name:
        builder.headers(headers)
    return builder


def build(name: str) -> Repository:
    global builder, repositories
    if not name in repositories:
        repositories[name]: Repository = builder.build()
    return repositories[name]


def ls() -> list[str]:
    global repositories
    return list(repositories.keys())
