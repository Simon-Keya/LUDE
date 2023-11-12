from pydantic import BaseModel
from typing import List
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: datetime
    completed: bool = False
    tags: List[str]
    
    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    title: str = None
    description: str = None
    due_date: datetime = None
    completed: bool = None
    tags: List[str] = None


class Task(BaseModel):
    id: int
    title: str
    description: str
    due_date: datetime
    completed: bool
    tags: List[str]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
