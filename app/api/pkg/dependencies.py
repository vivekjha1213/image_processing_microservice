from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from fastapi import Depends, HTTPException
from starlette.status import HTTP_503_SERVICE_UNAVAILABLE

from app.core.config import settings  

# Create an async engine instance
async_engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Session local for SQLAlchemy
async_session_local = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
    class_=AsyncSession
)

# Dependency to get the database session
async def get_db() -> AsyncSession:
    async with async_session_local() as session:
        try:
            yield session
        except Exception as e:
            raise HTTPException(status_code=HTTP_503_SERVICE_UNAVAILABLE, detail=str(e))


