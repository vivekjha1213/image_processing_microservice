# app/api/endpoints/image.py
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from fastapi import FastAPI, File, UploadFile
from pathlib import Path
from app.core import crud, schemas
from app.api.dependencies import get_db

router = APIRouter()


@router.get("/health-check")
async def read_root():
    return {"message": "Health-Check okay !!"}


FILE_DIRECTORY = Path(__file__).parent / "app"

print(f"FILE_DIRECTORY:{FILE_DIRECTORY}")

FILE_DIRECTORY.mkdir(parents=True, exist_ok=True)  # Ensure directory exists

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_location = FILE_DIRECTORY / file.filename
        with open(file_location, "wb") as out_file:
            content = await file.read() 
            out_file.write(content)

        return {"filename": file.filename, "location": str(file_location)}
    except Exception as e:
        # If something went wrong, return an error response
        raise HTTPException(status_code=500, detail=str(e))
    
    

@router.get("/images/{image_id}", response_model=schemas.Image)
def read_image(image_id: int, db: Session = Depends(get_db)):
    db_image = crud.get_image(db, image_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image
