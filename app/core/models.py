from sqlalchemy import Column, Integer, String, DateTime, func
from app.core.database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(
        String(50),
        index=True,
    )
    status = Column(
        String(20),
        default="pending",
    )
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
