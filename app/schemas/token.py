"""Module containing schemas for token handling and validation."""

from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    """Schema representing a token with access and refresh tokens."""

    access_token: str
    refresh_token: str


class RefreshToken(Token):
    """Schema extending the basic Token with optional access and refresh tokens."""

    access_token: Optional[str] = None
    refresh_token: Optional[str] = None


class TokenPayload(BaseModel):
    """Schema representing the payload part of a JWT token."""

    sub: str = None  # Subject (usually a user identifier)
    exp: int = None  # Expiration time
