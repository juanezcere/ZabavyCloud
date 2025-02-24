
from .factory import RepositoryFactory
from .repository import Repository

factory: RepositoryFactory = RepositoryFactory()
repositories: dict[str, Repository] = {}


def get(name: str) -> Repository:
    global repositories
    if name in repositories:
        return repositories[name]
    return None


def create(repository: str, name: str, *args, **kwargs) -> Repository:
    global repositories, factory
    repositories[name] = factory.create(
        factory_type=repository, *args, **kwargs)
    return repositories[name]


def ls() -> list[str]:
    global repositories
    return list(repositories.keys())
