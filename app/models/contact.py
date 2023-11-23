import os

from sqlalchemy import Column, Integer, String, Text, Enum
from app.db.base_class import Base
from .base import TimestampedModel



class Contact(TimestampedModel, Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String)
    email = Column(String)

