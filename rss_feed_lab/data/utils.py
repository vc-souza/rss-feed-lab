import os
from contextlib import asynccontextmanager
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


@asynccontextmanager
async def database_session() -> AsyncIterator[AsyncSession]:
    """
    Provides a managed database session.
    """

    async with async_sessionmaker(
        create_async_engine(
            "mysql+asyncmy://"
            f"{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWORD']}"
            f"@{os.environ['MYSQL_HOST']}:{os.environ['MYSQL_PORT']}"
            f"/{os.environ['MYSQL_DATABASE']}"
            "?charset=utf8mb4"
        )
    )() as session:
        yield session
