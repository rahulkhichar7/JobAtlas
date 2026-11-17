from datetime import datetime

from pydantic import Field

from backend.schemas import Schema


class CompanyFields(Schema):
    website: str | None = Field(default=None, max_length=500)
    location: str | None = Field(default=None, max_length=200)
    description: str | None = None
    notes: str | None = None


class CompanyCreate(CompanyFields):
    name: str = Field(min_length=1, max_length=200)
    category_id: int


class CompanyUpdate(CompanyFields):
    name: str | None = Field(default=None, min_length=1, max_length=200)
    category_id: int | None = None


class CompanyResponse(CompanyCreate):
    id: int
    created_at: datetime
    updated_at: datetime
