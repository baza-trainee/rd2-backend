from typing import Optional

from sqlalchemy.orm import Session

from .base import CRUDBase
from app.models.contact import Contact
from app import schemas


class ContactCRUD(CRUDBase[Contact, schemas.ContactBase, schemas.ContactUpdate]):
    def check_contact(self, db: Session) -> Optional[Contact]:
        return db.query(Contact).first()


crud_contact = ContactCRUD(Contact)
