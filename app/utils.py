import os
from datetime import datetime, timedelta
from typing import Any, Union

import jwt
from fastapi.security import APIKeyHeader
from passlib.context import CryptContext

from app.core.config import settings
from app.schemas.token import TokenPayload

# from jose import jwt



# from schemas.token import RefreshToken

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
apikey_scheme = APIKeyHeader(name="Authorization")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, settings.AUTHENTICATION__ALGORITHM
    )
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(

        to_encode, settings.JWT_SECRET_KEY, settings.AUTHENTICATION__ALGORITHM

    )
    return encoded_jwt


def create_reset_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.RESET_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, settings.AUTHENTICATION__ALGORITHM
    )
    return encoded_jwt


def token_decode(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=settings.AUTHENTICATION__ALGORITHM,
        )
        token_data = TokenPayload(**payload)
        return token_data
    except jwt.ExpiredSignatureError:

        return None
    except Exception:
        return False

