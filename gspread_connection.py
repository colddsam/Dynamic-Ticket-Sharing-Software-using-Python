import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from randomnumber import genuuid,genunique

def gspread_connection():
    scopes=[
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    creds=ServiceAccountCredentials.from_json_keyfile_name('secret_key.json',scopes=scopes)

    file=gspread.authorize(creds)
    workbook=file.open("Event Registration form")
    sheet=workbook.sheet1

    dataframe = pd.DataFrame(sheet.get_all_records())
    dataframe["Unique ID"]=""
    for num,emailid in enumerate(dataframe["Email Address"]):
        dataframe.loc[num, "Unique ID"] = genunique(email=emailid)
    dataframe["Checker"]="not done"
    dataframe.to_csv("data.csv")
    