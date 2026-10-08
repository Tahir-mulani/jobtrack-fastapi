from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.application import Application
from app.models.interview import Interview
from app.models.user import User
from app.routers.auth import current_user

router = APIRouter()


@router.get("/stats")
def stats(db: Session = Depends(get_db), user: User = Depends(current_user)):
    total = db.scalar(select(func.count(Application.id)).where(Application.user_id == user.id)) or 0
    rows = db.execute(
        select(Application.status, func.count(Application.id))
        .where(Application.user_id == user.id)
        .group_by(Application.status)
    ).all()
    statuses = {status: count for status, count in rows}
    interview_count = db.scalar(
        select(func.count(Interview.id))
        .join(Application)
        .where(Application.user_id == user.id)
    ) or 0
    offers = statuses.get("OFFER", 0)
    rejected = statuses.get("REJECTED", 0)
    return {
        "total_applications": total,
        "interviews": interview_count,
        "offers": offers,
        "rejected": rejected,
        "by_status": statuses,
    }
