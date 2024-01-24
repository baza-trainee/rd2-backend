"""Module containing user-related schemas for data validation and serialization."""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class MessageSchema(BaseModel):
    """Schema representing a message."""

    msg: str
    created_at: datetime

    class Config(object):
        """Configuration settings for the model."""

        from_attributes = True


class BaseUser(BaseModel):
    """Base schema for a user."""

    name: str
    surname: str
    phone: str
    email: EmailStr
    messages: Optional[List[MessageSchema]] = None


class CreateUser(BaseModel):
    """Schema for creating a new user."""

    name: str
    surname: str
    phone: str
    email: EmailStr


class ListUser(BaseModel):
    """Schema for listing a user."""

    id: int
    name: str
    surname: str
    phone: str
    email: EmailStr
