"""Module containing schemas for message handling and representation."""

from pydantic import BaseModel


class ResponseMessage(BaseModel):
    """Schema representing a response message."""

    message: str
