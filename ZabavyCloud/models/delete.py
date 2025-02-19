from pydantic import BaseModel


class DeleteModel(BaseModel):
    """
    ? Delete model to manage the data deletions on software.
    """
    reason: str
