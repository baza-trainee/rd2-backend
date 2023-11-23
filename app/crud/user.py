from typing import Optional

from sqlalchemy.orm import Session

from app import schemas
from .base import CRUDBase
from app.models.user import User, Message


class UserCRUD(CRUDBase[User, schemas.BaseUser, schemas.BaseUser]):
    def add_message(self, db: Session, user, message) -> None:
        user.messages.append(message)
        db.commit()


crud_user = UserCRUD(User)

crud_message = CRUDBase(Message)
