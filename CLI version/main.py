# main.py.
from choices import choices
#from computerChoice import getComputerChoice
from userInput import getUserChoice, getNumberOfRounds
from gameLogic import decideWinner
from display import printResult
from scoreBoard import update_Score, displayScore, earlyTerminator
from utils.colorUtils import colorText
from data.fileLogger import logResult
from aiBrian import getSmartMoves, trackUserMoves, printUserHistory

def main():
    print(colorText("🎮Welcome to Rock-Paper-Scissors Game🎮", 'info'))
    totalRound = getNumberOfRounds() # taking no. of rounds.
    if totalRound == 0:
        print(colorText("Game Canceled", "tie"))
        return

    print(colorText(f"Starting the game for {totalRound} Rounds--", "info"))

    currentRound = 1 # starting and incrementing inside.
    while totalRound >= currentRound:
        user = getUserChoice() # player choice.

        if user.lower() in ['q', 'quit']:
            print(colorText("--Quitting the Game.", 'info'))
            if(currentRound > 1):
                printUserHistory()
            logResult(user= user, computer="N/A", result= "Game Ended\n" + "-"*40 +"\n")
            break
        if user.lower()  not in choices:
            print(colorText("--Invalid Input... Try again.", 'lose'))
            continue

        #compChoice = getComputerChoice() # computer choice.
        trackUserMoves(move= user.lower()) # tracking player's moves.
        compChoice = getSmartMoves() # getting calculative choices.
        winner = decideWinner(user= user.lower(), compChoice= compChoice) # choosing the winner.
        printResult(user= user, compChoice= compChoice, winner= winner.lower())

        update_Score(result= winner.lower())
        displayScore() # displaying the score at every iteration.
        logResult(user= user, computer=compChoice, result=winner) # logging the scores.

        if earlyTerminator(maxRound= totalRound): # if more than half matches won/lose.
            logResult(user='N/A', computer='N/A', result= 'Early Victory Achieved..\n' + '-'*40 + '\n')
            printUserHistory()
            break;

        currentRound += 1 # incrementing the current Round.

    print(colorText("---Game Session 🏁 Completed---", "info"))
    printUserHistory()
    logResult(user= "N/A", computer= "N/A", result= "Game Session Ended\n" + "-"*40 + "\n")

if __name__ == '__main__':
    main()
