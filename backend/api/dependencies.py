from fastapi import Depends
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.services.application_service import ApplicationService
from backend.services.category_service import CategoryService
from backend.services.company_service import CompanyService
from backend.services.graph_service import GraphService
from backend.services.job_service import JobService
from backend.services.progress_service import ProgressService


def get_category_service(db: Session = Depends(get_db)) -> CategoryService:
    return CategoryService(db)


def get_company_service(db: Session = Depends(get_db)) -> CompanyService:
    return CompanyService(db)


def get_job_service(db: Session = Depends(get_db)) -> JobService:
    return JobService(db)


def get_application_service(db: Session = Depends(get_db)) -> ApplicationService:
    return ApplicationService(db)


def get_progress_service(db: Session = Depends(get_db)) -> ProgressService:
    return ProgressService(db)


def get_graph_service(db: Session = Depends(get_db)) -> GraphService:
    return GraphService(db)
