from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    name: str
    phone: str | None = None
    email: EmailStr
    description: str


class CreateUser(BaseUser):
    pass