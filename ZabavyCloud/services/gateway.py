from fastapi import HTTPException, status

import ZabavyCloud.repository as repository

from ..constants.collection import Collection
from ..constants.error import Error
from ..factories.gateway import GatewayFactory
from ..models.gateway import GatewayModel
from ..repository.repository import Repository


class GatewayService:
    def __init__(self, repository: Repository, factory: GatewayFactory = GatewayFactory()):
        self.repository: Repository = repository
        self.factory: GatewayFactory = factory

    def get_gateway(self, record: str = '', skip: int = 0, limit: int = 100) -> list:
        data: list = self.repository.read(
            collection=Collection.GATEWAY,
            record=record,
            skip=skip,
            limit=limit
        )
        return [self.factory(**model) for model in data]

    def create_gateway(self, model: GatewayModel) -> list:
        data = self.get_gateway()
        exists = list(filter(lambda x: x.platform == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.GATEWAY_ALREADY_EXISTS.value,
            )
        data = self.repository.create(
            collection=Collection.GATEWAY,
            data=model.dict()
        )
        return [self.factory(**data), ]

    def update_gateway(self, model: GatewayModel, record: str) -> list:
        data = self.get_gateway(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.GATEWAY_NOT_EXISTS.value,
            )
        data = self.get_gateway()
        exists = list(filter(lambda x: x.platform == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.GATEWAY_ALREADY_EXISTS.value,
            )
        data = self.repository.update(
            collection=Collection.GATEWAY,
            record=record,
            data=model.dict()
        )
        return [self.factory(**data), ]

    def delete_gateway(self, record: str, reason: str = '') -> list:
        data = self.get_gateway(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.GATEWAY_NOT_EXISTS.value,
            )
        data = self.repository.delete(
            collection=Collection.GATEWAY,
            record=record,
            reason=reason
        )
        return [self.factory(**data), ]


def build_service() -> GatewayService:
    return GatewayService(repository=repository.get(name='database'))
