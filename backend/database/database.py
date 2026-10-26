from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from backend.core.config import settings
from backend.database.base import Base
from backend.models import Application, Category, Company, Job, Progress

engine = create_engine(
    url=settings.database_url,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

def get_db() -> Generator[int, None, None]:
    db = SessionLocal()

    try:
        yield db
    except:
        db.close()

def init_db() -> None:
    Base.metadata.create_all(bind=engine)