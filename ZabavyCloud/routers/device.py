from typing import Annotated

from fastapi import APIRouter, Depends, Header, Request, status

from ..constants.error import Error
from ..constants.route import Route
from ..models.delete import DeleteModel
from ..models.device import DeviceModel, DevicesModel
from ..repositories.device import DeviceRepository
from ..services.device import DeviceService

router = APIRouter(prefix=Route.DEVICE.value, tags=['Devices API.'])

repository = DeviceRepository()


def build_service() -> DeviceService:
    return DeviceService(repository=repository)


@router.get('/', response_model=DevicesModel, status_code=status.HTTP_200_OK)
async def get_devices(request: Request, record: str = '', skip: int = 0, limit: int = 100, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> DevicesModel:
    """
    Gets the device models from the API.
    """
    # logging.debug(f"Getting devices for token '{x_token}' from api."")
    data: list = service.get_device(record=record, skip=skip, limit=limit)
    return DevicesModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.post('/', response_model=DevicesModel, status_code=status.HTTP_201_CREATED)
async def create_device(request: Request, model: DeviceModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> DevicesModel:
    """
    Creates a new device from api.
    """
    # logging.debug(f'Creating device '{model.name}' for token '{x_token}' from api.')
    data: list = service.create_device(model=model)
    return DevicesModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.put('/{record}', response_model=DevicesModel, status_code=status.HTTP_200_OK)
async def update_device(request: Request, record: str, model: DeviceModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> DevicesModel:
    """
    Updates a device specified by its id from the api.
    """
    # logging.debug(f"Updating device '{record}' with token '{x_token}' from api.")
    data: list = service.update_device(model=model, record=record)
    return DevicesModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.delete('/{record}', response_model=DevicesModel, status_code=status.HTTP_200_OK)
async def delete_device(request: Request, record: str, model: DeleteModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> DevicesModel:
    """
    Deletes a created device specified by its id from the api.
    """
    # logging.debug(f"Deleting device '{record}' with token '{x_token}' from api.")
    data: list = service.delete_device(record=record, reason=model.reason)
    return DevicesModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))
