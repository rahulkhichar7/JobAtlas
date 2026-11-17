from fastapi import APIRouter, Depends, status

from backend.api.dependencies import get_job_service
from backend.core.enums import JobType
from backend.schemas.job import JobCreate, JobResponse, JobUpdate
from backend.services.job_service import JobService

router = APIRouter(prefix="/jobs", tags=["Jobs"])
Service = JobService


@router.post("", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
def create_job(data: JobCreate, service: Service = Depends(get_job_service)):
    return service.create(data)


@router.get("", response_model=list[JobResponse])
def list_jobs(
    company_id: int | None = None,
    category_id: int | None = None,
    job_type: JobType | None = None,
    service: Service = Depends(get_job_service),
):
    return service.search(company_id, category_id, job_type.value if job_type else None)


@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int, service: Service = Depends(get_job_service)):
    return service.get(job_id)


@router.patch("/{job_id}", response_model=JobResponse)
def update_job(job_id: int, data: JobUpdate, service: Service = Depends(get_job_service)):
    return service.update(job_id, data)


@router.delete("/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(job_id: int, service: Service = Depends(get_job_service)):
    """Deletes the job with its application and progress."""
    service.delete(job_id)
