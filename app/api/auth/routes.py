from typing import Any

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from starlette import status

from app import schemas
from app.api.deps import get_db
from app.crud.admin import crud_user
from app.email_setting import send_welcom_letter
from fastapi import HTTPException
import smtplib

from app.utils import create_access_token, create_refresh_token

router = APIRouter()


@router.post("/login", response_model=schemas.Token)
def login(db: Session = Depends(get_db), user_data: schemas.AdminLogin = Body(...)) -> Any:
    """
    Endpoint to allow users to login

    :param db: DB session
    :param user_data: Body object with email and password
    :return: jwt access and refresh token
    """
    user = crud_user.authenticate(db, email=user_data.email, password=user_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    return {
        "access_token": create_access_token({"user_id": user.id}),
        "refresh_token": create_refresh_token({"user_id": user.id}),
    }
