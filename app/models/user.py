"""Models for user and message."""

from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from .admin import UserTypeEnum
from .base import TimestampedModel


class User(TimestampedModel, Base):
    """Model representing a user."""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(Enum(UserTypeEnum), nullable=False, default=UserTypeEnum.client)

    messages = relationship('Message', back_populates='users')


class Message(TimestampedModel, Base):
    """Model representing a message."""

    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    msg = Column(Text)

    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship('User', back_populates='messages')
