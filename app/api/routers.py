# app/api/endpoints/image.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ...core import crud, schemas
from ...dependencies import get_db

router = APIRouter()


@router.get("/health-check")
async def read_root():
    return {"message": "Health-Check okay !!"}


@router.post("/images/", response_model=schemas.Image)
def create_image(image: schemas.ImageCreate, db: Session = Depends(get_db)):
    return crud.create_image(db=db, image_data=image.dict())

@router.get("/images/{image_id}", response_model=schemas.Image)
def read_image(image_id: int, db: Session = Depends(get_db)):
    db_image = crud.get_image(db, image_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image
