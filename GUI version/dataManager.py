import os
import csv
from datetime import datetime
from config import DATA_DIR, CSV_FILE_PATH

os.makedirs(DATA_DIR, exist_ok=True)

if not os.path.exists(CSV_FILE_PATH):
    with open(CSV_FILE_PATH, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Player Choice', 'Computer Choice', 'Result'])

def saveMatch(player, computer, result):
    with open(CSV_FILE_PATH, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), player, computer, result])

def separator():
    with open(CSV_FILE_PATH, 'a', newline='') as f:
        writer = csv.writer(f)
        sep = '-' * 20
        writer.writerow([sep, sep, sep, sep])
