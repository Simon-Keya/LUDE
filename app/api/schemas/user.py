from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional 

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
    user_type: str
    password: str
    first_name: str
    last_name: str
    role: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

class AdminBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: Optional[str]

class AdminCreate(AdminBase):
    user_type: str


class AdminUpdate(AdminCreate):
    pass


class AdminShow(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    user_type: str
    
    class Config:
        orm_mode = True


