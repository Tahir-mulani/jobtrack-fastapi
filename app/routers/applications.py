from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.application import Application
from app.models.job import Job
from app.models.user import User
from app.schemas.application import ApplicationCreate, ApplicationOut, ApplicationUpdate, STATUSES
from app.routers.auth import current_user

router = APIRouter()


@router.get("", response_model=list[ApplicationOut])
def list_applications(
    status: str | None = None,
    db: Session = Depends(get_db),
    user: User = Depends(current_user),
):
    stmt = select(Application).where(Application.user_id == user.id)
    if status:
        if status.upper() not in STATUSES:
            raise HTTPException(400, "Invalid application status")
        stmt = stmt.where(Application.status == status.upper())
    return list(db.scalars(stmt.order_by(Application.id.desc())).all())


@router.post("", response_model=ApplicationOut, status_code=201)
def create_application(data: ApplicationCreate, db: Session = Depends(get_db), user: User = Depends(current_user)):
    if data.status.upper() not in STATUSES:
        raise HTTPException(400, "Invalid application status")
    if not db.get(Job, data.job_id):
        raise HTTPException(404, "Job not found")
    application = Application(
        user_id=user.id,
        job_id=data.job_id,
        status=data.status.upper(),
        applied_date=data.applied_date,
        source=data.source,
        notes=data.notes,
    )
    db.add(application)
    db.commit()
    db.refresh(application)
    return application


@router.get("/{application_id}", response_model=ApplicationOut)
def get_application(application_id: int, db: Session = Depends(get_db), user: User = Depends(current_user)):
    item = db.get(Application, application_id)
    if not item or item.user_id != user.id:
        raise HTTPException(404, "Application not found")
    return item


@router.put("/{application_id}", response_model=ApplicationOut)
def update_application(application_id: int, data: ApplicationUpdate, db: Session = Depends(get_db), user: User = Depends(current_user)):
    item = db.get(Application, application_id)
    if not item or item.user_id != user.id:
        raise HTTPException(404, "Application not found")
    changes = data.model_dump(exclude_unset=True)
    if "status" in changes:
        changes["status"] = changes["status"].upper()
        if changes["status"] not in STATUSES:
            raise HTTPException(400, "Invalid application status")
    for key, value in changes.items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/{application_id}", status_code=204)
def delete_application(application_id: int, db: Session = Depends(get_db), user: User = Depends(current_user)):
    item = db.get(Application, application_id)
    if not item or item.user_id != user.id:
        raise HTTPException(404, "Application not found")
    db.delete(item)
    db.commit()
