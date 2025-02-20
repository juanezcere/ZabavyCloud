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
