# app/core/crud.py
from sqlalchemy.orm import Session

from . import models

def create_image(db: Session, image_data: dict):
    db_image = models.Image(**image_data)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

def get_image(db: Session, image_id: int):
    return db.query(models.Image).filter(models.Image.id == image_id).first()


