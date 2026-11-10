from pydantic_settings import BaseSettings, SettingsConfigDict


# Essa classe que terá todas as variaveis de ambiente
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', extra='ignore'
    )

    DATABASE_URL: str
