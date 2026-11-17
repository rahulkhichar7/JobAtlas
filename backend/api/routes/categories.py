from fastapi import APIRouter, Depends, status

from backend.api.dependencies import get_category_service
from backend.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate
from backend.services.category_service import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])
Service = CategoryService


@router.post("", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(data: CategoryCreate, service: Service = Depends(get_category_service)):
    return service.create(data)


@router.get("", response_model=list[CategoryResponse])
def list_categories(service: Service = Depends(get_category_service)):
    return service.get_all()


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, service: Service = Depends(get_category_service)):
    return service.get(category_id)


@router.patch("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int, data: CategoryUpdate, service: Service = Depends(get_category_service)
):
    return service.update(category_id, data)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, service: Service = Depends(get_category_service)):
    """Deletes the category and everything under it."""
    service.delete(category_id)
