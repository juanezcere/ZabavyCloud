from ..models.device import DeviceModel


class DeviceFactory:
    def __call__(self, *args, **kwargs) -> DeviceModel:
        return DeviceModel(*args, **kwargs)
