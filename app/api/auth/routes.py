from typing import Any


from fastapi import APIRouter, Body, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from starlette import status

from app import schemas
from app.api.deps import get_current_user, get_db
from app.core.config import settings
from app.crud.admin import crud_user
from app.email_setting import EmailService
from app.models import Admin
from app.schemas import ResponseMessage
from app.utils import (
    create_access_token,
    create_refresh_token,
    create_reset_token,
    get_hashed_password,
    token_decode,
    verify_password,
)

router = APIRouter()


@router.post("/login", response_model=schemas.Token)
def login(request: Request,
    db: Session = Depends(get_db), user_data: schemas.AdminLogin = Body(...)
) -> Any:
    """
    Endpoint to allow users to login

    :param db: DB session
    :param user_data: Body object with email and password
    :return: jwt access and refresh token
    """

    # domain = request.headers
    # print(f"-------------------------------------Request from client IP: {domain}")
    user = crud_user.authenticate(
        db, email=user_data.email, password=user_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    return {
        "access_token": create_access_token(user.id),
        "refresh_token": create_refresh_token(user.id),
    }


@router.post("/refresh", response_model=schemas.RefreshToken)
def refresh_token(token: str, db: Session = Depends(get_db),):
    """

    :param token: refresh token
    :param db: DB session
    :return: if time expired return access_token, else return refresh_token
    """
    decoded_token = token_decode(token).sub
    if decoded_token is False:
        raise HTTPException(status_code=400, detail="Invalid token")

    user_id = decoded_token

    user = crud_user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if decoded_token is None:
        new_access_token = create_access_token(user.id)
        return {"access_token": new_access_token}

    new_refresh_token = create_refresh_token(user.id)
    return {"refresh_token": new_refresh_token}


@router.post(
    "/forgot-password",
    response_model=schemas.ResponseMessage,
    status_code=status.HTTP_200_OK,
)
def forgot_password(
    user_data: schemas.ForgotPassword = Body(...), db: Session = Depends(get_db)
):
    user = crud_user.get_user_by_email(db, email=user_data.email)
    if not user:
        return ResponseMessage(
            message=f"An email has been sent to {user_data.email} with a link to reset your password."
        )

    reset_token = create_reset_token(user.id)
    base_url = settings.BASE_URL  # test URL
    reset_url = f"{base_url}/reset-password/{reset_token}"
    subject = "Password reset"
    body = f"To reset your password, follow the following link: {reset_url}"
    EmailService(user_data.email, subject, body).send_message()

    return ResponseMessage(
        message=f"An email has been sent to {user_data.email} with a link to reset your password."
    )


@router.post(
    "/reset-password", response_model=ResponseMessage, status_code=status.HTTP_200_OK
)
def reset_password(
    reset_token: str,
    user_data: schemas.ResetPassword = Body(...),
    db: Session = Depends(get_db),
):
    user_id = token_decode(reset_token).sub

    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid reset token")
    user = crud_user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user_data.new_password == user_data.confirm_password:
        hashed_password = get_hashed_password(user_data.new_password)
        user.password = hashed_password
        db.commit()
        return ResponseMessage(message="Password reset successfully")
    else:
        raise HTTPException(status_code=400, detail="Passwords do not match")


@router.put(
    "/change-password", response_model=ResponseMessage, status_code=status.HTTP_200_OK
)
def change_password(
    current_user: Admin = Depends(get_current_user),
    user_data: schemas.ChangePassword = Body(...),
    db: Session = Depends(get_db),
):
    if not verify_password(user_data.password, current_user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    user = current_user
    if user_data.new_password == user_data.confirm_password:
        hashed_password = get_hashed_password(user_data.new_password)
        user.password = hashed_password
        db.commit()
        return ResponseMessage(message="Password change successfully")
    else:
        raise HTTPException(status_code=400, detail="Passwords do not match")
