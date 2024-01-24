"""Utility functions for app."""

from datetime import datetime, timedelta
from typing import Any, Union

import jwt
from fastapi.security import APIKeyHeader
from passlib.context import CryptContext

from app.core.config import settings
from app.schemas.token import TokenPayload

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
apikey_scheme = APIKeyHeader(name='Authorization')


def get_hashed_password(password: str) -> str:
    """Hash a password."""
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    """Verify a password against its hash."""
    return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """Create an access token."""
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        )

    to_encode = {'exp': expires_delta, 'sub': str(subject)}
    return jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, settings.AUTHENTICATION__ALGORITHM,
    )


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """Create a refresh token."""
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES,
        )

    to_encode = {'exp': expires_delta, 'sub': str(subject)}
    return jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, settings.AUTHENTICATION__ALGORITHM,
    )


def create_reset_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """Create a reset token."""
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.RESET_TOKEN_EXPIRE_MINUTES,
        )

    to_encode = {'exp': expires_delta, 'sub': str(subject)}
    return jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, settings.AUTHENTICATION__ALGORITHM,
    )


def token_decode(token: str):
    """Decode a token."""
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=settings.AUTHENTICATION__ALGORITHM,
        )
    except jwt.ExpiredSignatureError:
        return None
    except Exception:
        return False
    return TokenPayload(**payload)
