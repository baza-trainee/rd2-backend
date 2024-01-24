"""Routes for contact."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.api.deps import get_current_user, get_db
from app.crud.contact import crud_contact
from app.models import Admin
from app.schemas import ContactEmail, ContactPhone, EmailCreate, PhoneCreate, UpdateContact

router = APIRouter()


@router.put(
    '/contacts/phones', response_model=UpdateContact, status_code=status.HTTP_201_CREATED
)
def create_or_update_phone(
    obj_in: PhoneCreate,
    db: Session = Depends(get_db),
    current_user: Admin = Depends(get_current_user),
):
    """Create or update phone."""
    phone = crud_contact.check_contact(db)
    if phone:
        contact_id = phone.id
        contact = crud_contact.get(db, contact_id)
        updated_phone = crud_contact.update(db, db_obj=contact, obj_in=obj_in)
        return updated_phone
    else:
        created_phone = crud_contact.create(db, obj_in=obj_in)
        return created_phone


@router.put(
    '/contacts/emails', response_model=UpdateContact, status_code=status.HTTP_201_CREATED
)
def create_or_update_email(
    obj_in: EmailCreate,
    db: Session = Depends(get_db),
    current_user: Admin = Depends(get_current_user),
):
    """Create or update email."""
    email = crud_contact.check_contact(db)
    if email:
        contact_id = email.id
        contact = crud_contact.get(db, contact_id)
        updated_email = crud_contact.update(db, db_obj=contact, obj_in=obj_in)
        return updated_email
    else:
        created_email = crud_contact.create(db, obj_in=obj_in)
        return created_email


@router.get('/contacts/phones', response_model=ContactPhone, status_code=status.HTTP_200_OK)
def get_phones(db: Session = Depends(get_db)):
    """Get phones."""
    contact = crud_contact.check_contact(db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact not found')
    contact_id = contact.id
    contact = crud_contact.get(db, id=contact_id)
    phone = contact.phone
    return {'phone': phone}


@router.get('/contacts/emails', response_model=ContactEmail, status_code=status.HTTP_200_OK)
def get_emails(db: Session = Depends(get_db)):
    """Get emails."""
    contact = crud_contact.check_contact(db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact not found')
    contact_id = contact.id
    contact = crud_contact.get(db, id=contact_id)
    email = contact.email
    return {'email': email}


@router.delete('/contact', status_code=status.HTTP_204_NO_CONTENT)
def remove_contact(
    db: Session = Depends(get_db), current_user: Admin = Depends(get_current_user)
):
    """Remove contact."""
    contact = crud_contact.check_contact(db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact not found')

    contact_id = contact.id
    crud_contact.remove(db, id=contact_id)
    return contact
