# aiBrain.py.
from collections import defaultdict
import random as rd
from choices import choices

userHistory = defaultdict(int) # to track user's input.
recentResult = []

counterMoves = {
        'Rock' : 'Paper',
        'Paper' : 'Scissors',
        'Scissors' : 'Rock'
    }

def trackUserMoves(move):
    if move in choices:
        userHistory[move]+= 1

def updateRecentResult(result):
    recentResult.append(result)
    if len(recentResult) > 5:
        recentResult.pop(0)

def isAiLosing():
    return recentResult[-3:] == ['Loss', 'Loss', 'Loss']

def getSmartMoves():
    if not userHistory:
        return rd.choice(choices)

    userMostUsedMoves = max(userHistory, key= userHistory.get)

    if(userHistory[userMostUsedMoves] >= 5):
        if rd.random() < 0.5:
            return counterMoves[userMostUsedMoves]
        else:
            return rd.choice(choices)

    if isAiLosing():
        return rd.choice(choices)

    smartCounter = counterMoves[userMostUsedMoves]
    return smartCounter

