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
        query = {'_id': record} if len(record) else {}
        data = mongo_collection.find(query).skip(skip).limit(limit)
        return [{**d, 'id': str(d['_id'])} for d in data]

    def create(self, collection: Collection, data: dict) -> dict:
        mongo_collection = self._get_collection(collection)
        result = mongo_collection.insert_one(data)
        new_id = str(result.inserted_id)
        data['id'] = new_id
        return data

    def update(self, collection: Collection, record: str, data: dict) -> dict:
        mongo_collection = self._get_collection(collection)
        try:
            record_id = ObjectId(record)
        except:
            record_id = record

        result = mongo_collection.replace_one({'_id': record_id}, data)
        if result.modified_count > 0:
            return data
        else:
            return None

    def delete(self, collection: Collection, record: str, reason: str) -> dict:
        mongo_collection = self._get_collection(collection)
        try:
            record_id = ObjectId(record)
        except:
            record_id = record
        deleted_data = mongo_collection.find_one({'_id': record_id})
        result = mongo_collection.delete_one({'_id': record_id})
        if result.deleted_count > 0:
            return deleted_data
        else:
            return None
