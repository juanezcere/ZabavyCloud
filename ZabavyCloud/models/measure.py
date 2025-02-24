from typing import Optional

from pydantic import BaseModel

from .output import OutputModel


class MeasureModel(BaseModel):
    uid: Optional[str]
    device: str
    timestamp: int
    values: dict[str, float] = {}


class MeasuresModel(OutputModel):
    data: list[MeasureModel]
