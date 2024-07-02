from typing import ClassVar

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DRIVER: ClassVar[str] = "postgresql+psycopg2"
    USERNAME: ClassVar[str] = "user"
    PASSWORD: ClassVar[str] = "password"
    HOST: ClassVar[str] = "db"
    PORT: ClassVar[str] = 5432
    DATABASE: ClassVar[str] = "memento"
    TEST_DATABASE: ClassVar[str] = "test"

    SQLALCHEMY_DATABASE_URL: ClassVar[str] = (
        f"{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    )

    class Config:
        env_file = ".env"


settings = Settings()
