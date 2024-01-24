"""Configuration module."""


import os
from typing import List, Union

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Class for settings."""

    API_V1_STR: str = '/api'

    SERVER_NAME: str = 'socrat'
    SERVER_HOST: AnyHttpUrl = 'http://127.0.0.1:8000'

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        'http://127.0.0.1:3000', 'http://localhost:3000', 'http://localhost', 'http://0.0.0.0:3000',
    ]

    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    REFRESH_TOKEN_EXPIRE_MINUTES: int = os.getenv('REFRESH_TOKEN_EXPIRE_MINUTES')
    RESET_TOKEN_EXPIRE_MINUTES: int = os.getenv('RESET_TOKEN_EXPIRE_MINUTES')
    AUTHENTICATION__ALGORITHM: str = os.getenv('AUTHENTICATION__ALGORITHM')
    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY')
    JWT_REFRESH_SECRET_KEY: str = os.getenv('JWT_REFRESH_SECRET_KEY')

    SMTP_SERVER: str = os.getenv('SMTP_SERVER')
    SMTP_PORT: int = int(os.getenv('SMTP_PORT'))
    SMTP_USER_NAME: str = os.getenv('SMTP_USER_NAME')
    SMTP_PASSWORD: str = os.getenv('SMTP_PASSWORD')
    BASE_URL: str = os.getenv('BASE_URL')

    @field_validator('BACKEND_CORS_ORIGINS', mode='before')
    @classmethod
    def assemble_cors_origins(cls, vv: Union[str, List[str]]) -> Union[List[str], str]:
        """Assemble CORS origins."""
        if isinstance(vv, str) and not vv.startswith('['):
            return [el.strip() for el in vv.split(',')]
        elif isinstance(vv, (list, str)):
            return vv
        raise ValueError(vv)

    PROJECT_NAME: str = 'socrat'


settings = Settings()
