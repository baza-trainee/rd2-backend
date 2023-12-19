from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.api.deps import get_current_user, get_db
from app.crud.contact import crud_contact
from app.models import Admin

from app.schemas import ContactBase, ContactPhone, ContactEmail, PhoneCreate, EmailCreate, UpdateContact


router = APIRouter()


# @router.put(
#     "/contact", response_model=ContactUpdate, status_code=status.HTTP_201_CREATED
# )
# def create_or_update_contact(
#     obj_in: ContactUpdate,
#     db: Session = Depends(get_db),
#     current_user: Admin = Depends(get_current_user),
# ):
#     contact = crud_contact.check_contact(db)
#
#     if contact:
#         contact_id = contact.id
#         contact = crud_contact.get(db, contact_id)
#         updated_contact = crud_contact.update(db, db_obj=contact, obj_in=obj_in)
#         return updated_contact
#     else:
#         created_contact = crud_contact.create(db, obj_in=obj_in)
#         return created_contact

@router.put(
    "/contacts/phones", response_model=UpdateContact, status_code=status.HTTP_201_CREATED
)
def create_or_update_phone(
    obj_in: PhoneCreate,
    db: Session = Depends(get_db),
    current_user: Admin = Depends(get_current_user),
):
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
    "/contacts/emails", response_model=UpdateContact, status_code=status.HTTP_201_CREATED
)
def create_or_update_email(
    obj_in: EmailCreate,
    db: Session = Depends(get_db),
    current_user: Admin = Depends(get_current_user),
):
    email = crud_contact.check_contact(db)
    if email:
        contact_id = email.id
        contact = crud_contact.get(db, contact_id)
        updated_email = crud_contact.update(db, db_obj=contact, obj_in=obj_in)
        return updated_email
    else:
        created_email = crud_contact.create(db, obj_in=obj_in)
        return created_email

#
# @router.get("/contacts", response_model=ContactBase, status_code=status.HTTP_200_OK)
# def get_contact(db: Session = Depends(get_db)):
#     contact = crud_contact.check_phone(db)
#     if contact is None:
#         raise HTTPException(status_code=404, detail="Contact not found")
#     contact_id = contact.id
#     contact = crud_contact.get(db, id=contact_id)
#     return contact


@router.get("/contacts/phones", response_model=ContactPhone, status_code=status.HTTP_200_OK)
def get_phones(db: Session = Depends(get_db)):
    contact = crud_contact.check_contact(db)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    contact_id = contact.id
    contact = crud_contact.get(db, id=contact_id)
    phone = contact.phone
    return {"phone": phone}


@router.get("/contacts/emails", response_model=ContactEmail, status_code=status.HTTP_200_OK)
def get_emails(db: Session = Depends(get_db)):

    contact = crud_contact.check_contact(db)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    contact_id = contact.id
    contact = crud_contact.get(db, id=contact_id)

    email = contact.email
    return {"email": email}



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
