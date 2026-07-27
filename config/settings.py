from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    GOOGLE_API_KEY: str
    VECTOR_DB_DIR: str
    MODEL_PATH: str

    class Config:
        env_file = ".env"

settings = Settings()