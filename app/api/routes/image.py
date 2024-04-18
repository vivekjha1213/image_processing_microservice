
from pathlib import Path
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.api.controllers import image_controller
from app.core import schemas
from app.api.pkg.dependencies import get_db
from app.api.pkg.file_directory import  get_file_directory
from typing import List

router = APIRouter()


@router.get("/health-check")
def root_checker():
    return image_controller.read_root()

@router.post("/upload")
def upload(file: UploadFile = File(...), upload_dir: Path = Depends(get_file_directory)):
    return image_controller.upload_image(file, upload_dir)

@router.get("/images/{image_id}", response_model=schemas.Image)
def read_image(image_id: int, db: Session = Depends(get_db)):
    return image_controller.read_image(image_id, db)


@router.get("/images", response_model=List[schemas.Image])
def get_all_images(db: Session = Depends(get_db)):
    """
    Endpoint to retrieve all images.
    """
    images = image_controller.read_all_images(db)
    return images