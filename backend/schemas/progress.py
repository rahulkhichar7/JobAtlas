from datetime import date, datetime

from pydantic import Field

from backend.core.enums import ProgressResult
from backend.schemas import Schema


class ProgressFields(Schema):
    stage_date: date | None = None
    notes: str | None = None


class ProgressCreate(ProgressFields):
    stage: str = Field(min_length=1, max_length=100)
    result: ProgressResult = ProgressResult.PENDING
    application_id: int


class ProgressUpdate(ProgressFields):
    stage: str | None = Field(default=None, min_length=1, max_length=100)
    result: ProgressResult | None = None


class ProgressResponse(ProgressCreate):
    id: int
    created_at: datetime
    updated_at: datetime
