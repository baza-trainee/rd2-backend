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
        orm_mode = True



class AdminLogin(BaseModel):
    email: EmailStr
    password: str


class AdminUpdate(BaseModel):
    pass