from typing import AsyncGenerator
from pydantic import PostgresDsn

from sqlalchemy.ext.asyncio import ( 
    AsyncEngine, 
    AsyncSession,
    async_sessionmaker, 
    create_async_engine,
)

from api.core.config import settings


class DatabaseHelper:

    def __init__(self, url: PostgresDsn, echo: bool = False) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url, 
            echo=echo,
            pool_size=5,
            max_overflow=10,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session

db_helper = DatabaseHelper(settings.db.db_url, echo=True)