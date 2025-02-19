from ..models.variable import VariableModel


class VariableFactory:
    def __call__(self, *args, **kwargs) -> VariableModel:
        return VariableModel(*args, **kwargs)
