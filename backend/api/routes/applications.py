from fastapi import APIRouter, Depends, Query, status

from backend.api.dependencies import get_application_service
from backend.core.enums import ApplicationStatus, Priority, StatusGroup
from backend.schemas.application import (
    ApplicationCreate,
    ApplicationResponse,
    ApplicationUpdate,
)
from backend.services.application_service import ApplicationService

router = APIRouter(prefix="/applications", tags=["Applications"])
Service = ApplicationService


@router.post("", response_model=ApplicationResponse, status_code=status.HTTP_201_CREATED)
def create_application(data: ApplicationCreate, service: Service = Depends(get_application_service)):
    return service.create(data)


@router.get("", response_model=list[ApplicationResponse])
def list_applications(
    status: list[ApplicationStatus] | None = Query(default=None),
    status_group: StatusGroup | None = None,
    priority: Priority | None = None,
    category_id: int | None = None,
    company_id: int | None = None,
    service: Service = Depends(get_application_service),
):
    """e.g. `?status_group=active` or `?status=applied&status=interviewing`"""
    return service.search(
        [s.value for s in status or []],
        status_group,
        priority.value if priority else None,
        category_id,
        company_id,
    )


@router.get("/{application_id}", response_model=ApplicationResponse)
def get_application(application_id: int, service: Service = Depends(get_application_service)):
    return service.get(application_id)


@router.patch("/{application_id}", response_model=ApplicationResponse)
def update_application(
    application_id: int,
    data: ApplicationUpdate,
    service: Service = Depends(get_application_service),
):
    return service.update(application_id, data)


@router.delete("/{application_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_application(application_id: int, service: Service = Depends(get_application_service)):
    """Deletes the application with its progress."""
    service.delete(application_id)
