from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:123456@localhost/crud"

settings = Settings()
