"""Module containing schemas for admin-related operations and data validation."""

from pydantic import BaseModel, EmailStr

from app.models.admin import UserTypeEnum


class BaseAdmin(BaseModel):
    """Base schema for an admin user."""

    name: str
    email: EmailStr
    password: str
    is_active: bool
    description: str
    role: UserTypeEnum


class AdminCreate(BaseModel):
    """Schema for creating a new admin user."""

    name: str
    email: EmailStr
    password: str
    is_superuser: bool
    role: UserTypeEnum

    class Config(object):
        """Configuration settings for the model."""

        from_attributes = True


class AdminLogin(BaseModel):
    """Schema for admin user login."""

    email: EmailStr
    password: str


class ForgotPassword(BaseModel):
    """Schema for requesting a password reset."""

    email: EmailStr


class ResetPassword(BaseModel):
    """Schema for resetting an admin user's password."""

    new_password: str
    confirm_password: str


class ChangePassword(BaseModel):
    """Schema for changing an existing admin user's password."""

    password: str
    new_password: str
    confirm_password: str


class AdminUpdate(BaseModel):
    """Schema for updating an admin user. Currently empty, but may be extended in the future."""

    pass  # or remove 'pass' if you plan to add fields or methods
