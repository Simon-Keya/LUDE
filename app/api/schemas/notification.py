from pydantic import BaseModel
from datetime import datetime

class NotificationCreate(BaseModel):
    message: str
    url: str
    read: bool = False


class NotificationUpdate(BaseModel):
    read: bool = None


class Notification(BaseModel):
    id: int
    message: str
    url: str
    read: bool
    created_at: datetime
    updated_at: datetime

