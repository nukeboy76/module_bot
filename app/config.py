from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    # Значение по умолчанию для подключения к базе данных
    DATABASE_URL: str = "postgresql+asyncpg://module_user:module_password@db:5432/module_db"

    class Config:
        env_file = ".env"

settings = Settings()
