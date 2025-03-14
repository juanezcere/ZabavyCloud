from fastapi import HTTPException, status

from ..constants.error import Error
from ..models.action import ActionModel


class ActionFactory:
    def __call__(self, name: str, image: str, platform: str, uid: str = '', description: str = '') -> ActionModel:
        try:
            data: dict = {
                'uid': str(uid),
                'name': str(name),
                'image': str(image),
                'platform': str(platform),
                'description': str(description),
            }
            return ActionModel(**data)
        except Exception as err:
            print(err)
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=Error.ACTION_BAD_REQUEST.value,
            )
