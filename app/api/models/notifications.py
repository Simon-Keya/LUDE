from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from ...database.session import Base


class Notification(Base):
    __tablename__ = 'notifications'
    id = Column(Integer, primary_key=True)
    message = Column(String(255))
    url = Column(String(255))
    read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

