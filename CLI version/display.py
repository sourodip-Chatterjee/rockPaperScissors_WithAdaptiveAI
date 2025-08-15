# display.py.
from utils.colorUtils import colorText
from data.fileLogger import logResult

def printResult(user, compChoice, winner):
    print(f"You chose: {user}")
    print(f"The computer chose: {compChoice}")

    if 'win' in winner:
        print(colorText(winner, 'win'))
    elif 'lose' in winner:
        print(colorText(winner, 'lose'))
    elif 'tie' in winner:
        print(colorText(winner, 'tie'))
    else:
        print (winner)

def earlyWinLose(winner):
    terminate = False
    print(colorText(f"Early End: You {winner.upper()} the match by Majority.\n", 'info'))
    if 'win' in winner:
        print(colorText(winner, 'win'))
        terminate = True
    elif 'lose' in winner:
        print(colorText(winner, 'lose'))
        terminate = True

    if (terminate == True):
        logResult(user='Early terminate', computer='Early terminate', result= winner)


