from pydantic import BaseModel, EmailStr
from typing import Optional
from os import getenv


class ContactBase(BaseModel):
    email: EmailStr
    phone: str


class ContactCreate(BaseModel):
    phone: str
    email: EmailStr


class ContactUpdate(BaseModel):
    phone: str
    email: EmailStr
