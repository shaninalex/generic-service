import logging

from aiohttp import web

from .db import db_context
from .middlewares import setup_middlewares
from .routes import setup_routes
from .settings import config


async def init_app():
    app = web.Application()

    app['config'] = config()

    # create db connection on startup, shutdown on exit
    app.cleanup_ctx.append(db_context)

    # setup views and routes
    setup_routes(app)

    setup_middlewares(app)

    return app


def main():
    logging.basicConfig(level=logging.DEBUG)

    app = init_app()

    conf = config()
    web.run_app(app, host=conf['APP_HOST'], port=conf['APP_PORT'])


