from fastapi import APIRouter, UploadFile, File
import shutil
import os

from src.services.contract_service import analyze_contract

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_contract(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print("PDF Uploaded Successfully!")

    result = analyze_contract(file_path)

    return {
        "filename": file.filename,
        "analysis": result
    }