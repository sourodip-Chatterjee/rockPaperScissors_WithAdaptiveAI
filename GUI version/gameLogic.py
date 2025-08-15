import aiBrain
from dataManager import saveMatch

playerPoints = 0
computerPoints = 0
tiePoints = 0

def playRound(playerChoice, labels, imgLabels, choiceImages, statusLabel, scoreLabels):
    global playerPoints, computerPoints, tiePoints

    aiBrain.trackUserMoves(playerChoice)
    computerChoice = aiBrain.getSmartMoves()

    # Show Player's choice image
    if playerChoice == 'Rock':
        imgLabels['player'].config(image=choiceImages[0])
    elif playerChoice == 'Paper':
        imgLabels['player'].config(image=choiceImages[1])
    else:
        imgLabels['player'].config(image=choiceImages[2])

    # Show Computer's choice image
    if computerChoice == 'Rock':
        imgLabels['computer'].config(image=choiceImages[0])
    elif computerChoice == 'Paper':
        imgLabels['computer'].config(image=choiceImages[1])
    else:
        imgLabels['computer'].config(image=choiceImages[2])

    # Add Points
    if playerChoice == computerChoice:
        tiePoints += 1
        result = 'Tie'
        statusLabel.config(text=f'Tie! Both of You chose {playerChoice}.')
    elif (playerChoice == 'Rock' and computerChoice == 'Scissors') or \
         (playerChoice == 'Scissors' and computerChoice == 'Paper') or \
         (playerChoice == 'Paper' and computerChoice == 'Rock'):
        playerPoints += 1
        result = 'Win'
        statusLabel.config(text=f"You win! {playerChoice} beats {computerChoice}.")
    else:
        computerPoints += 1
        result = 'Loss'
        statusLabel.config(text=f"You Lose! {computerChoice} beats {playerChoice}.")

    saveMatch(player=playerChoice, computer=computerChoice, result=result)
    aiBrain.updateRecentResult(result=result)

    # Update score labels
    scoreLabels['player'].config(text=f"Player: {playerPoints}")
    scoreLabels['computer'].config(text=f"Computer: {computerPoints}")
    scoreLabels['tie'].config(text=f"Tie: {tiePoints}")
