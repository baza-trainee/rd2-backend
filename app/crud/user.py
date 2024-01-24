"""Module for CRUD operations on User model."""

from sqlalchemy.orm import Session

from app import schemas
from app.models.user import Message, User

from .base import CRUDBase


class UserCRUD(CRUDBase[User, schemas.BaseUser, schemas.BaseUser]):
    """Class for CRUD operations on User model."""

    def add_message(self, db: Session, user, message) -> None:
        """Add message to user."""
        user.messages.append(message)
        db.commit()


crud_user = UserCRUD(User)

crud_message = CRUDBase(Message)
