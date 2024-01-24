"""Schemas for reports related models."""

from sqlalchemy import Column, Integer, String

from app.db.base_class import Base

from .base import TimestampedModel


class Report(TimestampedModel, Base):
    """Model representing a report."""

    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, nullable=False)
    path = Column(String, unique=True, nullable=False)


class PrivatePolicy(TimestampedModel, Base):
    """Model representing a private policy."""

    __tablename__ = 'privatepolicy'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, nullable=False)
    path = Column(String, unique=True, nullable=False)


class Rules(TimestampedModel, Base):
    """Model representing a rules."""

    __tablename__ = 'rules'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, nullable=False)
    path = Column(String, unique=True, nullable=False)
