from fastapi import HTTPException, status

from ..constants.error import Error
from ..models.sensor import SensorModel


class SensorFactory:
    def __call__(self, name: str, image: str, platform: str, id: str = '', description: str = '', variables: list = []) -> SensorModel:
        try:
            data: dict = {
                'id': str(id),
                'name': str(name),
                'image': str(image),
                'platform': str(platform),
                'description': str(description),
                'variables': [str(e) for e in list(variables)],
            }
            return SensorModel(**data)
        except Exception as err:
            print(err)
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=Error.SENSOR_BAD_REQUEST.value,
            )
