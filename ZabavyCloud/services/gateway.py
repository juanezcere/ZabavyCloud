from fastapi import HTTPException, status

from ..constants.error import Error
from ..factories.gateway import GatewayFactory
from ..models.gateway import GatewayModel
from ..repositories.gateway import GatewayRepository


class GatewayService:
    def __init__(self, repository: GatewayRepository = GatewayRepository(), factory: GatewayFactory = GatewayFactory()):
        self.repository: GatewayRepository = repository
        self.factory: GatewayFactory = factory

    def get_gateway(self, record: str = '', skip: int = 0, limit: int = 100) -> list:
        data: list = self.repository.get(record=record, skip=skip, limit=limit)
        return [self.factory(**model) for model in data]

    def create_gateway(self, model: GatewayModel) -> list:
        data = self.repository.get()
        exists = list(filter(lambda x: x['platform'] == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.GATEWAY_ALREADY_EXISTS.value,
            )
        data = self.repository.create(model=model)
        return [self.factory(**data), ]

    def update_gateway(self, model: GatewayModel, record: str) -> list:
        data = self.repository.get(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.GATEWAY_NOT_EXISTS.value,
            )
        data = self.repository.get()
        exists = list(filter(lambda x: x['platform'] == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.GATEWAY_ALREADY_EXISTS.value,
            )
        data = self.repository.update(model=model, record=record)
        return [self.factory(**data), ]

    def delete_gateway(self, record: str, reason: str = '') -> list:
        data = self.repository.get(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.GATEWAY_NOT_EXISTS.value,
            )
        data = self.repository.delete(record=record, reason=reason)
        return [self.factory(**data), ]
