from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    PGSQL: PostgresDsn = 'postgresql://audio:ZH8k1Ill@localhost:5432/audio'


settings = Settings()
