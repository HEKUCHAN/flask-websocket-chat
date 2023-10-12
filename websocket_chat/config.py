from yarl import URL
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    host: str = "localhost"
    port: int = 5000
    debug_mode: bool = True

    db_schema: str = "postgresql+psycopg2"
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = "root"
    db_pass: str = ""
    db_base: str = ""

    @property
    def db_url(self) -> URL:
        return URL.create(
            drivername=self.db_schema,
            username=self.db_user,
            password=self.db_pass,
            host=self.db_host,
            port=self.db_port,
            database=f"/{self.db_base}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="FLASK_",
        env_file_encoding="utf-8",
    )

config = Config()

class Settings:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI=str(config.db_url)
