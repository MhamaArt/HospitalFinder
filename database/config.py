from playhouse.pool import PooledPostgresqlExtDatabase

from peewee import Model

from database import *

# PooledPostgresqlExtDatabase.
db = PooledPostgresqlExtDatabase(PG_DB,
                                 user=PG_USER,
                                 password=PG_PASSWORD,
                                 host=PG_HOST,
                                 port=PG_PORT,
                                 max_connections=1000,
                                 stale_timeout=5,
                                 register_hstore=False)


class DatabaseModel(Model):
    class Meta:
        database = db
