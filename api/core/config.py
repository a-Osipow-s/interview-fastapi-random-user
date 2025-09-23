from pathlib import Path
from pydantic import BaseModel, RedisDsn

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent.parent


class Redis(BaseModel):
    url: RedisDsn


class PostgresDB(BaseModel):
    host: str = "localhost"
    port: str = "5432"
    db: str
    user: str
    password: str
    driver: str = "postgresql+asyncpg"

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    @property
    def db_url(self) -> str:
        return f'{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}'


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="TODO__",
        env_nested_delimiter="__",
    )
    node_env: str
    db: PostgresDB


class DevSettings(Settings):
    ...


settings: Settings = DevSettings()
