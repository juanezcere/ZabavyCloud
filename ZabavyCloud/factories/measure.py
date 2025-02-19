from ..models.measure import MeasureModel


class MeasureFactory:
    def __call__(self, *args, **kwargs) -> MeasureModel:
        return MeasureModel(*args, **kwargs)
