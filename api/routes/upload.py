from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload")
async def upload_contract(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "message": "File uploaded successfully"
    }