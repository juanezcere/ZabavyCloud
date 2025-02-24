from fastapi import HTTPException, status

from ..constants.error import Error
from ..models.device import DeviceModel


class DeviceFactory:
    def __call__(self, name: str, image: str, platform: str, id: str = '', description: str = '', sensors: list = [], actuators: list = []) -> DeviceModel:
        try:
            data: dict = {
                'id': str(id),
                'name': str(name),
                'image': str(image),
                'platform': str(platform),
                'description': str(description),
                'sensors': [str(e) for e in list(sensors)],
                'actuators': [str(e) for e in list(actuators)],
            }
            return DeviceModel(**data)
        except Exception as err:
            print(err)
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=Error.DEVICE_BAD_REQUEST.value,
            )
