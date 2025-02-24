from fastapi import HTTPException, status

from ..constants.error import Error
from ..models.variable import VariableModel


class VariableFactory:
    def __call__(self, name: str, image: str, platform: str, uid: str = '', description: str = '', maximum: float = 100.0, minimum: float = -100.0, offset: float = 0.0, equation: list = [0.0, 0.0, 0.0, 0.0, 1.0, 0.0]) -> VariableModel:
        try:
            data: dict = {
                'uid': str(uid),
                'name': str(name),
                'image': str(image),
                'platform': str(platform),
                'description': str(description),
                'maximum': float(maximum),
                'minimum': float(minimum),
                'offset': float(offset),
                'equation': [float(e) for e in list(equation)],
            }
            return VariableModel(**data)
        except Exception as err:
            print(err)
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=Error.VARIABLE_BAD_REQUEST.value,
            )
