from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    sqlalchemy_database_url: str
    sqlalchemy_schema_url: str
    fluentbit_host: str
    fluentbit_port: int
    fluentbit_app_name: str

    model_config = SettingsConfigDict(env_file=".env")

config = Settings()
