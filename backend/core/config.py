from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    app_name: str = "JobGraph API"
    app_version: str = "0.1.0"

    database_url: str = f"sqlite:///{BASE_DIR / 'data' / 'job_tracker.db'}"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()