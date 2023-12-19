import os
from typing import List

from fastapi import APIRouter, Depends, Form, HTTPException, UploadFile
from fastapi.params import File
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import JSONResponse, FileResponse

from app.api.deps import get_current_user, get_db
from app.crud.logos import crud_logo
from app.models import Admin
from app.schemas import BaseLogo, LogoList

router = APIRouter()


@router.post("/upload", response_model=BaseLogo, status_code=status.HTTP_201_CREATED)
def upload_report(
    file: UploadFile = File(...),
    description: str = Form(...),
    db: Session = Depends(get_db),
    current_user: Admin = Depends(get_current_user),
):
    allowed_extensions = ["jpeg", "jpg", "png", "gif"]
    file_extension = file.filename.split(".")[-1].lower()

    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400, detail="File must be in .jpeg, .jpg, .png, .gif format"
        )

    upload_folder = "logo"
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)
    print(file_path)
    if os.path.exists(file_path):
        raise HTTPException(
            status_code=400, detail="File with this name already exists"
        )

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    logo_schema = BaseLogo(
        filename=file.filename, path=file_path, description=description
    )
    logo = crud_logo.create(db=db, obj_in=logo_schema)

    return JSONResponse(
        content={
            "message": f"{file.filename} successfully added. "
            f"Date: {logo.created_at.strftime('%Y-%m-%d %H:%M:%S')} "
            f"Description: {logo.description}"
        },
        media_type="application/json",
    )


@router.get("/logos", response_model=List[LogoList], status_code=status.HTTP_200_OK)
def list_logos(db: Session = Depends(get_db)):
    logos = crud_logo.get_multi(db)
    return logos


@router.get("/logos/{logo_path:path}", response_class=FileResponse)
def get_logo(logo_path: str):
    return FileResponse(logo_path)


@router.delete("/remove", status_code=status.HTTP_204_NO_CONTENT)
def remove_logo(
    logo_id: int,
    db: Session = Depends(get_db),
    current_user: Admin = Depends(get_current_user),
):
    logo = crud_logo.get(db, logo_id)
    if logo is None:
        raise HTTPException(status_code=404, detail="Logo not found")

    file_path = logo.path
    if os.path.exists(file_path):
        os.remove(file_path)

    crud_logo.remove(db, id=logo_id)
    return {"message": f"Logo {logo.filename} successfully removed."}
