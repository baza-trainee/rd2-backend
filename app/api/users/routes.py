from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from app import schemas
from app.api.deps import get_db
from app.crud.user import crud_user
from app.email_setting import send_welcom_letter
from fastapi import HTTPException
import smtplib

router = APIRouter()


@router.post("create-user", response_model=schemas.BaseUser, status_code=status.HTTP_201_CREATED)
def create_user(obj_in: schemas.CreateUser, db: Session = Depends(get_db)):

    existing_user = crud_user.get_user_by_email(db, email=obj_in.email)

    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists, please send message 'email'")

    users = crud_user.create(db, obj_in=obj_in)

    user_email = users.email
    donat_url = f"#"
    send_welcom_letter(user_email, donat_url)
    try:
        send_welcom_letter(user_email, donat_url)
    except smtplib.SMTPException as e:
        raise HTTPException(status_code=500, detail=f"Failed to send welcome email: {str(e)}")
    return users


@router.get("users", response_model=None, status_code=status.HTTP_200_OK)
def get_user_list(db: Session = Depends(get_db)):
    users = crud_user.get_multi(db)

    return users
