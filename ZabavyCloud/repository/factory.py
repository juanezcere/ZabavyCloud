from ..utils.factory_utils import Factory
from .file_repository import FileRepository
from .memory_repository import MemoryRepository
from .mongo_repository import MongoRepository


class RepositoryFactory(Factory):

    factories: dict = {
        'memory': MemoryRepository,
        'file': FileRepository,
        'mongo': MongoRepository,
        # 'sqlite': SqliteRepository,
        # 'mysql': MysqlRepository,
    }

    def create(self, factory_type: str, *args, **kwargs):
        """
        ? Creates a repository of the given type.
        """
        if factory_type in self.factories:
            return self.factories[factory_type].RepositoryBuilder(*args, **kwargs)
        else:
            raise ValueError(f'Unknown factory type: {factory_type}.')
