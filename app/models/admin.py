import enum

from sqlalchemy import Column, Integer, String, Boolean, Enum

from app.db.base_class import Base
from .base import TimestampedModel


class UserTypeEnum(enum.Enum):
    client = "user"
    superadmin = "superuser"


class Admin(TimestampedModel, Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(UserTypeEnum), nullable=False)
    is_superuser = Column(Boolean, default=False)
