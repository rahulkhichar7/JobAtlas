from fastapi import APIRouter, Depends, status

from backend.api.dependencies import get_company_service
from backend.schemas.company import CompanyCreate, CompanyResponse, CompanyUpdate
from backend.services.company_service import CompanyService

router = APIRouter(prefix="/companies", tags=["Companies"])
Service = CompanyService


@router.post("", response_model=CompanyResponse, status_code=status.HTTP_201_CREATED)
def create_company(data: CompanyCreate, service: Service = Depends(get_company_service)):
    return service.create(data)


@router.get("", response_model=list[CompanyResponse])
def list_companies(
    category_id: int | None = None,
    search: str | None = None,
    service: Service = Depends(get_company_service),
):
    return service.search(category_id, search)


@router.get("/{company_id}", response_model=CompanyResponse)
def get_company(company_id: int, service: Service = Depends(get_company_service)):
    return service.get(company_id)


@router.patch("/{company_id}", response_model=CompanyResponse)
def update_company(
    company_id: int, data: CompanyUpdate, service: Service = Depends(get_company_service)
):
    return service.update(company_id, data)


@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_company(company_id: int, service: Service = Depends(get_company_service)):
    """Deletes the company with its jobs, applications and progress."""
    service.delete(company_id)
