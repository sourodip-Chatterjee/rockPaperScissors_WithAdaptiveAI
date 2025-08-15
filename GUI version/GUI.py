from tkinter import *
from PIL import Image, ImageTk
from dataManager import separator
from ui import pastMatches, openCSVFile, userChoiceHistory, screenShot
from gameLogic import playRound
import config as cfg

# Window Setup
window = Tk()
window.title(cfg.WINDOW_TITLE)
window.config(background=cfg.WINDOW_BG)
window.geometry(cfg.WINDOW_SIZE)
window.resizable(False, False)

iconLogo = PhotoImage(file=cfg.ICON_PATH)
window.iconphoto(True, iconLogo)

def quitGame():
    separator()
    window.destroy()
window.protocol('WM_DELETE_WINDOW', quitGame)

# Menu Bar
history = PhotoImage(file=cfg.HISTORY_ICON)
quitWin = PhotoImage(file=cfg.QUIT_ICON)
sShot = PhotoImage(file=cfg.SCREENSHOT_ICON)
csvFile = PhotoImage(file=cfg.CSV_ICON)
userHistory = PhotoImage(file=cfg.USER_HISTORY_ICON)

menuBar = Menu(window)
window.config(menu=menuBar)

fileMenu = Menu(tearoff=0, font=('Arial', 10))
menuBar.add_cascade(label='open', menu=fileMenu)
fileMenu.add_command(label='see history', command=lambda: pastMatches(window), image=history, compound=LEFT)
fileMenu.add_command(label='open CSV File', command=openCSVFile, image=csvFile, compound=LEFT)
fileMenu.add_command(label='user choice history', command=userChoiceHistory, image=userHistory, compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label='exit', command=quitGame, image=quitWin, compound=LEFT)

saveMenu = Menu(tearoff=0, font=('Arial', 10))
menuBar.add_cascade(label='moment', menu=saveMenu)
saveMenu.add_command(label='take SS', command=lambda: screenShot(window), image=sShot, compound=LEFT)

# Title
titleLabel = Label(window, font=cfg.TITLE_FONT, text="Rock - Paper - Scissors", bg=cfg.WINDOW_BG)
titleLabel.pack(pady=20)

# Scoreboard
scoreFrame = Frame(window, bg=cfg.WINDOW_BG)
scoreFrame.pack(pady=10)

scoreLabels = {
    'player': Label(scoreFrame, text='Player: 0', font=cfg.SCORE_FONT, bg=cfg.WINDOW_BG),
    'computer': Label(scoreFrame, text='Computer: 0', font=cfg.SCORE_FONT, bg=cfg.WINDOW_BG),
    'tie': Label(scoreFrame, text='Tie: 0', font=cfg.SCORE_FONT, bg=cfg.WINDOW_BG)
}
scoreLabels['player'].grid(row=0, column=0, padx=20)
scoreLabels['computer'].grid(row=0, column=1, padx=20)
scoreLabels['tie'].grid(row=0, column=2, padx=20)

# Load Images
imageFiles = [cfg.ROCK_IMG, cfg.PAPER_IMG, cfg.SCISSORS_IMG]
buttonImages = [ImageTk.PhotoImage(Image.open(file).resize(cfg.BUTTON_IMG_SIZE)) for file in imageFiles]
choiceImages = [ImageTk.PhotoImage(Image.open(file).resize(cfg.CHOICE_IMG_SIZE)) for file in imageFiles]

# Buttons
buttonFrame = Frame(window, bg=cfg.WINDOW_BG)
buttonFrame.pack(pady=20)

labels = ['Rock', 'Paper', 'Scissors']
for i in range(3):
    btn = Button(buttonFrame,
                 text=labels[i],
                 image=buttonImages[i],
                 compound='top',
                 command=lambda c=labels[i]: playRound(
                     c,
                     labels,
                     {'player': playerImageLabel, 'computer': computerImageLabel},
                     choiceImages,
                     statusLabel,
                     scoreLabels
                 ),
                 font=('Arial', 12, 'bold'),
                 borderwidth=0,
                 bg=cfg.WINDOW_BG,
                 fg=cfg.WINDOW_BG,
                 activebackground='#EAEAEA',
                 activeforeground='#EAEAEA',
                 cursor='hand2')
    btn.grid(row=0, column=i, padx=15)

# Status Label
statusLabel = Label(window, text="Make Your Move!", font=cfg.STATUS_FONT, bg=cfg.WINDOW_BG, fg=cfg.STATUS_COLOR)
statusLabel.pack(pady=20)

# Choice Display
choiceFrame = Frame(window, bg=cfg.WINDOW_BG)
choiceFrame.pack(pady=10)

Label(choiceFrame, text='Player Choice', font=('Arial', 12), bg=cfg.WINDOW_BG).grid(row=0, column=0, padx=20)
Label(choiceFrame, text='Computer Choice', font=('Arial', 12), bg=cfg.WINDOW_BG).grid(row=0, column=1, padx=20)

playerImageLabel = Label(choiceFrame, bg=cfg.WINDOW_BG)
playerImageLabel.grid(row=1, column=0)
computerImageLabel = Label(choiceFrame, bg=cfg.WINDOW_BG)
computerImageLabel.grid(row=1, column=1)

window.mainloop()
