# app/models/task_assignment.py
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from ...database.session import Base


class TaskAssignment(Base):
    __tablename__ = 'task_assignments'
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

