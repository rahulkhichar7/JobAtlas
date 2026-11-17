from datetime import date

from fastapi import APIRouter, Depends, Query

from backend.api.dependencies import get_graph_service
from backend.core.enums import ApplicationStatus, JobType, Priority, StatusGroup
from backend.services.graph_service import GraphFilters, GraphService

router = APIRouter(tags=["Graph & Dashboard"])
Service = GraphService


@router.get("/graph")
def get_graph(
    category_id: int | None = None,
    company_id: list[int] | None = Query(default=None),
    search: str | None = None,
    job_type: list[JobType] | None = Query(default=None),
    location: str | None = None,
    status: list[ApplicationStatus] | None = Query(default=None),
    status_group: StatusGroup | None = None,
    priority: list[Priority] | None = Query(default=None),
    applied_from: date | None = None,
    applied_to: date | None = None,
    include_progress: bool = True,
    service: Service = Depends(get_graph_service),
):
    """
    Graph of one category (`category_id`) or of everything (global root).

    Filters rebuild the graph: e.g. `?category_id=1&status_group=active` keeps only
    companies that have an ongoing application, and only those jobs/applications.
    Every node has `id`, `type` (root/category/company/job/application/progress),
    `label`, `parent` and the full record in `data`.
    """
    filters = GraphFilters(
        category_id=category_id,
        company_ids=company_id or [],
        search=search,
        job_types=[t.value for t in job_type or []],
        location=location,
        statuses=[s.value for s in status or []],
        status_group=status_group.value if status_group else None,
        priorities=[p.value for p in priority or []],
        applied_from=applied_from,
        applied_to=applied_to,
        include_progress=include_progress,
    )
    return service.build_graph(filters)


@router.get("/stats")
def get_stats(
    category_id: int | None = None,
    days: int = Query(default=14, ge=1, le=365, description="Look-ahead for upcoming items"),
    service: Service = Depends(get_graph_service),
):
    """Dashboard numbers, rates, upcoming deadlines and next actions."""
    return service.stats(category_id, days)


@router.get("/meta")
def get_meta():
    """Allowed values for dropdowns (statuses, priorities, job types...)."""
    return GraphService.meta()
