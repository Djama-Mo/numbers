from commands import insert_command
from main import GoogleSheetsData
from currency_valute import get_current_value
from table_db import run_command


# Create an instance of GoogleSheetsData class
gsd = GoogleSheetsData()
# Get rows from GoogleSheet
values = gsd.get_values()
# Get current value of converting USD to RUB
rub_in_usd = get_current_value()

# Insert each row from GoogleSheets to DB
for value in values:
    rub_cost = float(rub_in_usd) * int(value[2])
    run_command(*insert_command(_num=value[0], _order=value[1], _usd_cost=value[2],
                                _rub_cost=rub_cost, _date=value[3]))
