from fastapi import HTTPException, status

from ..constants.error import Error
from ..factories.action import ActionFactory
from ..models.action import ActionModel
from ..repositories.action import ActionRepository


class ActionService:
    def __init__(self, repository: ActionRepository = ActionRepository(), factory: ActionFactory = ActionFactory()):
        self.repository: ActionRepository = repository
        self.factory: ActionFactory = factory

    def get_action(self, record: str = '', skip: int = 0, limit: int = 100) -> list:
        data: list = self.repository.get(record=record, skip=skip, limit=limit)
        return [self.factory(**model) for model in data]

    def create_action(self, model: ActionModel) -> list:
        data = self.repository.get()
        exists = list(filter(lambda x: x['platform'] == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.ACTION_ALREADY_EXISTS.value,
            )
        data = self.repository.create(model=model)
        return [self.factory(**data), ]

    def update_action(self, model: ActionModel, record: str) -> list:
        data = self.repository.get(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.ACTION_NOT_EXISTS.value,
            )
        data = self.repository.get()
        exists = list(filter(lambda x: x['platform'] == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.ACTION_ALREADY_EXISTS.value,
            )
        data = self.repository.update(model=model, record=record)
        return [self.factory(**data), ]

    def delete_action(self, record: str, reason: str = '') -> list:
        data = self.repository.get(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.ACTION_NOT_EXISTS.value,
            )
        data = self.repository.delete(record=record, reason=reason)
        return [self.factory(**data), ]
