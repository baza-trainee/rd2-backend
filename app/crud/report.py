"""Module for CRUD operations on Report model."""

from typing import Optional

from sqlalchemy.orm import Session

from app import schemas
from app.models.reports import PrivatePolicy, Report, Rules

from .base import CRUDBase


class ReportCRUD(CRUDBase[Report, schemas.BaseFile, schemas.ReportResponse]):
    """Class for CRUD operations on Report model."""

    def check_report(self, db: Session) -> Optional[Report]:
        """Check if report exists."""
        return db.query(Report).first()


crud_report = ReportCRUD(Report)


class PrivatePolicyCRUD(CRUDBase[PrivatePolicy, schemas.BaseFile, schemas.ReportResponse]):
    """Class for CRUD operations on PrivatePolicy model."""

    def check_privatepolicy(self, db: Session) -> Optional[PrivatePolicy]:
        """Check if private policy exists."""
        return db.query(PrivatePolicy).first()


crud_privatepolicy = PrivatePolicyCRUD(PrivatePolicy)


class RuleCRUD(CRUDBase[Rules, schemas.BaseFile, schemas.ReportResponse]):
    """Class for CRUD operations on Rules model."""

    def check_rule(self, db: Session) -> Optional[Rules]:
        """Check if rule exists."""
        return db.query(Rules).first()


crud_rules = RuleCRUD(Rules)
