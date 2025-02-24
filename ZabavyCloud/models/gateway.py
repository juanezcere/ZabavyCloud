from typing import Optional

from pydantic import BaseModel

from .output import OutputModel


class GatewayModel(BaseModel):
    uid: Optional[str]
    name: str
    image: str
    platform: str
    description: Optional[str] = ''
    devices: Optional[list] = []


class GatewaysModel(OutputModel):
    data: list[GatewayModel]
