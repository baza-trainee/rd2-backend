from typing import Optional

from sqlalchemy.orm import Session

from app import schemas

from app.models.reports import Report, PrivatePolicy, Rules


from .base import CRUDBase


class ReportCRUD(CRUDBase[Report, schemas.BaseFile, schemas.ReportResponse]):
    def check_report(self, db: Session) -> Optional[Report]:
        return db.query(Report).first()


crud_report = ReportCRUD(Report)



class PrivatePolicyCRUD(CRUDBase[PrivatePolicy, schemas.BaseFile, schemas.ReportResponse]):
    def check_privatepolicy(self, db: Session) -> Optional[PrivatePolicy]:
        return db.query(PrivatePolicy).first()


crud_privatepolicy = PrivatePolicyCRUD(PrivatePolicy)


class RuleCRUD(CRUDBase[Rules, schemas.BaseFile, schemas.ReportResponse]):
    def check_rule(self, db: Session) -> Optional[Rules]:
        return db.query(Rules).first()


crud_rules = RuleCRUD(Rules)

