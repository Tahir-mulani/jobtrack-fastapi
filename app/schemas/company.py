from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class CompanyCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    website: HttpUrl | None = None
    location: str | None = Field(default=None, max_length=150)
    industry: str | None = Field(default=None, max_length=100)


class CompanyOut(CompanyCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
