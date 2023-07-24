from pydantic import BaseModel
from datetime import datetime

class ProjectCreate(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime


class ProjectUpdate(BaseModel):
    title: str = None
    description: str = None
    start_date: datetime = None
    end_date: datetime = None


class Project(BaseModel):
    id: int
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    created_at: datetime
    updated_at: datetime

