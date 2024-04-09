from fastapi import FastAPI
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Read database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Image Processing Microservice!"}

if __name__ == "__main__":
    import uvicorn

    # Read environment variables for host and port
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))  # Convert port to integer

    uvicorn.run(app, host=host, port=port)
