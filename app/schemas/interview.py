from datetime import datetime
from pydantic import BaseModel, ConfigDict


class InterviewCreate(BaseModel):
    application_id: int
    round_name: str
    interview_type: str | None = None
    scheduled_at: datetime
    status: str = "SCHEDULED"
    feedback: str | None = None


class InterviewOut(InterviewCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
