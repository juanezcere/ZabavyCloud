from pydantic import BaseModel


class OutputModel(BaseModel):
    """
    ? Base model to manage the output schemas on software.
    """
    code: str
    message: str
    token: str
    user: dict
    data: list
    quantity: int = 0
