import asyncio
import os

import tornado

from .handlers.feeds import FeedsHandler


async def main():
    app = tornado.web.Application(
        [
            (r"/feeds", FeedsHandler),
        ]
    )

    app.listen(int(os.environ['WEB_PORT']))

    await asyncio.Event().wait()


asyncio.run(main())
