
from typing import Any

from fastapi import APIRouter

from app.api.users import routes as user_routes


api_router = APIRouter()

api_router.include_router(user_routes.router, prefix="/user", tags=["user"])


@api_router.post("/alive")
def alive() -> Any:
    """
    Default alive endpoint
    """
    return {"status": "ok"}

