from os import getenv
from typing import Optional

from pydantic import BaseModel, EmailStr


class ContactBase(BaseModel):
    email: EmailStr
    phone: str


class ContactCreate(BaseModel):
    phone: str
    email: EmailStr


class ContactUpdate(BaseModel):
    phone: str
    email: EmailStr
