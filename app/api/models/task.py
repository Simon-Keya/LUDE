from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship  
from app.database.session import Base
from .tags import Tag

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    due_date = Column(DateTime)
    completed = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"))
    
