from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.interview import Interview
from app.models.application import Application
from app.models.user import User
from app.schemas.interview import InterviewCreate, InterviewOut
from app.routers.auth import current_user

router = APIRouter()


@router.get("", response_model=list[InterviewOut])
def list_interviews(db: Session = Depends(get_db), user: User = Depends(current_user)):
    stmt = select(Interview).join(Application).where(Application.user_id == user.id)
    return list(db.scalars(stmt.order_by(Interview.scheduled_at)).all())


@router.post("", response_model=InterviewOut, status_code=201)
def create_interview(data: InterviewCreate, db: Session = Depends(get_db), user: User = Depends(current_user)):
    application = db.get(Application, data.application_id)
    if not application or application.user_id != user.id:
        raise HTTPException(404, "Application not found")
    item = Interview(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
