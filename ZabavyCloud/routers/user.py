import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Header, Request, status

from Zabavy.constants.error import Error
from Zabavy.constants.route import Route
from Zabavy.iterators.user import UserIterator
from Zabavy.schema.delete import DeleteSchema
from Zabavy.schema.output import OutputSchema
from Zabavy.schema.user_input import UserInputSchema
from Zabavy.schema.user_output import UserOutputSchema

# from core.middlewares.token_middleware import TokenMiddleware
# from core.middlewares.permissions_middleware import PermissionsMiddleware


class UsersOutputSchema(OutputSchema):
    data: list[UserOutputSchema]


router = APIRouter(prefix=Route.USER.value, tags=['Users API.'])
iterator = UserIterator()

# token_middleware = TokenMiddleware()
# permissions_middleware = PermissionsMiddleware()


@router.get('/', response_model=UsersOutputSchema, status_code=status.HTTP_200_OK)
async def get_users(request: Request, record: str = '', skip: int = 0, limit: int = 100, x_token: Annotated[str, Header()] = '') -> UsersOutputSchema:
    """
    Gets the user models from the API.
    """
    logging.debug(f'Getting users for token "{x_token}" from api.')
    data: list = await iterator.get_users(request=request.state.headers, record=record, skip=skip, limit=limit)
    return UsersOutputSchema(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.post('/', response_model=UsersOutputSchema, status_code=status.HTTP_200_OK)
async def create_user(request: Request, model: UserInputSchema, x_token: Annotated[str, Header()] = '') -> UsersOutputSchema:
    """
    Creates a new user from api.
    """
    logging.debug(
        f'Creating user {model.dict()} with token "{x_token}" from api.')
    data: list = await iterator.create_user(request=request.state.headers, model=model)
    return UsersOutputSchema(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.put('/{record}', response_model=UsersOutputSchema, status_code=status.HTTP_200_OK)
async def update_user(request: Request, record: str, model: UserInputSchema, x_token: Annotated[str, Header()] = '') -> UsersOutputSchema:
    """
    Updates an user specified by its id from the api.
    """
    logging.debug(
        f'Updating the user with id "{record}" with token "{x_token}" from api.')
    data: list = await iterator.update_user(request=request.state.headers, model=model, record=record)
    return UsersOutputSchema(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))


@router.delete('/{record}', response_model=UsersOutputSchema, status_code=status.HTTP_200_OK)
async def delete_user(request: Request, record: str, model: DeleteSchema, x_token: Annotated[str, Header()] = '') -> UsersOutputSchema:
    """
    Deletes a created user specified by its id from the api.
    """
    logging.debug(
        f'Deleting the user with id "{record}" with token "{x_token}" from api.')
    data: list = await iterator.delete_user(request=request.state.headers, model=model, record=record)
    return UsersOutputSchema(**Error.SUCCESSFULLY.value, token=x_token, user={}, data=data, quantity=len(data))
