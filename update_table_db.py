from insert_data import insert_into_table
from commands import truncate_table
from table_db import run_command


def main():
    run_command(truncate_table, command_name="TRUNCATE TABLE")
    insert_into_table()


if __name__ == '__main__':
    main()
