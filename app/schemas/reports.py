"""Module containing schemas for report handling and representation."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseFile(BaseModel):
    """Schema representing the basic information of a file."""

    filename: str
    path: str


class ReportResponse(BaseModel):
    """Schema for basic response information of a report."""

    id: int
    created_at: datetime


class ReportDetail(BaseModel):
    """Detailed schema for a report including optional path information."""

    id: int
    created_at: datetime
    path: Optional[str] | None
