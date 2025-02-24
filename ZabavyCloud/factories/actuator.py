from fastapi import HTTPException, status

from ..constants.error import Error
from ..models.actuator import ActuatorModel


class ActuatorFactory:
    def __call__(self, name: str, image: str, platform: str, uid: str = '', description: str = '', actions: list = []) -> ActuatorModel:
        try:
            data: dict = {
                'uid': str(uid),
                'name': str(name),
                'image': str(image),
                'platform': str(platform),
                'description': str(description),
                'actions': [str(e) for e in list(actions)],
            }
            return ActuatorModel(**data)
        except Exception as err:
            print(err)
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=Error.ACTUATOR_BAD_REQUEST.value,
            )
