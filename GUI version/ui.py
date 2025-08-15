import os, subprocess, platform, csv, time
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageGrab
from config import CSV_FILE_PATH, SCREENSHOT_DIR
import aiBrain

def pastMatches(window):
    if not os.path.exists(CSV_FILE_PATH):
        print("No History Found!")
        return

    historyWindow = Toplevel(window)
    historyWindow.title("Match History")
    historyWindow.geometry('800x400')

    frame = Frame(historyWindow)
    frame.pack(fill=BOTH, expand=True)

    scrollBar = ttk.Scrollbar(frame)
    scrollBar.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(frame, columns=('Date', 'Player', 'Computer', 'Result'),
                        show='headings', yscrollcommand=scrollBar.set)

    tree.column('Date', width=200, anchor='center')
    tree.column('Player', width=150, anchor='center')
    tree.column('Computer', width=150, anchor='center')
    tree.column('Result', width=120, anchor='center')

    tree.heading('Date', text='Date')
    tree.heading('Player', text='Player Choice')
    tree.heading('Computer', text='Computer Choice')
    tree.heading('Result', text='Result')
    tree.pack(fill=BOTH, expand=True)
    scrollBar.config(command=tree.yview)

    lastItem = None
    with open(CSV_FILE_PATH, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0].startswith('-'):
                itemId = tree.insert("", END, values=row, tags=('separator',))
            else:
                itemId = tree.insert("", END, values=row)
            lastItem = itemId
        tree.tag_configure('separator', foreground='grey')

    if lastItem:
        tree.see(lastItem)

def openCSVFile():
    if not os.path.exists(CSV_FILE_PATH):
        print('File Not Found')
        return
    if platform.system() == 'Windows':
        os.startfile(CSV_FILE_PATH)
    elif platform.system() == 'Darwin':
        subprocess.call(["open", CSV_FILE_PATH])
    else:
        subprocess.call(["xdg-open", CSV_FILE_PATH])

def userChoiceHistory():
    historyStr = "Your Move History:\n"
    for key, val in aiBrain.userHistory.items():
        historyStr += f"{key.capitalize()} → {val} times\n"
    messagebox.showinfo("AI Move History", historyStr)

def screenShot(window):
    window.focus_force()
    window.update_idletasks()
    time.sleep(0.35)
    geom = window.geometry()
    w, h, x, y = [int(i) for i in geom.replace("x", "+").split("+")]

    scale_factor = window.winfo_fpixels('1i') / 72
    RIGHT_TRIM = 55
    TOP_TRIM = 45
    LEFT_EXPAND = 1
    BOTTOM_TRIM = 39

    w = int((w - RIGHT_TRIM) * scale_factor)
    h = int((h - BOTTOM_TRIM) * scale_factor)
    x = int((x + LEFT_EXPAND) * scale_factor)
    y = int((y + TOP_TRIM) * scale_factor)

    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    img = ImageGrab.grab(bbox=(x, y, x + w, y + h))
    fileName = os.path.join(SCREENSHOT_DIR, f"game_{time.strftime('%Y%m%d_%H%M%S')}.png")
    img.save(fileName)
    print(f'SS saved: {fileName}')
