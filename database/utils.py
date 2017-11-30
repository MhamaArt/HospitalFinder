
def yes_or_no(question):
    reply = str(input(question + ' (y/n) [default NO]: ')).lower().strip()
    if not len(reply):
        reply = 'n'
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no(question)


def create_tables(db_connect, table_list):
    with db_connect.transaction() as tx:
        # True here makes table creation fail silently in
        # case if the tables were already created before
        table_names = [name.__name__ for name in table_list]
        decision = yes_or_no("Drop existing %s tables?" % table_names)

        if decision:
            db_connect.drop_tables(table_list, True, cascade=True)
        decision = yes_or_no("Create new %s tables?" % table_names)

        if decision:
            db_connect.create_tables(table_list, True)
        tx.commit()
        return decision


def create_database_schema(host, port, user, password, new_db_name):
    from psycopg2 import connect
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    con = None
    try:
        con = connect(host=host, port=port, user=user, password=password, dbname='postgres')
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    except Exception as e:
        print(e)
    if con:
        cur = con.cursor()

        try:
            cur.execute('CREATE DATABASE ' + new_db_name)
        except Exception as e:
            print(e)
        cur.close()
        con.close()

