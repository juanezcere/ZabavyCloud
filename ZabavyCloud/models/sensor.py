from typing import Optional

from pydantic import BaseModel

from .output import OutputModel


class SensorModel(BaseModel):
    id: Optional[str]
    name: str
    image: str
    platform: str
    description: Optional[str] = ''
    variables: Optional[list] = []


class SensorsModel(OutputModel):
    data: list[SensorModel]
