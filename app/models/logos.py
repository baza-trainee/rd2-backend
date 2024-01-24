"""Models for logos."""

from sqlalchemy import Column, Integer, String, Text

from app.db.base_class import Base

from .base import TimestampedModel


class Logo(TimestampedModel, Base):
    """Model representing a logo."""

    __tablename__ = 'logos'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    path = Column(String)
    description = Column(Text)
