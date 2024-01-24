"""Module for CRUD operations on Admin model."""

from typing import Optional

from pydantic import EmailStr
from sqlalchemy.orm import Session

from app import schemas
from app.models.admin import Admin
from app.utils import verify_password

from .base import CRUDBase


class AdminCRUD(CRUDBase[Admin, schemas.AdminCreate, schemas.AdminUpdate]):
    """Class for CRUD operations on Admin model."""

    def get_user_by_email(self, db: Session, email: EmailStr) -> Optional[Admin]:
        """Get user by email."""
        return db.query(Admin).filter(Admin.email == email).first()

    def authenticate(self, db: Session, email: str, password: str) -> Optional[Admin]:
        """Authenticate user."""
        user = self.get_user_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user


crud_user = AdminCRUD(Admin)
