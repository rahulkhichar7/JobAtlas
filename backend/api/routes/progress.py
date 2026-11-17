from fastapi import APIRouter, Depends, status

from backend.api.dependencies import get_progress_service
from backend.schemas.progress import ProgressCreate, ProgressResponse, ProgressUpdate
from backend.services.progress_service import ProgressService

router = APIRouter(prefix="/progress", tags=["Progress"])
Service = ProgressService


@router.post("", response_model=ProgressResponse, status_code=status.HTTP_201_CREATED)
def create_progress(data: ProgressCreate, service: Service = Depends(get_progress_service)):
    return service.create(data)


@router.get("", response_model=list[ProgressResponse])
def list_progress(application_id: int, service: Service = Depends(get_progress_service)):
    """Timeline of one application, ordered by date."""
    return service.get_by_application(application_id)


@router.get("/{progress_id}", response_model=ProgressResponse)
def get_progress(progress_id: int, service: Service = Depends(get_progress_service)):
    return service.get(progress_id)


@router.patch("/{progress_id}", response_model=ProgressResponse)
def update_progress(
    progress_id: int, data: ProgressUpdate, service: Service = Depends(get_progress_service)
):
    return service.update(progress_id, data)


@router.delete("/{progress_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_progress(progress_id: int, service: Service = Depends(get_progress_service)):
    service.delete(progress_id)
