import psycopg2
from config import config


def create():
    """ Create table in PostgreSQL server """
    comm = """
        CREATE TABLE testing (
            "№" SMALLINT NOT NULL,
            "заказ, №" VARCHAR(127) NOT NULL,
            "стоимость, $" INTEGER NOT NULL,
            "стоимость в руб." DECIMAL(10, 2) NOT NULL,
            "срок поставки" DATE
        )
        """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(comm)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    create()
