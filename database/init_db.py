from database.utils import *

from database import *


if __name__ == "__main__":
    create_database_schema(PG_HOST, PG_PORT, PG_USER, PG_PASSWORD, PG_DB)

    print('Connecting to Postgres at: %s' % PG_HOST)
    db.connect()

    create_tables(db, TABLES)

    db.close()
