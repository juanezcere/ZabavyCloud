from fastapi import HTTPException, status

import ZabavyCloud.repository as repository

from ..constants.collection import Collection
from ..constants.error import Error
from ..factories.actuator import ActuatorFactory
from ..models.actuator import ActuatorModel
from ..repository.repository import Repository


class ActuatorService:
    def __init__(self, repository: Repository, factory: ActuatorFactory = ActuatorFactory()):
        self.repository: Repository = repository
        self.factory: ActuatorFactory = factory

    def get_actuator(self, record: str = '', skip: int = 0, limit: int = 100) -> list:
        data: list = self.repository.read(
            collection=Collection.ACTUATOR,
            record=record,
            skip=skip,
            limit=limit
        )
        return [self.factory(**model) for model in data]

    def create_actuator(self, model: ActuatorModel) -> list:
        data = self.get_actuator()
        exists = list(filter(lambda x: x.platform == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.ACTUATOR_ALREADY_EXISTS.value,
            )
        data = self.repository.create(
            collection=Collection.ACTUATOR,
            data=model.dict()
        )
        return [self.factory(**data), ]

    def update_actuator(self, model: ActuatorModel, record: str) -> list:
        data = self.get_actuator(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.ACTUATOR_NOT_EXISTS.value,
            )
        data = self.get_actuator()
        exists = list(filter(lambda x: x.platform == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.ACTUATOR_ALREADY_EXISTS.value,
            )
        data = self.repository.update(
            collection=Collection.ACTUATOR,
            record=record,
            data=model.dict()
        )
        return [self.factory(**data), ]

    def delete_actuator(self, record: str, reason: str = '') -> list:
        data = self.get_actuator(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.ACTUATOR_NOT_EXISTS.value,
            )
        data = self.repository.delete(
            collection=Collection.ACTUATOR,
            record=record,
            reason=reason
        )
        return [self.factory(**data), ]


def build_service() -> ActuatorService:
    return ActuatorService(repository=repository.get(name='database'))
