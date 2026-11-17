from datetime import datetime

from pydantic import Field

from backend.schemas import Schema


class CategoryCreate(Schema):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None


class CategoryUpdate(Schema):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None


class CategoryResponse(CategoryCreate):
    id: int
    created_at: datetime
    updated_at: datetime
