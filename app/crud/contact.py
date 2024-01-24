"""Module for CRUD operations on Contact model."""

from typing import Optional

from sqlalchemy.orm import Session

from app import schemas
from app.models.contact import Contact

from .base import CRUDBase


class ContactCRUD(CRUDBase[Contact, schemas.ContactBase, schemas.UpdateContact]):
    """Class for CRUD operations on Contact model."""

    def check_contact(self, db: Session) -> Optional[Contact]:
        """Check if contact exists."""
        return db.query(Contact).first()


crud_contact = ContactCRUD(Contact)
