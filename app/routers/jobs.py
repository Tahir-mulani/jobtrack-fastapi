from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.job import Job
from app.models.company import Company
from app.schemas.job import JobCreate, JobOut
from app.routers.auth import current_user
from app.models.user import User

router = APIRouter()


@router.get("", response_model=list[JobOut])
def list_jobs(db: Session = Depends(get_db), user: User = Depends(current_user)):
    return list(db.scalars(select(Job).order_by(Job.id.desc())).all())


@router.post("", response_model=JobOut, status_code=201)
def create_job(data: JobCreate, db: Session = Depends(get_db), user: User = Depends(current_user)):
    if not db.get(Company, data.company_id):
        raise HTTPException(404, "Company not found")
    job = Job(**data.model_dump())
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


@router.get("/{job_id}", response_model=JobOut)
def get_job(job_id: int, db: Session = Depends(get_db), user: User = Depends(current_user)):
    job = db.get(Job, job_id)
    if not job:
        raise HTTPException(404, "Job not found")
    return job
