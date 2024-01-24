"""Module containing base models for SQLAlchemy models."""

from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func


class TimestampedModel:
    """Base model with timestamp fields."""

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(),
    )
