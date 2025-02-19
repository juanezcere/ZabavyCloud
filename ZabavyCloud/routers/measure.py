from typing import Annotated

from fastapi import APIRouter, Depends, Header, Request, status

from ..constants.error import Error
from ..constants.route import Route
from ..models.delete import DeleteModel
from ..models.measure import MeasureModel, MeasuresModel
from ..repositories.measure import MeasureRepository
from ..services.measure import MeasureService

router = APIRouter(prefix=Route.MEASURE.value, tags=['Measures API.'])

repository = MeasureRepository()


def build_service() -> MeasureService:
    return MeasureService(repository=repository)


@router.get('/', response_model=MeasuresModel, status_code=status.HTTP_200_OK)
async def get_measures(request: Request, record: str = '', skip: int = 0, limit: int = 100, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> MeasuresModel:
    """
    Gets the measure models from the API.
    """
    # logging.debug(f"Getting measures for token '{x_token}' from api."")
    data: list = service.get_measure(record=record, skip=skip, limit=limit)
    return MeasuresModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.post('/', response_model=MeasuresModel, status_code=status.HTTP_201_CREATED)
async def create_measure(request: Request, model: MeasureModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> MeasuresModel:
    """
    Creates a new measure from api.
    """
    # logging.debug(f'Creating measure '{model.name}' for token '{x_token}' from api.')
    data: list = service.create_measure(model=model)
    return MeasuresModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.put('/{record}', response_model=MeasuresModel, status_code=status.HTTP_200_OK, deprecated=True)
async def update_measure(request: Request, record: str, model: MeasureModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> MeasuresModel:
    """
    Updates a measure specified by its id from the api.
    """
    # logging.debug(f"Updating measure '{record}' with token '{x_token}' from api.")
    data: list = service.update_measure(model=model, record=record)
    return MeasuresModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.delete('/{record}', response_model=MeasuresModel, status_code=status.HTTP_200_OK, deprecated=True)
async def delete_measure(request: Request, record: str, model: DeleteModel, x_token: Annotated[str, Header()] = '', service=Depends(build_service)) -> MeasuresModel:
    """
    Deletes a created measure specified by its id from the api.
    """
    # logging.debug(f"Deleting measure '{record}' with token '{x_token}' from api.")
    data: list = service.delete_measure(record=record, reason=model.reason)
    return MeasuresModel(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))
