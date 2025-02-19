from fastapi import HTTPException, status

from ..constants.error import Error
from ..factories.actuator import ActuatorFactory
from ..models.actuator import ActuatorModel
from ..repositories.actuator import ActuatorRepository


class ActuatorService:
    def __init__(self, repository: ActuatorRepository = ActuatorRepository(), factory: ActuatorFactory = ActuatorFactory()):
        self.repository: ActuatorRepository = repository
        self.factory: ActuatorFactory = factory

    def get_actuator(self, record: str = '', skip: int = 0, limit: int = 100) -> list:
        data: list = self.repository.get(record=record, skip=skip, limit=limit)
        return [self.factory(**model) for model in data]

    def create_actuator(self, model: ActuatorModel) -> list:
        data = self.repository.get()
        exists = list(filter(lambda x: x['platform'] == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.ACTUATOR_ALREADY_EXISTS.value,
            )
        data = self.repository.create(model=model)
        return [self.factory(**data), ]

    def update_actuator(self, model: ActuatorModel, record: str) -> list:
        data = self.repository.get(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.ACTUATOR_NOT_EXISTS.value,
            )
        data = self.repository.get()
        exists = list(filter(lambda x: x['platform'] == model.platform, data))
        if len(exists):
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=Error.ACTUATOR_ALREADY_EXISTS.value,
            )
        data = self.repository.update(model=model, record=record)
        return [self.factory(**data), ]

    def delete_actuator(self, record: str, reason: str = '') -> list:
        data = self.repository.get(record=record)
        if not len(data):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Error.ACTUATOR_NOT_EXISTS.value,
            )
        data = self.repository.delete(record=record, reason=reason)
        return [self.factory(**data), ]
