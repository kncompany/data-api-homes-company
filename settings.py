import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from config.logging_config import logger

def get_env_file() -> str:
    """환경 변수에 따라 적절한 .env 파일을 반환"""
    env = os.getenv("ENV", "local")

    print("env : " + env)
    logger.info("env : " + env)

    if env == "prod":
        return ".env.prod"
    elif env == "dev":
        return ".env.dev"
    else:
        return ".env.local"


class Settings(BaseSettings):
    """
    애플리케이션 환경 설정
    ENV 환경 변수에 따라 .env.dev 또는 .env.prod 파일을 로드합니다.
    """
    # 데이터베이스 설정
    SQLALCHEMY_DATABASE_URL: str
    SQLALCHEMY_SCHEMA_URL: str

    model_config = SettingsConfigDict(
        env_file=get_env_file(),
        env_file_encoding='utf-8',
        case_sensitive=True,
        extra='ignore'
    )


# 싱글톤 패턴으로 설정 인스턴스 생성
settings = Settings()

print("SQLALCHEMY_DATABASE_URL : " + settings.SQLALCHEMY_DATABASE_URL)
print("SQLALCHEMY_SCHEMA_URL : " + settings.SQLALCHEMY_SCHEMA_URL)
logger.info("SQLALCHEMY_DATABASE_URL : " + settings.SQLALCHEMY_DATABASE_URL)
logger.info("SQLALCHEMY_SCHEMA_URL : " + settings.SQLALCHEMY_SCHEMA_URL)