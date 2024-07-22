import asyncio
import os
import logging

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.future import select

from .constants import APPLICATION_NAME
from .models.feeds import Feed


async def log_feeds():
    """
    Logs every recorded feed using the default application logger.
    """

    logger = logging.getLogger(APPLICATION_NAME)

    engine = create_async_engine(
        "mysql+asyncmy://"
        f"{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWORD']}"
        f"@{os.environ['MYSQL_HOST']}:{os.environ['MYSQL_PORT']}"
        f"/{os.environ['MYSQL_DATABASE']}"
        "?charset=utf8mb4"
    )

    async_session = async_sessionmaker(
        engine,
        expire_on_commit=False,
    )

    async with async_session() as session:
        async for feed in (await session.stream(select(Feed))).scalars():
            logger.warning("-->")
            logger.warning(feed.id)
            logger.warning(feed.title)
            logger.warning(feed.url)


asyncio.run(log_feeds())
