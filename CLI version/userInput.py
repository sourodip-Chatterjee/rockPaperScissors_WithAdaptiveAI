# userInput.py.
from utils.colorUtils import colorText

def getUserChoice():
    uChoice = input("Enter your choice (rock/ paper/ scissors) or q to Quit--> ")
    return uChoice

def getNumberOfRounds():
    while True:
        print("-> Please enter an Odd number like 3, 5, 7...")
        round = input("Enter the number of round you would like to play : ")
        if round.lower() in ['q', 'quit']:
            return 0
        if round.isdigit():
            round = int(round)
            if round <= 1:
                print(colorText("Please enter a number greater than 1 for a meaningful game..", "lose"))
            if round % 2 == 0:
                print(colorText(f"{round} is an even number, changing it to {round +1} to avoid tie.", "info"))
                return round +1
            else:
                return round
        else:
            print(colorText("Invalid input.. Please enter a Valid number like 3, 5, 7, ...", "lose"))
