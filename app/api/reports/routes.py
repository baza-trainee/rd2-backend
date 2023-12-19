import os



from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from starlette import status

from starlette.responses import JSONResponse, FileResponse

from app.api.deps import get_current_user, get_db
from app.crud.report import crud_report, crud_privatepolicy, crud_rules
from app.models import Admin
from app.schemas import BaseFile, ReportResponse
from app.file_validate import file_valid


router = APIRouter()


@router.post(

    "/reports", response_model=ReportResponse, status_code=status.HTTP_201_CREATED

)
def upload_report(
    file: UploadFile,
    db: Session = Depends(get_db),
    current_user: Admin = Depends(get_current_user),
):

    valid_file = file_valid(file)
    if valid_file is False:
        raise HTTPException(status_code=400, detail="File must be in PDF format")

    elif valid_file is None:
        raise HTTPException(status_code=400, detail="The file size should not exceed 200 MB")


    upload_folder = "report"
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)

    print(file_path)
    if crud_report.check_report(db):
        report = crud_report.check_report(db)
        report_id = report.id
        file_path = report.path
        if os.path.exists(file_path):
            os.remove(file_path)
        crud_report.remove(db, id=report_id)


    with open(file_path, "wb") as f:
        f.write(file.file.read())


    report_schema = BaseFile(filename=file.filename, path=file_path)
    report = crud_report.create(db=db, obj_in=report_schema)

    return JSONResponse(
        content={
            "message": f"{file.filename} successfully added. "

            f"Report ID: {report.id} "
            f"Report date: {report.created_at}"
        },
        media_type="application/json",
    )



@router.post(
    "/private-policy", response_model=ReportResponse, status_code=status.HTTP_201_CREATED
)
def upload_private_policy(
    file: UploadFile,
    db: Session = Depends(get_db),
    current_user: Admin = Depends(get_current_user),
):
    valid_file = file_valid(file)
    if valid_file is False:
        raise HTTPException(status_code=400, detail="File must be in PDF format")

    elif valid_file is None:
        raise HTTPException(status_code=400, detail="The file size should not exceed 200 MB")

    upload_folder = "private_policy"
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)
    print(file_path)
    if crud_privatepolicy.check_privatepolicy(db):
        privatepolicy = crud_privatepolicy.check_privatepolicy(db)
        privatepolicy_id = privatepolicy.id
        file_path = privatepolicy.path
        if os.path.exists(file_path):
            os.remove(file_path)
        crud_privatepolicy.remove(db, id=privatepolicy_id)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    privatepolicy_schema = BaseFile(filename=file.filename, path=file_path)
    privatepolicy = crud_privatepolicy.create(db=db, obj_in=privatepolicy_schema)

    return JSONResponse(
        content={
            "message": f"{file.filename} successfully added. "
            f"Private Policy ID: {privatepolicy.id} "
            f"Private Policy date: {privatepolicy.created_at}"
        },
        media_type="application/json",
    )


@router.post(
    "/terms-use", response_model=ReportResponse, status_code=status.HTTP_201_CREATED
)
def upload_terms_use(
    file: UploadFile,
    db: Session = Depends(get_db),
    current_user: Admin = Depends(get_current_user),
):
    valid_file = file_valid(file)
    if valid_file is False:
        raise HTTPException(status_code=400, detail="File must be in PDF format")

    elif valid_file is None:
        raise HTTPException(status_code=400, detail="The file size should not exceed 200 MB")

    upload_folder = "terms_use"
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)
    print(file_path)
    if crud_rules.check_rule(db):
        rule = crud_rules.check_rule(db)
        rule_id = rule.id
        file_path = rule.path
        if os.path.exists(file_path):
            os.remove(file_path)
        crud_rules.remove(db, id=rule_id)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    rule_schema = BaseFile(filename=file.filename, path=file_path)
    rules = crud_rules.create(db=db, obj_in=rule_schema)

    return JSONResponse(
        content={
            "message": f"{file.filename} successfully added. "
            f"Terms Use ID: {rules.id} "
            f"Terms Use date: {rules.created_at}"
        },
        media_type="application/json",
    )


@router.get("/reports/", response_class=FileResponse, status_code=status.HTTP_200_OK)
def get_report(db: Session = Depends(get_db)):
    report = crud_report.check_report(db)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    report_id = report.id
    reports = crud_report.get(db, id=report_id)
    return FileResponse(reports.path)


@router.get("/private-policy/", response_class=FileResponse, status_code=status.HTTP_200_OK)
def get_privatepolicy(db: Session = Depends(get_db)):
    privatepolicy = crud_privatepolicy.check_privatepolicy(db)
    if privatepolicy is None:
        raise HTTPException(status_code=404, detail="Private Policy not found")
    privatepolicy_id = privatepolicy.id
    privatepolicies = crud_privatepolicy.get(db, id=privatepolicy_id)
    return FileResponse(privatepolicies.path)


@router.get("/terms-use/", response_class=FileResponse, status_code=status.HTTP_200_OK)
def get_rule(db: Session = Depends(get_db)):
    rule = crud_rules.check_rule(db)
    if rule is None:
        raise HTTPException(status_code=404, detail="Terms use not found")
    rule_id = rule.id
    rules = crud_rules.get(db, id=rule_id)
    return FileResponse(rules.path)



@router.delete("/remove", status_code=status.HTTP_204_NO_CONTENT)
def remove_report(
    db: Session = Depends(get_db), current_user: Admin = Depends(get_current_user)
):

    """
    Remove report
    """

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



@router.delete("/remove/private-policy", status_code=status.HTTP_204_NO_CONTENT)
def remove_privatepolicy(
    db: Session = Depends(get_db), current_user: Admin = Depends(get_current_user)
):
    """
    Remove Private Policy
    """
    privatepolicy = crud_privatepolicy.check_privatepolicy(db)
    if privatepolicy is None:
        raise HTTPException(status_code=404, detail="Private Policy not found")

    privatepolicy_id = privatepolicy.id
    privatepolicy = crud_privatepolicy.get(db, privatepolicy_id)

    if privatepolicy is None:
        raise HTTPException(status_code=404, detail="Private Policy not found")

    file_path = privatepolicy.path
    if os.path.exists(file_path):
        os.remove(file_path)

    crud_privatepolicy.remove(db, id=privatepolicy_id)
    return privatepolicy


@router.delete("/remove/terms-use", status_code=status.HTTP_204_NO_CONTENT)
def remove_rule(
    db: Session = Depends(get_db), current_user: Admin = Depends(get_current_user)
):
    """
    Remove Private Policy
    """
    rule = crud_rules.check_rule(db)
    if rule is None:
        raise HTTPException(status_code=404, detail="Report not found")

    rule_id = rule.id
    rule = crud_rules.get(db, rule_id)
    if rule is None:
        raise HTTPException(status_code=404, detail="Report not found")

    file_path = rule.path
    if os.path.exists(file_path):
        os.remove(file_path)

    crud_rules.remove(db, id=rule_id)
    return rule





