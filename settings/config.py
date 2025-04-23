from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ROOT_PATH: Path = Path(__file__).parent.parent

    PG_DB: str
    PG_HOST: str
    PG_PORT: int
    PG_USER: str
    PG_PASSWORD: str
    
    API_HOST: str
    API_PORT: int

    model_config = SettingsConfigDict(
        env_file=ROOT_PATH / ".env", env_file_encoding="utf-8"
    )

    def get_db_url(self, db_type: str = "sync"):
        match db_type:
            case "sync":
                return f"postgresql://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB}"
            case "async":
                return f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB}"

    def get_db_url_sqlite(self, db_type: str = "sync"):
        match db_type:
            case "sync":
                return f"sqlite:///data/main.db"
            case "async":
                return f"sqlite+aiosqlite:///data/main.db"

settings = Settings()
