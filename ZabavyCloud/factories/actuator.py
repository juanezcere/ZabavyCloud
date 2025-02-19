from ..models.actuator import ActuatorModel


class ActuatorFactory:
    def __call__(self, *args, **kwargs) -> ActuatorModel:
        return ActuatorModel(*args, **kwargs)
