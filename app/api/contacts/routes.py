from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.api.deps import get_current_user, get_db
from app.crud.contact import crud_contact
from app.models import Admin
from app.schemas import ContactBase, ContactUpdate

router = APIRouter()


@router.put(
    "/contact", response_model=ContactUpdate, status_code=status.HTTP_201_CREATED
)
def create_or_update_contact(
    obj_in: ContactUpdate,
    db: Session = Depends(get_db),
    current_user: Admin = Depends(get_current_user),
):
    contact = crud_contact.check_contact(db)

    if contact:
        contact_id = contact.id
        contact = crud_contact.get(db, contact_id)
        updated_contact = crud_contact.update(db, db_obj=contact, obj_in=obj_in)
        return updated_contact
    else:
        created_contact = crud_contact.create(db, obj_in=obj_in)
        return created_contact


@router.get("/contacts", response_model=ContactBase, status_code=status.HTTP_200_OK)
def get_contact(
    db: Session = Depends(get_db), current_user: Admin = Depends(get_current_user)
):
    contact = crud_contact.check_contact(db)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    contact_id = contact.id
    contact = crud_contact.get(db, id=contact_id)
    return contact


@router.delete("/contact", status_code=status.HTTP_204_NO_CONTENT)
def remove_contact(
    db: Session = Depends(get_db), current_user: Admin = Depends(get_current_user)
):
    contact = crud_contact.check_contact(db)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")

    contact_id = contact.id
    crud_contact.remove(db, id=contact_id)
    return contact
