from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    role: str = "user"
    
    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    first_name: str = None
    last_name: str = None
    role: str = None


class User(BaseModel):
    id: int
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    role: str
    created_at: datetime
    updated_at: datetime

