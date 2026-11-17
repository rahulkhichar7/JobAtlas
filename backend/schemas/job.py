from datetime import date, datetime

from pydantic import Field

from backend.core.enums import JobType
from backend.schemas import Schema


class JobFields(Schema):
    location: str | None = Field(default=None, max_length=200)
    job_url: str | None = Field(default=None, max_length=1000)
    date_discovered: date | None = None
    deadline: date | None = None
    description: str | None = None
    notes: str | None = None


class JobCreate(JobFields):
    title: str = Field(min_length=1, max_length=300)
    job_type: JobType = JobType.FULL_TIME
    company_id: int


class JobUpdate(JobFields):
    title: str | None = Field(default=None, min_length=1, max_length=300)
    job_type: JobType | None = None
    company_id: int | None = None


class JobResponse(JobCreate):
    id: int
    created_at: datetime
    updated_at: datetime
