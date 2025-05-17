from pydantic import BaseModel
from typing import List
from datetime import datetime

class NotificationCreate(BaseModel):
    user_id: str
    type: str
    message: str

class NotificationOut(BaseModel):
    id: int
    user_id: str
    type: str
    message: str
    status: str
    timestamp: datetime

    class Config:
        orm_mode = True