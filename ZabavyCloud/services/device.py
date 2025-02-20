from fastapi import HTTPException, status

import ZabavyCloud.repository as repository

from ..constants.collection import Collection
from ..constants.error import Error
from ..factories.device import DeviceFactory
from ..models.device import DeviceModel
from ..repository.repository import Repository


class DeviceService:
    def __init__(self, repository: Repository, factory: DeviceFactory = DeviceFactory()):
        self.repository: Repository = repository
        self.factory: DeviceFactory = factory

    def get_device(self, record: str = '', skip: int = 0, limit: int = 100) -> list:
        data: list = self.repository.read(
            collection=Collection.DEVICE,
            record=record,
            skip=skip,
            limit=limit
        )
        return [self.factory(**model) for model in data]

    def create_device(self, model: DeviceModel) -> list:
        data = self.get_device()
        exists = list(filter(lambda x: x.platform == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.DEVICE_ALREADY_EXISTS.value,
            )
        data = self.repository.create(
            collection=Collection.DEVICE,
            data=model.dict()
        )
        return [self.factory(**data), ]

    def update_device(self, model: DeviceModel, record: str) -> list:
        data = self.get_device(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.DEVICE_NOT_EXISTS.value,
            )
        data = self.get_device()
        exists = list(filter(lambda x: x.platform == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.DEVICE_ALREADY_EXISTS.value,
            )
        data = self.repository.update(
            collection=Collection.DEVICE,
            record=record,
            data=model.dict()
        )
        return [self.factory(**data), ]

    def delete_device(self, record: str, reason: str = '') -> list:
        data = self.get_device(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.DEVICE_NOT_EXISTS.value,
            )
        data = self.repository.delete(
            collection=Collection.DEVICE,
            record=record,
            reason=reason
        )
        return [self.factory(**data), ]


def build_service() -> DeviceService:
    return DeviceService(repository=repository.get(name='database'))
