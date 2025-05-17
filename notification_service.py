from models import Notification
from services.email_service import send_email
from services.sms_service import send_sms
from sqlalchemy.orm import Session
import schemas

def send_notification(db: Session, notification: schemas.NotificationCreate):
    if notification.type == "email":
        send_email(notification.user_id, notification.message)
    elif notification.type == "sms":
        send_sms(notification.user_id, notification.message)
    elif notification.type == "in-app":
        pass
    else:
        raise ValueError("Unsupported notification type")

    db_notification = Notification(
        user_id=notification.user_id,
        type=notification.type,
        message=notification.message,
        status="sent"
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

def get_user_notifications(db: Session, user_id: str):
    return db.query(Notification).filter(Notification.user_id == user_id).all()