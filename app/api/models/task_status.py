# app/models/task_status.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from ...database.session import Base


class TaskStatus(Base):
    __tablename__ = 'task status'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

