import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pandas as pd

# okej te funkcije neki delajo
def pull_sheet_data(SCOPES,SPREADSHEET_ID,DATA_TO_PULL):
    creds = gsheet_api_check(SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=DATA_TO_PULL).execute()
    values = result.get('values', [])
    
    if not values:
        print('No data found.')
    else:
        rows = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                  range=DATA_TO_PULL).execute()
        data = rows.get('values')
        print("COMPLETE: Data copied")
        return data



def gsheet_api_check(SCOPES):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

# koda
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1Cv9EgP-gcNYhTOR2O9DxDBdSoSLT0iBg5lDCvBdx51E'
DATA_TO_PULL = 'tocke'

data = pull_sheet_data(SCOPES,SPREADSHEET_ID,DATA_TO_PULL)

data1 = data[4:]
imena = data[2][2:9] 

print(imena)
tocke = []
stIger = 0
for line in data1:
    if line[1] == '':
        break
    stIger += 1
    tocke.append(line[2:9])



for i in range(7):
    print(i, imena[i])
    f = open(imena[i] + ".txt", "w")

    for j in range(stIger):
        f.write(tocke[j][i] + "\n")
    f.close()




