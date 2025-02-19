from typing import Annotated

from fastapi import APIRouter, Depends, Header, Request, status

from ..constants.error import Error
from ..constants.route import Route
from ..models.delete import DeleteModel
from ..models.gateway import GatewayModel, GatewaysModel
from ..repositories.gateway import GatewayRepository
from ..services.gateway import GatewayService

router = APIRouter(prefix=Route.VARIABLE.value, tags=['Gateways API.'])

repository = GatewayRepository()


def build_service() -> GatewayService:
    return GatewayService(repository=repository)


@router.get('/', response_model=GatewaysModel, status_code=status.HTTP_200_OK)
async def get_gateways(request: Request, record: str = '', skip: int = 0, limit: int = 100, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> GatewaysModel:
    """
    Gets the gateway models from the API.
    """
    # logging.debug(f"Getting gateways for token '{x_token}' from api."")
    data: list = service.get_gateway(record=record, skip=skip, limit=limit)
    return GatewaysModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.post('/', response_model=GatewaysModel, status_code=status.HTTP_201_CREATED)
async def create_gateway(request: Request, model: GatewayModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> GatewaysModel:
    """
    Creates a new gateway from api.
    """
    # logging.debug(f'Creating gateway '{model.name}' for token '{x_token}' from api.')
    data: list = service.create_gateway(model=model)
    return GatewaysModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.put('/{record}', response_model=GatewaysModel, status_code=status.HTTP_200_OK)
async def update_gateway(request: Request, record: str, model: GatewayModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> GatewaysModel:
    """
    Updates a gateway specified by its id from the api.
    """
    # logging.debug(f"Updating gateway '{record}' with token '{x_token}' from api.")
    data: list = service.update_gateway(model=model, record=record)
    return GatewaysModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.delete('/{record}', response_model=GatewaysModel, status_code=status.HTTP_200_OK)
async def delete_gateway(request: Request, record: str, model: DeleteModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> GatewaysModel:
    """
    Deletes a created gateway specified by its id from the api.
    """
    # logging.debug(f"Deleting gateway '{record}' with token '{x_token}' from api.")
    data: list = service.delete_gateway(record=record, reason=model.reason)
    return GatewaysModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))
