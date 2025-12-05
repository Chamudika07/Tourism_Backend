import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application Settings"""
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/tourism_db"
    
    # JWT
    SECRET_KEY: str = "your-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # App
    APP_NAME: str = "Tourism API"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    
    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignore extra fields from .env


settings = Settings()
