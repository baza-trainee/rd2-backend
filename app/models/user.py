from sqlalchemy import Column, Integer, String, Text, Enum

from app.db.base_class import Base
from .admin import UserTypeEnum
from .base import TimestampedModel


class User(TimestampedModel, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(Enum(UserTypeEnum), nullable=False, default=UserTypeEnum.client)
    description = Column(Text)





