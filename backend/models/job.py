from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from backend.database.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
        index=True,
    )

    job_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    location: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    job_url: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    date_discovered: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    deadline: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
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

    company: Mapped["Company"] = relationship(
        "Company",
        back_populates="jobs",
    )

    applications: Mapped[list["Application"]] = relationship(
        "Application",
        back_populates="job",
        cascade="all, delete-orphan",
    )