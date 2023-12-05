from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseFile(BaseModel):
    filename: str
    path: str


class ReportResponse(BaseModel):
    id: int
    created_at: datetime


class ReportDetail(BaseModel):
    id: int
    created_at: datetime
    path: Optional[str] | None
