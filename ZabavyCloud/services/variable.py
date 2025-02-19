from fastapi import HTTPException, status

from ..constants.error import Error
from ..factories.variable import VariableFactory
from ..models.variable import VariableModel
from ..repositories.variable import VariableRepository


class VariableService:
    def __init__(self, repository: VariableRepository = VariableRepository(), factory: VariableFactory = VariableFactory()):
        self.repository: VariableRepository = repository
        self.factory: VariableFactory = factory

    def get_variable(self, record: str = '', skip: int = 0, limit: int = 100) -> list:
        data: list = self.repository.get(record=record, skip=skip, limit=limit)
        return [self.factory(**model) for model in data]

    def create_variable(self, model: VariableModel) -> list:
        data = self.repository.get()
        exists = list(filter(lambda x: x['platform'] == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.VARIABLE_ALREADY_EXISTS.value,
            )
        data = self.repository.create(model=model)
        return [self.factory(**data), ]

    def update_variable(self, model: VariableModel, record: str) -> list:
        data = self.repository.get(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.VARIABLE_NOT_EXISTS.value,
            )
        data = self.repository.get()
        exists = list(filter(lambda x: x['platform'] == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.VARIABLE_ALREADY_EXISTS.value,
            )
        data = self.repository.update(model=model, record=record)
        return [self.factory(**data), ]

    def delete_variable(self, record: str, reason: str = '') -> list:
        data = self.repository.get(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.VARIABLE_NOT_EXISTS.value,
            )
        data = self.repository.delete(record=record, reason=reason)
        return [self.factory(**data), ]
