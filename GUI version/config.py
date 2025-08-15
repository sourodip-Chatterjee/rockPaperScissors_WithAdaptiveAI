import os

# WINDOW SETTINGS
WINDOW_TITLE = "Rock-Paper-Scissors Game"
WINDOW_SIZE = "450x500"
WINDOW_BG = "#F9F9F9"

# SCORE LABEL SETTINGS
SCORE_FONT = ("Arial", 14)
TITLE_FONT = ("Arial", 20, "bold")
STATUS_FONT = ("Arial", 14)
STATUS_COLOR = "gray"

# IMAGE SETTINGS
BUTTON_IMG_SIZE = (90, 90)
CHOICE_IMG_SIZE = (60, 60)

# PATHS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ICON_PATH = os.path.join(BASE_DIR, "pics", "logo.png")
HISTORY_ICON = os.path.join(BASE_DIR, "pics", "History.png")
QUIT_ICON = os.path.join(BASE_DIR, "pics", "QuitSmall.png")
SCREENSHOT_ICON = os.path.join(BASE_DIR, "pics", "screenshot.png")
CSV_ICON = os.path.join(BASE_DIR, "pics", "csvFile.png")
USER_HISTORY_ICON = os.path.join(BASE_DIR, "pics", "userHistory.png")

ROCK_IMG = os.path.join(BASE_DIR, "pics", "rockHand.png")
PAPER_IMG = os.path.join(BASE_DIR, "pics", "paperHand.png")
SCISSORS_IMG = os.path.join(BASE_DIR, "pics", "scissorsHand.png")


# FILE STORAGE
DATA_DIR = os.path.join(BASE_DIR, "data")
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
CSV_FILE_PATH = os.path.join(DATA_DIR, "pastHistory.csv")
