"""Models for contact information."""

from sqlalchemy import Column, Integer, String

from app.db.base_class import Base

from .base import TimestampedModel


class Contact(TimestampedModel, Base):
    """Model representing a contact."""

    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String)
    email = Column(String)
