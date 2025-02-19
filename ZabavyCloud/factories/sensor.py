from ..models.sensor import SensorModel


class SensorFactory:
    def __call__(self, *args, **kwargs) -> SensorModel:
        return SensorModel(*args, **kwargs)
