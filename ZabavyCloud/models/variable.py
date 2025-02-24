from typing import Optional

from pydantic import BaseModel

from .output import OutputModel


class VariableModel(BaseModel):
    uid: Optional[str]
    name: str
    image: str
    platform: str
    description: Optional[str] = ''
    maximum: Optional[float] = 100.0
    minimum: Optional[float] = 0.0
    offset: Optional[float] = 0.0
    equation: Optional[list[float]] = [0.0, 0.0, 0.0, 0.0, 1.0, 0.0]


class VariablesModel(OutputModel):
    data: list[VariableModel]
