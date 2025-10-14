from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from settings import settings

engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    echo=False,          # SQL 쿼리 로그 비활성화 (성능 최적화)
    pool_size=100,        # 기본 연결 풀 크기 (동시 접속 가능한 DB 연결 수)
    max_overflow=300,     # 초과 연결 허용 개수 (추가로 허용할 최대 연결 수)
    pool_timeout=30,     # 연결 대기 시간 (초) (기본값: 30초)
    pool_recycle=1800,   # 재사용 전 최대 연결 유지 시간 (초) (기본값: None)
    pool_pre_ping=True,  # 연결 유효성 검사 (DB 연결 끊김 방지)
)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# 종속성 만들기 : 요청 당 독립적인 데이터베이스 세션/연결이 필요하고 요청이 완료되면 닫음
async def get_db():
    async with SessionLocal() as db:
        yield db
