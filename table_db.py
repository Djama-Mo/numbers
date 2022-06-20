import psycopg2
from config import config


def run_command(comm, _vars=None, select=0, command_name=''):
    conn = None
    data = None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(comm, _vars)
        if select:
            data = cur.fetchall()
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            if select:
                return data
            print(command_name)
            print('Database connection closed.')

