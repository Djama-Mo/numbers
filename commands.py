create_command = """
    CREATE TABLE testing (
            "№" SMALLINT PRIMARY KEY,
            "заказ, №" VARCHAR(127) NOT NULL,
            "стоимость, $" INTEGER NOT NULL,
            "стоимость в руб." DECIMAL(10, 2) NOT NULL,
            "срок поставки" DATE
        )"""


def insert_command(_num, _order, _usd_cost, _rub_cost, _date):
    comm = """
    INSERT INTO testing ("№", "заказ, №", "стоимость, $", "стоимость в руб.", "срок поставки")
    VALUES (%s, %s, %s, %s, %s)""", (_num, _order, _usd_cost, _rub_cost, _date)
    return comm


truncate_table = """TRUNCATE TABLE testing;"""
