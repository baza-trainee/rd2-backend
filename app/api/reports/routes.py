import os
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import JSONResponse

from app.api.deps import get_current_user, get_db
from app.crud.report import crud_report
from app.models import Admin
from app.schemas import BaseFile, ReportDetail, ReportResponse

router = APIRouter()


@router.post(
    "/upload", response_model=ReportResponse, status_code=status.HTTP_201_CREATED
)
def upload_report(
    file: UploadFile,
    db: Session = Depends(get_db),
    current_user: Admin = Depends(get_current_user),
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="File must be in PDF format")

    created_at_str = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    new_filename = f"Report_{created_at_str}.pdf"

    max_length = 2 * 1024**2
    if (file.size / 1024**2) > max_length:
        raise HTTPException(
            status_code=400, detail="The file exceeds the maximum allowed size (2 MB)"
        )

    upload_folder = "report"
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)

    if crud_report.check_report(db):
        raise HTTPException(
            status_code=400, detail="To upload a new report, delete the existing one"
        )

    if os.path.exists(file_path):
        raise HTTPException(
            status_code=400, detail="File with this name already exists"
        )

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    report_schema = BaseFile(filename=new_filename, path=file_path)

    report = crud_report.create(db=db, obj_in=report_schema)
    return JSONResponse(
        content={
            "message": f"{new_filename} successfully added. "
            f"Report ID: {report.id} "
            f"Report date: {report.created_at}"
        },
        media_type="application/json",
    )


@router.get("/", response_model=ReportDetail, status_code=status.HTTP_200_OK)
def get_report(
    db: Session = Depends(get_db), current_user: Admin = Depends(get_current_user)
):
    report = crud_report.check_report(db)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")

    report_id = report.id
    report = crud_report.get(db, id=report_id)

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    return report


@router.delete("/remove", status_code=status.HTTP_204_NO_CONTENT)
def remove_report(
    db: Session = Depends(get_db), current_user: Admin = Depends(get_current_user)
):
    report = crud_report.check_report(db)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")

    report_id = report.id
    report = crud_report.get(db, report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")

    file_path = report.path
    if os.path.exists(file_path):
        os.remove(file_path)

    crud_report.remove(db, id=report_id)
    return report
