from datetime import date, datetime

from pydantic import Field

from backend.core.enums import ApplicationStatus, Priority
from backend.schemas import Schema


class ApplicationFields(Schema):
    applied_date: date | None = None
    resume_used: str | None = Field(default=None, max_length=300)
    next_action: str | None = Field(default=None, max_length=500)
    next_action_date: date | None = None
    notes: str | None = None


class ApplicationCreate(ApplicationFields):
    status: ApplicationStatus = ApplicationStatus.APPLIED
    priority: Priority = Priority.MEDIUM
    job_id: int


class ApplicationUpdate(ApplicationFields):
    status: ApplicationStatus | None = None
    priority: Priority | None = None


class ApplicationResponse(ApplicationCreate):
    id: int
    job_title: str
    company_id: int
    company_name: str
    created_at: datetime
    updated_at: datetime
