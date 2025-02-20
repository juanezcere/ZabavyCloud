from typing import Annotated

from fastapi import APIRouter, Depends, Header, Request, status

from ..constants.error import Error
from ..constants.route import Route
from ..models.actuator import ActuatorModel, ActuatorsModel
from ..models.delete import DeleteModel
from ..services.actuator import build_service

router = APIRouter(prefix=Route.ACTUATOR.value, tags=['Actuators API.'])


@router.get('/', response_model=ActuatorsModel, status_code=status.HTTP_200_OK)
async def get_actuators(request: Request, record: str = '', skip: int = 0, limit: int = 100, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> ActuatorsModel:
    """
    Gets the actuator models from the API.
    """
    # logging.debug(f"Getting actuators for token '{x_token}' from api."")
    data: list = service.get_actuator(record=record, skip=skip, limit=limit)
    return ActuatorsModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.post('/', response_model=ActuatorsModel, status_code=status.HTTP_201_CREATED)
async def create_actuator(request: Request, model: ActuatorModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> ActuatorsModel:
    """
    Creates a new actuator from api.
    """
    # logging.debug(f'Creating actuator '{model.name}' for token '{x_token}' from api.')
    data: list = service.create_actuator(model=model)
    return ActuatorsModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.put('/{record}', response_model=ActuatorsModel, status_code=status.HTTP_200_OK)
async def update_actuator(request: Request, record: str, model: ActuatorModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> ActuatorsModel:
    """
    Updates a actuator specified by its id from the api.
    """
    # logging.debug(f"Updating actuator '{record}' with token '{x_token}' from api.")
    data: list = service.update_actuator(model=model, record=record)
    return ActuatorsModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.delete('/{record}', response_model=ActuatorsModel, status_code=status.HTTP_200_OK)
async def delete_actuator(request: Request, record: str, model: DeleteModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> ActuatorsModel:
    """
    Deletes a created actuator specified by its id from the api.
    """
    # logging.debug(f"Deleting actuator '{record}' with token '{x_token}' from api.")
    data: list = service.delete_actuator(record=record, reason=model.reason)
    return ActuatorsModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))
