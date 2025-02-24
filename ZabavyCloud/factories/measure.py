from fastapi import HTTPException, status

from ..constants.error import Error
from ..models.measure import MeasureModel
from ..utils.time_utils import timestamp


class MeasureFactory:
    def __call__(self, device: str, uid: str = '', timestamp: int = timestamp(), values: dict = {}) -> MeasureModel:
        try:
            data: dict = {
                'uid': str(uid),
                'device': str(device),
                'timestamp': int(timestamp),
                'values': {key: float(value) for key, value in values.items()},
            }
            return MeasureModel(**data)
        except Exception as err:
            print(err)
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=Error.MEASURE_BAD_REQUEST.value,
            )
