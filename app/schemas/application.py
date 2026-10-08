from datetime import date
from pydantic import BaseModel, ConfigDict, Field

STATUSES = ["APPLIED", "SCREENING", "INTERVIEW", "OFFER", "REJECTED", "WITHDRAWN"]


class ApplicationCreate(BaseModel):
    job_id: int
    status: str = Field(default="APPLIED")
    applied_date: date
    source: str | None = None
    notes: str | None = None


class ApplicationUpdate(BaseModel):
    status: str | None = None
    applied_date: date | None = None
    source: str | None = None
    notes: str | None = None


class ApplicationOut(ApplicationCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
