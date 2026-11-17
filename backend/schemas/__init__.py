from pydantic import BaseModel, ConfigDict


class Schema(BaseModel):
    """Base for all request/response schemas."""

    model_config = ConfigDict(
        from_attributes=True,  # build responses straight from ORM objects
        use_enum_values=True,  # enums are stored as plain strings
        str_strip_whitespace=True,
    )
