from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from app import schemas
from app.api.deps import get_db
from app.crud.user import crud_user

router = APIRouter()


@router.post("/", response_model=schemas.BaseUser, status_code=status.HTTP_201_CREATED)
def create_user(obj_in: schemas.CreateUser, db: Session = Depends(get_db)):
    users = crud_user.create(db, obj_in=obj_in)

    return users
