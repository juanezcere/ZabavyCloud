from typing import Annotated

from fastapi import APIRouter, Depends, Header, Request, status

from ..constants.error import Error
from ..constants.route import Route
from ..models.delete import DeleteModel
from ..models.sensor import SensorModel, SensorsModel
from ..repositories.sensor import SensorRepository
from ..services.sensor import SensorService

router = APIRouter(prefix=Route.SENSOR.value, tags=['Sensors API.'])

repository = SensorRepository()


def build_service() -> SensorService:
    return SensorService(repository=repository)


@router.get('/', response_model=SensorsModel, status_code=status.HTTP_200_OK)
async def get_sensors(request: Request, record: str = '', skip: int = 0, limit: int = 100, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> SensorsModel:
    """
    Gets the sensor models from the API.
    """
    # logging.debug(f"Getting sensors for token '{x_token}' from api."")
    data: list = service.get_sensor(record=record, skip=skip, limit=limit)
    return SensorsModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.post('/', response_model=SensorsModel, status_code=status.HTTP_201_CREATED)
async def create_sensor(request: Request, model: SensorModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> SensorsModel:
    """
    Creates a new sensor from api.
    """
    # logging.debug(f'Creating sensor '{model.name}' for token '{x_token}' from api.')
    data: list = service.create_sensor(model=model)
    return SensorsModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.put('/{record}', response_model=SensorsModel, status_code=status.HTTP_200_OK)
async def update_sensor(request: Request, record: str, model: SensorModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> SensorsModel:
    """
    Updates a sensor specified by its id from the api.
    """
    # logging.debug(f"Updating sensor '{record}' with token '{x_token}' from api.")
    data: list = service.update_sensor(model=model, record=record)
    return SensorsModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.delete('/{record}', response_model=SensorsModel, status_code=status.HTTP_200_OK)
async def delete_sensor(request: Request, record: str, model: DeleteModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> SensorsModel:
    """
    Deletes a created sensor specified by its id from the api.
    """
    # logging.debug(f"Deleting sensor '{record}' with token '{x_token}' from api.")
    data: list = service.delete_sensor(record=record, reason=model.reason)
    return SensorsModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))
