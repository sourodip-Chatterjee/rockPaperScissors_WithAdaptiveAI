# fileLogger.py.
from datetime import datetime
import os

def logResult(user, computer, result):
    os.makedirs("data", exist_ok= True)
    timeStamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    line = f"[{timeStamp}] You: {user} | Computer: {computer} | Result: {result}\n"


    with open("data/storeLog.txt", "a", encoding= "utf-8") as file:
        file.write(line)

