from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseLogo(BaseModel):
    filename: str
    path: str
    description: str


class LogoUpload(BaseModel):
    id: int
    created_at: datetime
    description: str


class LogoList(BaseModel):
    id: int
    filename: str
    description: str
    path: str
