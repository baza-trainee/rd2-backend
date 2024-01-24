"""Main module for FastAPI application."""

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routers import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f'{settings.API_V1_STR}/openapi.json',
)

# Set up CORS
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'],
        allow_headers=[
            'Content-Type',
            'Set-cookie',
            'Access-Control-Allow-Headers',
            'Access-Control-Allow-Origin',
            'Authorizations',
            'accept',
            'Origin',
        ],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
