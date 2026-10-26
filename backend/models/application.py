from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from backend.database.base import Base


class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="applied",
        index=True,
    )

    priority: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="medium",
    )

    applied_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    resume_used: Mapped[str | None] = mapped_column(
        String(300),
        nullable=True,
    )

    next_action: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    next_action_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey("jobs.id"),
        nullable=False,
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    job: Mapped["Job"] = relationship(
        "Job",
        back_populates="applications",
    )

    progress: Mapped[list["Progress"]] = relationship(
        "Progress",
        back_populates="application",
        cascade="all, delete-orphan",
        order_by="Progress.created_at",
    )
