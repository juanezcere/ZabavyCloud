from fastapi import HTTPException, status

import ZabavyCloud.repository as repository

from ..constants.collection import Collection
from ..constants.error import Error
from ..factories.sensor import SensorFactory
from ..models.sensor import SensorModel
from ..repository.repository import Repository


class SensorService:
    def __init__(self, repository: Repository, factory: SensorFactory = SensorFactory()):
        self.repository: Repository = repository
        self.factory: SensorFactory = factory

    def get_sensor(self, record: str = '', skip: int = 0, limit: int = 100) -> list:
        data: list = self.repository.read(
            collection=Collection.SENSOR,
            record=record,
            skip=skip,
            limit=limit
        )
        return [self.factory(**model) for model in data]

    def create_sensor(self, model: SensorModel) -> list:
        data = self.get_sensor()
        exists = list(filter(lambda x: x.platform == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.SENSOR_ALREADY_EXISTS.value,
            )
        data = self.repository.create(
            collection=Collection.SENSOR,
            data=model.dict()
        )
        return [self.factory(**data), ]

    def update_sensor(self, model: SensorModel, record: str) -> list:
        data = self.get_sensor(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.SENSOR_NOT_EXISTS.value,
            )
        data = self.get_sensor()
        exists = list(filter(lambda x: x.platform == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.SENSOR_ALREADY_EXISTS.value,
            )
        data = self.repository.update(
            collection=Collection.SENSOR,
            record=record,
            data=model.dict()
        )
        return [self.factory(**data), ]

    def delete_sensor(self, record: str, reason: str = '') -> list:
        data = self.get_sensor(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.SENSOR_NOT_EXISTS.value,
            )
        data = self.repository.delete(
            collection=Collection.SENSOR,
            record=record,
            reason=reason
        )
        return [self.factory(**data), ]


def build_service() -> SensorService:
    return SensorService(repository=repository.get(name='database'))
