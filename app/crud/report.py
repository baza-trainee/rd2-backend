from typing import Optional

from sqlalchemy.orm import Session

from app import schemas
from app.models.reports import Report

from .base import CRUDBase


class ReportCRUD(CRUDBase[Report, schemas.BaseFile, schemas.ReportResponse]):
    def check_report(self, db: Session) -> Optional[Report]:
        return db.query(Report).first()


crud_report = ReportCRUD(Report)
