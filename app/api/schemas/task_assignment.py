from pydantic import BaseModel
from datetime import datetime

class TaskAssignmentCreate(BaseModel):
    task_id: int
    user_id: int


class TaskAssignmentUpdate(BaseModel):
    task_id: int = None
    user_id: int = None


class TaskAssignment(BaseModel):
    id: int
    task_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

