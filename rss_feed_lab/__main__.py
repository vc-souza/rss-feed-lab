import asyncio
import os
import logging

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

from .constants import APPLICATION_NAME
from .models.feeds import Feed


async def log_feeds():
    """
    Logs every recorded feed using the default application logger.
    """

    logger = logging.getLogger(APPLICATION_NAME)

    # TODO: impl


asyncio.run(log_feeds())
