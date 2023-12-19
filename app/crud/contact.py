from typing import Optional

from sqlalchemy.orm import Session

from app import schemas
from app.models.contact import Contact

from .base import CRUDBase


class ContactCRUD(CRUDBase[Contact, schemas.ContactBase, schemas.UpdateContact]):
    def check_contact(self, db: Session) -> Optional[Contact]:
        print(db.query(Contact).first())
        return db.query(Contact).first()

    # def check_email(self, db: Session) -> Optional[Contact]:
    #     return db.query(Contact).first().email



crud_contact = ContactCRUD(Contact)
