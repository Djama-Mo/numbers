from __future__ import print_function

import os.path
from direnv import load

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'

load()
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = os.getenv('SAMPLE_SPREADSHEET_ID')
SAMPLE_RANGE_NAME = 'Лист1!A2:D'


class GoogleSheetsData(object):
    def __init__(self):
        self.creds = None

    def get_values(self):
        # Get credentials by OAuth2 Client ID
        self.creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        try:
            # Construct a Resource object for interacting with an API
            service = build('sheets', 'v4', credentials=self.creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range=SAMPLE_RANGE_NAME).execute()

            # A range of values from a spreadsheet
            values = result.get('values', [])

            if not values:
                print('No data found.')
            else:
                return values
        except HttpError as err:
            print(err)
