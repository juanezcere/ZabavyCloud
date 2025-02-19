from typing import Optional

from pydantic import BaseModel

from .output import OutputModel


class ActuatorModel(BaseModel):
    id: Optional[str]
    name: str
    image: str
    platform: str
    description: Optional[str] = ''
    actions: Optional[list] = []


class ActuatorsModel(OutputModel):
    data: list[ActuatorModel]
