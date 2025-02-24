from fastapi import HTTPException, status

from ..constants.error import Error
from ..models.gateway import GatewayModel


class GatewayFactory:
    def __call__(self, name: str, image: str, platform: str, uid: str = '', description: str = '', devices: list = []) -> GatewayModel:
        try:
            data: dict = {
                'uid': str(uid),
                'name': str(name),
                'image': str(image),
                'platform': str(platform),
                'description': str(description),
                'devices': [str(e) for e in list(devices)],
            }
            return GatewayModel(**data)
        except Exception as err:
            print(err)
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=Error.GATEWAY_BAD_REQUEST.value,
            )
