from pydantic import BaseModel, EmailStr

from app.models.admin import UserTypeEnum


class BaseAdmin(BaseModel):
    name: str
    email: EmailStr
    password: str
    is_active: bool
    description: str
    role: UserTypeEnum


class AdminCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    is_superuser: bool
    role: UserTypeEnum

    class Config:
        from_attributes = True


class AdminLogin(BaseModel):
    email: EmailStr
    password: str


class ForgotPassword(BaseModel):
    email: EmailStr


class ResetPassword(BaseModel):
    new_password: str
    confirm_password: str


class ChangePassword(BaseModel):
    password: str
    new_password: str
    confirm_password: str


class AdminUpdate(BaseModel):
    pass