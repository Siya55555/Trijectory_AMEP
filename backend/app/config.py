from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@localhost/amep_db"
    api_title: str = "AMEP API"
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
