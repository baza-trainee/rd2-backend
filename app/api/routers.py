from fastapi import APIRouter

from app.api.auth import routes as auth_routes
from app.api.contacts import routes as contact_routes
from app.api.logos import routes as logos_routes
from app.api.reports import routes as report_routes
from app.api.users import routes as user_routes

api_router = APIRouter()


api_router.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
api_router.include_router(user_routes.router, prefix="/user", tags=["user"])
api_router.include_router(contact_routes.router, prefix="/contact", tags=["contact"])
api_router.include_router(report_routes.router, prefix="/report", tags=["reports"])
api_router.include_router(logos_routes.router, prefix="/logo", tags=["logo"])
