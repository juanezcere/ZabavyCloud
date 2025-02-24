from ..constants.collection import Collection
from ..utils.uuid_utils import generate_id
from .repository import Repository


class MemoryRepository(Repository):
    """
    Memory repository implementation based on python dicts.
    """

    def __init__(self):
        self.__data = {}

    def read(self, collection: Collection, record: str, skip: int = 0, limit: int = 100) -> list:
        if collection not in self.__data:
            return []
        if len(record):
            return list(filter(lambda x: x['uid'] == record, self.__data[collection]))
        return self.__data[collection][skip:skip + limit]

    def create(self, collection: Collection, data: dict) -> dict:
        if collection not in self.__data:
            self.__data[collection] = []
        if not data:
            raise ValueError("Data is empty.")
        new_id = generate_id()
        data['uid'] = new_id
        self.__data[collection].append(data)
        return data

    def update(self, collection: Collection, record: str, data: dict) -> dict:
        if collection not in self.__data:
            return None
        saved = self.read(collection=collection, record=record)
        if not len(saved):
            return None
        saved = saved[0]
        self.__data[collection].remove(saved)
        data['uid'] = record
        self.__data[collection].append(data)
        return data

    def delete(self, collection: Collection, record: str, reason: str) -> dict:
        if collection not in self.__data:
            return None
        data = self.read(collection=collection, record=record)
        if not len(data):
            return None
        data = data[0]
        self.__data[collection].remove(data)
        return data
