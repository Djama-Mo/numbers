from commands import create_command
from table_db import run_command


def main():
    run_command(create_command, command_name="TABLE CREATE")


if __name__ == '__main__':
    main()
