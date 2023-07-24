from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    task_id: int
    user_id: int
    content: str


class CommentUpdate(BaseModel):
    content: str


class Comment(BaseModel):
    id: int
    task_id: int
    user_id: int
    content: str
    created_at: datetime
    updated_at: datetime

