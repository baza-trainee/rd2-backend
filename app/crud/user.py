from typing import Optional

from sqlalchemy.orm import Session

from app import schemas
from app.models.user import Message, User

from .base import CRUDBase


class UserCRUD(CRUDBase[User, schemas.BaseUser, schemas.BaseUser]):
    def add_message(self, db: Session, user, message) -> None:
        user.messages.append(message)
        db.commit()


crud_user = UserCRUD(User)

crud_message = CRUDBase(Message)
