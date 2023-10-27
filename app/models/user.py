from sqlalchemy import Column, Integer, String, Text


from app.db.base_class import Base
from .base import TimestampedModel


class User(TimestampedModel, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text)





