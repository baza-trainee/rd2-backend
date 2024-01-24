"""Modelo de datos para el CRUD de logos."""

from app.models.logos import Logo

from .base import CRUDBase

crud_logo = CRUDBase(Logo)
