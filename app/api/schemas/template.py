from pydantic import BaseModel
from datetime import datetime

class TemplateCreate(BaseModel):
    title: str
    description: str
    content: str
    
    class Config:
        orm_mode = True


class TemplateUpdate(BaseModel):
    title: str = None
    description: str = None
    content: str = None


class Template(BaseModel):
    id: int
    title: str
    description: str
    content: str
    created_at: datetime
    updated_at: datetime

