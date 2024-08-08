from core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from loguru import logger
from sqlalchemy.orm import sessionmaker
from database.models import Base


__all__ = [
    "database_manager"
]

DB_URL = (
    f"postgresql+asyncpg://"
    f"{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}?"
)

CONNECTION_ARGS = {
    "pool_recycle": 3600,
    "echo": settings.DEBUG,
    "echo_pool": settings.DEBUG,
    "pool_size": 10,
    "max_overflow": 5
}

async_engine = create_async_engine(
    url=DB_URL,
    **CONNECTION_ARGS
)

async_session = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class DatabaseConnectionManager:
    def __init__(self):
        self.session_factory = async_session
        self.__initialized = False

    @staticmethod
    async def __init_connection():
        async with async_engine.begin() as conn:
            logger.info("Establishing database connection...")
            await conn.run_sync(Base.metadata.create_all)
            logger.info("Database connection established")

    async def init(self):
        if not self.__initialized:
            try:
                await self.__init_connection()
                self.__initialized = True
                logger.info("DatabaseConnectionManager initialized")
            except Exception as e:
                self.__initialized = False
                logger.error(f"Failed to initialize DatabaseConnectionManager: {e}")

    def get_session(self) -> AsyncSession:
        if not self.__initialized:
            raise Exception("DatabaseConnectionManager is not initialized. Call 'init' method first.")
        return self.session_factory()


database_manager = DatabaseConnectionManager()
