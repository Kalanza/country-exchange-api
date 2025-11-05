from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings"""
    BASE_CURRENCY: str = "USD"
    DATABASE_URL: str = "sqlite:///./country_exchange.db"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
