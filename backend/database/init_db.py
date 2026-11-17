import backend.models  # noqa: F401  (registers all models on Base.metadata)
from backend.database.base import Base
from backend.database.database import engine


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
