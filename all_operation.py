from send_mail import send_mail
from gspread_connection import gspread_connection
import os
from imageoperation import imagegen
import pandas as pd

def operations():
    if os.path.exists("data.csv"):
        gspread_connection()
    dataframe=pd.read_csv("data.csv")
    for num,email in enumerate(dataframe["Email Address"]):
        if(dataframe["Checker"][num]=="not done"):
            imagegen(dataframe["Unique ID"][num])
            dataframe.loc[num, "Checker"] = send_mail(name=dataframe.loc[num, "First Name"], receiver_email=email)
            os.remove("barcode.png")
            os.remove("ticket.jpg")
    dataframe.to_csv("data.csv")