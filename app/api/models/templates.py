# app/models/templates.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from ...database.session import Base


class Template(Base):
    __tablename__ = 'templates'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

