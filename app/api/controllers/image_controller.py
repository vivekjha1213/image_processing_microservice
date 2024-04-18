from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.core.models import Image  
from pathlib import Path
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core import crud


def read_root():
    return {"message": "image Health-Check okay !!"}


def upload_image(file: UploadFile, upload_dir: Path):
    file_location = upload_dir / file.filename  

    try:
        contents = file.file.read()
        
        with open(file_location, 'wb') as f:
            f.write(contents)
    except Exception as e:
        print(f"Failed to write file due to {e}")
        return {"message": "There was an error uploading the file"}
    finally:
        # Close the file to free up system resources
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}

def read_image(image_id: int, db: Session):
    db_image = crud.get_image(db, image_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image

  
async def read_all_images(db: AsyncSession):
    """
    Asynchronously retrieves all images from the database using AsyncSession.
    """
    async with db:
        result = await db.execute(select(Image))
        images = result.scalars().all()
        return images