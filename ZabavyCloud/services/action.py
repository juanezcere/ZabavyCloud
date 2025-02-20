from fastapi import HTTPException, status

import ZabavyCloud.repository as repository

from ..constants.collection import Collection
from ..constants.error import Error
from ..factories.action import ActionFactory
from ..models.action import ActionModel
from ..repository.repository import Repository


class ActionService:
    def __init__(self, repository: Repository, factory: ActionFactory = ActionFactory()):
        self.repository: Repository = repository
        self.factory: ActionFactory = factory

    def get_action(self, record: str = '', skip: int = 0, limit: int = 100) -> list:
        data: list = self.repository.read(
            collection=Collection.ACTION, record=record, skip=skip, limit=limit)
        return [self.factory(**model) for model in data]

    def create_action(self, model: ActionModel) -> list:
        data = self.get_action()
        exists = list(filter(lambda x: x.platform == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.ACTION_ALREADY_EXISTS.value,
            )
        data = self.repository.create(
            collection=Collection.ACTION, data=model.dict())
        return [self.factory(**data), ]

    def update_action(self, model: ActionModel, record: str) -> list:
        data = self.get_action(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.ACTION_NOT_EXISTS.value,
            )
        data = self.get_action()
        exists = list(filter(lambda x: x.platform == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.ACTION_ALREADY_EXISTS.value,
            )
        data = self.repository.update(
            collection=Collection.ACTION, record=record, data=model.dict())
        return [self.factory(**data), ]

    def delete_action(self, record: str, reason: str = '') -> list:
        data = self.get_action(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.ACTION_NOT_EXISTS.value,
            )
        data = self.repository.delete(
            collection=Collection.ACTION, record=record, reason=reason)
        return [self.factory(**data), ]


def build_service() -> ActionService:
    return ActionService(repository=repository.get(name='database'))
