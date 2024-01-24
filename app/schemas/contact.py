"""Module containing schemas for contact information, including phone and email."""

from typing import Optional

from pydantic import BaseModel, EmailStr


class ContactBase(BaseModel):
    """Base schema for contact information, including optional phone and email."""

    phone: Optional[str] | None
    email: Optional[EmailStr] | None


class UpdateContact(ContactBase):
    """Schema for updating contact information."""

    phone: Optional[str] | None
    email: Optional[EmailStr] | None


class PhoneCreate(BaseModel):
    """Schema for creating a phone contact."""

    phone: str


class PhoneUpdate(BaseModel):
    """Schema for updating a phone contact."""

    phone: str


class EmailCreate(BaseModel):
    """Schema for creating an email contact."""

    email: EmailStr


class EmailUpdate(BaseModel):
    """Schema for updating an email contact."""

    email: EmailStr


class ContactPhone(BaseModel):
    """Schema representing a phone contact."""

    phone: str


class ContactEmail(BaseModel):
    """Schema representing an email contact."""

    email: EmailStr
