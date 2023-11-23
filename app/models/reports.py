
from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.dialects.postgresql import BYTEA

from app.db.base_class import Base
from .base import TimestampedModel


class Report(TimestampedModel, Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, nullable=False)
    path = Column(String, unique=True, nullable=False)
