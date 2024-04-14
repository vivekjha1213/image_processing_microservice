from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import image
from app.core.database import Base, engine, SessionLocal
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# CORS middleware allows requests from different origins in your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# def startup_event():
    # Create all tables if they don't already exist
Base.metadata.create_all(bind=engine)

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Include routers from image.py
app.include_router(image.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Image Processing Microservice!"}