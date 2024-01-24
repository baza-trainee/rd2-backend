
"""Dependencies for API endpoints."""

from datetime import datetime
from typing import Generator

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.crud.admin import crud_user
from app.db.session import SessionLocal
from app.models import Admin
from app.models.admin import UserTypeEnum
from app.utils import apikey_scheme, token_decode


def get_db() -> Generator:
    """Get database session."""
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(apikey_scheme), db: Session = Depends(get_db),
):
    """Get current user."""

    try:
        token_data = token_decode(token)
        if token_data.exp and datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token expired',
                headers={'WWW-Authenticate': 'Bearer'},
            )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    user = crud_user.get(db, id=token_data.sub)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Could not find user',
        )

    return user


def check_active_user(user: Admin = Depends(get_current_user)):
    """Check active user."""

    if user.is_active:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Not active account',
    )


def check_admin(user: Admin = Depends(check_active_user)):
    """Check admin."""
    if user.role == UserTypeEnum.superadmin:
        return user

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='Insufficient access rights',
        headers={'WWW-Authenticate': 'Bearer'},
    )
