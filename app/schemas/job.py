from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class JobCreate(BaseModel):
    company_id: int
    title: str = Field(min_length=2, max_length=150)
    description: str | None = None
    location: str | None = None
    employment_type: str | None = None
    salary_min: float | None = Field(default=None, ge=0)
    salary_max: float | None = Field(default=None, ge=0)
    job_url: HttpUrl | None = None


class JobOut(JobCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
