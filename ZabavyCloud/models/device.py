from typing import Optional

from pydantic import BaseModel

from .output import OutputModel


class DeviceModel(BaseModel):
    uid: Optional[str]
    name: str
    image: str
    platform: str
    description: Optional[str] = ''
    sensors: Optional[list] = []
    actuators: Optional[list] = []


class DevicesModel(OutputModel):
    data: list[DeviceModel]
