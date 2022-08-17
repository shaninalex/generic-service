import aiopg.sa
from datetime import datetime
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Text,
    TIMESTAMP,
    Integer
)

meta = MetaData()

log = Table(
    'log', meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('text', Text),
    Column('created_at', TIMESTAMP, default=datetime.now(), nullable=False),
)


class RecordNotFound(Exception):
    """Requested record in database was not found"""


def create_tables(database_uri, echo):
    engine = create_engine(database_uri, echo=echo)
    meta.create_all(engine)


async def db_context(app):
    engine = await aiopg.sa.create_engine(
        dsn=app['config']['DATABASE_URL'],
        echo=app['config']['DEBUG'])

    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()
