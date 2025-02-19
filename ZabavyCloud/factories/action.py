from ..models.action import ActionModel


class ActionFactory:
    def __call__(self, *args, **kwargs) -> ActionModel:
        return ActionModel(*args, **kwargs)
