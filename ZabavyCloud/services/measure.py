from fastapi import HTTPException, status

import ZabavyCloud.repository as repository

from ..constants.error import Error
from ..factories.measure import MeasureFactory
from ..models.measure import MeasureModel
from ..repository.repository import Repository


class MeasureService:
    def __init__(self, repository: Repository, factory: MeasureFactory = MeasureFactory()):
        self.repository: Repository = repository
        self.factory: MeasureFactory = factory

    def get_measure(self, record: str = '', skip: int = 0, limit: int = 100) -> list:
        data: list = self.repository.get(record=record, skip=skip, limit=limit)
        return [self.factory(**model) for model in data]

    def create_measure(self, model: MeasureModel) -> list:
        data = self.repository.get()
        exists = list(filter(
            lambda x: x['device'] == model.device and x['timestamp'] == model.timestamp, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.MEASURE_ALREADY_EXISTS.value,
            )
        data = self.repository.create(model=model)
        return [self.factory(**data), ]

    def update_measure(self, model: MeasureModel, record: str) -> list:
        data = self.repository.get(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.MEASURE_NOT_EXISTS.value,
            )
        data = self.repository.get()
        exists = list(filter(lambda x: x['platform'] == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.MEASURE_ALREADY_EXISTS.value,
            )
        data = self.repository.update(model=model, record=record)
        return [self.factory(**data), ]

    def delete_measure(self, record: str, reason: str = '') -> list:
        data = self.repository.get(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.MEASURE_NOT_EXISTS.value,
            )
        data = self.repository.delete(record=record, reason=reason)
        return [self.factory(**data), ]


def build_service() -> MeasureService:
    return MeasureService(repository=repository.get(name='database'))
