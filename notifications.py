from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import schemas
import services.notification_service as notification_service
from typing import List

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.post("/", response_model=schemas.NotificationOut)
def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(get_db)):
    try:
        return notification_service.send_notification(db, notification)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/{user_id}", response_model=List[schemas.NotificationOut])
def get_notifications(user_id: str, db: Session = Depends(get_db)):
    return notification_service.get_user_notifications(db, user_id)