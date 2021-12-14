import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://sheets.googleapis.com"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open('CSV-to-Google-Sheet')

with open('data.csv', 'r') as file_obj:
    content = file_obj.read()
    client.import_csv(spreadsheet.id, data=content)

