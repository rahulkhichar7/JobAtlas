from fastapi import APIRouter

from backend.api.routes import applications, categories, companies, graph, jobs, progress

api_router = APIRouter()

api_router.include_router(graph.router)
api_router.include_router(categories.router)
api_router.include_router(companies.router)
api_router.include_router(jobs.router)
api_router.include_router(applications.router)
api_router.include_router(progress.router)
