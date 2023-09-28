# app/models/user.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ...database.session import Base
from ..models.task import Task

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    user_type = Column(String, default="guest")
    role_id = Column(Integer, ForeignKey("roles.id"))
    tasks = relationship("Task", back_populates="user")
