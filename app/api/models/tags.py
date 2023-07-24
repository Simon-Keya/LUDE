# app/models/tag.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from ...database.session import Base
from sqlalchemy.orm import relationship


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    color = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
    

