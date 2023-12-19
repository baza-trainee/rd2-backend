import smtplib

import time

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from starlette import status
from starlette.background import BackgroundTasks


from app.api.deps import get_current_user, get_db
from app.crud.user import crud_message, crud_user
from app.email_setting import EmailService
from app.exel_generate import generate_exel_report
from app.models import Admin
from app.schemas import BaseUser, CreateUser, ListUser, MessageSchema


router = APIRouter()


@router.get(
    "/download-report",
    response_class=FileResponse,
)
def get_report(
    db: Session = Depends(get_db), current_user: Admin = Depends(get_current_user)
):
    report_path = generate_exel_report(db)
    return FileResponse(report_path, filename="report.xlsx")


@router.post(
    "/create-user", response_model=BaseUser, status_code=status.HTTP_201_CREATED
)
def create_user(

    background_tasks: BackgroundTasks,
    obj_in: CreateUser,
    message: MessageSchema,
    db: Session = Depends(get_db)

):
    user = crud_user.get_user_by_email(db, email=obj_in.email)
    message = crud_message.create(db, obj_in=message)

    if user:
        crud_user.add_message(db, user, message)

    else:
        user = crud_user.create(db, obj_in=obj_in)
        crud_user.add_message(db, user, message)

    user_email = user.email
    donat_url = f"#"
    subject = "State Enterprise R&D Center for Overuse Issues of Georesources"
    body = (
        f"Hello, thank you for your question. We will contact you shortly\n"
        f"If we support Socrat project, follow the link for support {donat_url}\n"
    )


    send_message = EmailService(user_email, subject, body)
    background_tasks.add_task(send_message.send_message)

    #
    try:
        send_message
    except smtplib.SMTPException as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to send welcome email: {str(e)}"
        )
    return user


@router.get("/", response_model=List[ListUser], status_code=status.HTTP_200_OK)
def get_user_list(
    db: Session = Depends(get_db), current_user: Admin = Depends(get_current_user)
):
    users = crud_user.get_multi(db)
    return users


@router.get("/{user_id}", response_model=BaseUser, status_code=status.HTTP_200_OK)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: Admin = Depends(get_current_user),
):
    user = crud_user.get(db, id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")


    return user
