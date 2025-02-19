from typing import Annotated

from fastapi import APIRouter, Depends, Header, Request, status

from ..constants.error import Error
from ..constants.route import Route
from ..models.delete import DeleteModel
from ..models.variable import VariableModel, VariablesModel
from ..repositories.variable import VariableRepository
from ..services.variable import VariableService

router = APIRouter(prefix=Route.VARIABLE.value, tags=['Variables API.'])

repository = VariableRepository()


def build_service() -> VariableService:
    return VariableService(repository=repository)


@router.get('/', response_model=VariablesModel, status_code=status.HTTP_200_OK)
async def get_variables(request: Request, record: str = '', skip: int = 0, limit: int = 100, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> VariablesModel:
    """
    Gets the variable models from the API.
    """
    # logging.debug(f"Getting variables for token '{x_token}' from api."")
    data: list = service.get_variable(record=record, skip=skip, limit=limit)
    return VariablesModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.post('/', response_model=VariablesModel, status_code=status.HTTP_201_CREATED)
async def create_variable(request: Request, model: VariableModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> VariablesModel:
    """
    Creates a new variable from api.
    """
    # logging.debug(f'Creating variable '{model.name}' for token '{x_token}' from api.')
    data: list = service.create_variable(model=model)
    return VariablesModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.put('/{record}', response_model=VariablesModel, status_code=status.HTTP_200_OK)
async def update_variable(request: Request, record: str, model: VariableModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> VariablesModel:
    """
    Updates a variable specified by its id from the api.
    """
    # logging.debug(f"Updating variable '{record}' with token '{x_token}' from api.")
    data: list = service.update_variable(model=model, record=record)
    return VariablesModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.delete('/{record}', response_model=VariablesModel, status_code=status.HTTP_200_OK)
async def delete_variable(request: Request, record: str, model: DeleteModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> VariablesModel:
    """
    Deletes a created variable specified by its id from the api.
    """
    # logging.debug(f"Deleting variable '{record}' with token '{x_token}' from api.")
    data: list = service.delete_variable(record=record, reason=model.reason)
    return VariablesModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))
