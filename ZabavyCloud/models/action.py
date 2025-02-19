from typing import Optional

from pydantic import BaseModel

from .output import OutputModel


class ActionModel(BaseModel):
    id: Optional[str]
    name: str
    image: str
    platform: str
    description: Optional[str] = ''


class ActionsModel(OutputModel):
    data: list[ActionModel]
