import tornado

from sqlalchemy.future import select

from ..data.utils import database_session
from ..models.feeds import Feed


class FeedsHandler(tornado.web.RequestHandler):
    """
    Handler for feeds-related requests.
    """

    async def get(self):
        async with database_session() as session:
            self.write(
                {
                    "feeds": [
                        {
                            "id": f.id,
                            "title": f.title,
                            "url": f.url,
                        }
                        async for f in (
                            await session.stream(
                                select(Feed)
                            )
                        ).scalars()
                    ]
                }
            )
