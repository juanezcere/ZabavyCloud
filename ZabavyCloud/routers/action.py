from typing import Annotated

from fastapi import APIRouter, Depends, Header, Request, status

from ..constants.error import Error
from ..constants.route import Route
from ..models.delete import DeleteModel
from ..models.action import ActionModel, ActionsModel
from ..repositories.action import ActionRepository
from ..services.action import ActionService

router = APIRouter(prefix=Route.ACTION.value, tags=['Actions API.'])

repository = ActionRepository()


def build_service() -> ActionService:
    return ActionService(repository=repository)


@router.get('/', response_model=ActionsModel, status_code=status.HTTP_200_OK)
async def get_actions(request: Request, record: str = '', skip: int = 0, limit: int = 100, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> ActionsModel:
    """
    Gets the action models from the API.
    """
    # logging.debug(f"Getting actions for token '{x_token}' from api."")
    data: list = service.get_action(record=record, skip=skip, limit=limit)
    return ActionsModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.post('/', response_model=ActionsModel, status_code=status.HTTP_201_CREATED)
async def create_action(request: Request, model: ActionModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> ActionsModel:
    """
    Creates a new action from api.
    """
    # logging.debug(f'Creating action '{model.name}' for token '{x_token}' from api.')
    data: list = service.create_action(model=model)
    return ActionsModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.put('/{record}', response_model=ActionsModel, status_code=status.HTTP_200_OK)
async def update_action(request: Request, record: str, model: ActionModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> ActionsModel:
    """
    Updates a action specified by its id from the api.
    """
    # logging.debug(f"Updating action '{record}' with token '{x_token}' from api.")
    data: list = service.update_action(model=model, record=record)
    return ActionsModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.delete('/{record}', response_model=ActionsModel, status_code=status.HTTP_200_OK)
async def delete_action(request: Request, record: str, model: DeleteModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> ActionsModel:
    """
    Deletes a created action specified by its id from the api.
    """
    # logging.debug(f"Deleting action '{record}' with token '{x_token}' from api.")
    data: list = service.delete_action(record=record, reason=model.reason)
    return ActionsModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))
