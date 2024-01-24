"""Models for admin users."""

import enum

from sqlalchemy import Boolean, Column, Enum, Integer, String

from app.db.base_class import Base

from .base import TimestampedModel


class UserTypeEnum(enum.Enum):
    """Enum representing user types."""

    client = 'user'
    superadmin = 'superuser'


class Admin(TimestampedModel, Base):
    """Model representing an admin user."""

    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(UserTypeEnum), nullable=False)
    is_superuser = Column(Boolean, default=False)
