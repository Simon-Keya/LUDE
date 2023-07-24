from pydantic import BaseModel
from datetime import datetime

class TagCreate(BaseModel):
    name: str
    color: str


class TagUpdate(BaseModel):
    name: str = None
    color: str = None


class Tag(BaseModel):
    id: int
    name: str
    color: str
    created_at: datetime
    updated_at: datetime

