"""Module containing schemas for logo management and representation."""

from datetime import datetime

from pydantic import BaseModel


class BaseLogo(BaseModel):
    """Schema representing the basic information of a logo."""

    filename: str
    path: str
    description: str


class LogoUpload(BaseModel):
    """Schema for uploading a logo with its metadata."""

    id: int
    created_at: datetime
    description: str


class LogoList(BaseModel):
    """Schema for listing logos with their details."""

    id: int
    filename: str
    description: str
    path: str
