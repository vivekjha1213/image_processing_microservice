from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+aiomysql://root:12345678@localhost/image_pre_process"
    SECRET_KEY: str
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    HOST: str = '127.0.0.1'
    PORT: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

# Create an instance of Settings that will be imported elsewhere in your application.
settings = Settings()
