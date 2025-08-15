# gameLogic.py.
def decideWinner(user, compChoice):
    if user == compChoice:
        return "=>It's a Tie.. 🟰"
    elif (user == 'rock' and compChoice == 'scissors') or \
        (user == 'paper' and compChoice == 'rock') or \
        (user == 'scissors' and compChoice == 'paper'):
        return ("=>Yay! 🎉 you Win!")
    else:
        return ("=>You Lose!😣")
