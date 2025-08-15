# scoreBoard.py.
from display import earlyWinLose
score = {'wins' : 0,
         'losses' : 0,
         'ties' : 0}

def update_Score(result):
    if 'win' in result:
        score['wins']+=1
    elif 'tie' in result:
        score['ties']+=1
    elif 'lose' in result:
        score['losses']+=1

def displayScore():
    print('\n-Current Score-📊')
    print(f"Won : {score['wins']}")
    print(f"Tie : {score['ties']}")
    print(f"Lose : {score['losses']}\n")

def earlyTerminator(maxRound):
    countRound = maxRound//2
    if(score['wins'] > countRound):
        earlyWinLose(winner='wins' )
        return True
    elif(score['losses'] > countRound):
        earlyWinLose(winner='lose')
        return True
    return False
