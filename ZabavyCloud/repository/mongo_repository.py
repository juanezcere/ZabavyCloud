from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.collection import Collection as MongoCollection

from ..constants.collection import Collection
from .repository import Repository


class MongoRepository(Repository):
    def __init__(self, connection_string: str):
        self.client = MongoClient(connection_string)
        self.db = self.client.get_default_database()

    def _get_collection(self, collection: Collection) -> MongoCollection:
        """
        ? Obtains the MongoDB's collection indicated by the Collection class.
        """
        return self.db[collection.value]

    def read(self, collection: Collection, record: str, skip: int = 0, limit: int = 100) -> list:
        mongo_collection = self._get_collection(collection)
        query = {'_id': ObjectId(record)} if len(record) else {}
        mongo_data = mongo_collection.find(query).skip(skip).limit(limit)
        data: list = []
        for register in mongo_data:
            register = {
                'uid': str(register['_id']),
                **register,
            }
            del register['_id']
            data.append(register)
        return data

    def create(self, collection: Collection, data: dict) -> dict:
        mongo_collection = self._get_collection(collection)
        del data['uid']
        result = mongo_collection.insert_one(data)
        new_id = str(result.inserted_id)
        data['uid'] = new_id
        del data['_id']
        return data

    def update(self, collection: Collection, record: str, data: dict) -> dict:
        mongo_collection = self._get_collection(collection)
        del data['uid']
        result = mongo_collection.find_one_and_replace(
            {'_id': ObjectId(record)}, data)
        data['uid'] = record
        return data

    def delete(self, collection: Collection, record: str, reason: str) -> dict:
        mongo_collection = self._get_collection(collection)
        result = mongo_collection.find_one_and_delete(
            {'_id': ObjectId(record)})
        del result['_id']
        result['uid'] = record
        return result
