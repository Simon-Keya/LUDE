from pydantic import BaseModel
from datetime import datetime

class TaskStatus(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

