from fastapi import HTTPException, status

import ZabavyCloud.repository as repository

from ..constants.collection import Collection
from ..constants.error import Error
from ..factories.variable import VariableFactory
from ..models.variable import VariableModel
from ..repository.repository import Repository


class VariableService:
    def __init__(self, repository: Repository, factory: VariableFactory = VariableFactory()):
        self.repository: Repository = repository
        self.factory: VariableFactory = factory

    def get_variable(self, record: str = '', skip: int = 0, limit: int = 100) -> list:
        data: list = self.repository.read(
            collection=Collection.VARIABLE,
            record=record,
            skip=skip,
            limit=limit
        )
        return [self.factory(**model) for model in data]

    def create_variable(self, model: VariableModel) -> list:
        data = self.get_variable()
        exists = list(filter(lambda x: x.platform == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.VARIABLE_ALREADY_EXISTS.value,
            )
        data = self.repository.create(
            collection=Collection.VARIABLE,
            data=model.dict()
        )
        return [self.factory(**data), ]

    def update_variable(self, model: VariableModel, record: str) -> list:
        data = self.get_variable(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.VARIABLE_NOT_EXISTS.value,
            )
        data = self.get_variable()
        exists = list(filter(lambda x: x.platform ==
                      model.platform and x.uid != record, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.VARIABLE_ALREADY_EXISTS.value,
            )
        data = self.repository.update(
            collection=Collection.VARIABLE,
            record=record,
            data=model.dict()
        )
        return [self.factory(**data), ]

    def delete_variable(self, record: str, reason: str = '') -> list:
        data = self.get_variable(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.VARIABLE_NOT_EXISTS.value,
            )
        data = self.repository.delete(
            collection=Collection.VARIABLE,
            record=record,
            reason=reason
        )
        return [self.factory(**data), ]


def build_service() -> VariableService:
    return VariableService(repository=repository.get(name='database'))
