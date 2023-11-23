from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr


class MessageSchema(BaseModel):
    msg: str
    created_at: datetime

    class Config:
        from_attributes = True


class BaseUser(BaseModel):
    name: str
    surname: str
    phone: str
    email: EmailStr
    messages: Optional[List[MessageSchema]] = None


class CreateUser(BaseModel):
    name: str
    surname: str
    phone: str
    email: EmailStr


class ListUser(BaseModel):
    id: int
    name: str
    surname: str
    phone: str
    email: EmailStr



