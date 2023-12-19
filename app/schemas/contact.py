from os import getenv
from typing import Optional

from pydantic import BaseModel, EmailStr


class ContactBase(BaseModel):
    phone: Optional[str] | None
    email: Optional[EmailStr] | None


class UpdateContact(ContactBase):
    phone: Optional[str] | None
    email: Optional[EmailStr] | None


class PhoneCreate(BaseModel):
    phone: str


class PhoneUpdate(BaseModel):
    phone: str


class EmailCreate(BaseModel):
    email: EmailStr


class EmailUpdate(BaseModel):
    phone: EmailStr


class ContactPhone(BaseModel):
    phone: str


class ContactEmail(BaseModel):
    email: EmailStr

# class ContactPhoneCreate(BaseModel):
#     phone: str
#
#
# class ContactEmailCreate(BaseModel):
#     email: EmailStr
#