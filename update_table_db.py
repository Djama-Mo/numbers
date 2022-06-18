from insert_data import insert_into_table
from commands import truncate_table
from table_db import run_command


def update_table():
    run_command(truncate_table)
    insert_into_table()
