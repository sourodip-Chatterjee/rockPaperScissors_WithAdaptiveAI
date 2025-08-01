# aiBrain.py.
from collections import defaultdict
import random as rd
from utils.colorUtils import colorText

userHistory = defaultdict(int) # to track user's input.

def trackUserMoves(move):
    if move in ['rock', 'paper', 'scissors']:
        userHistory[move]+= 1

def getSmartMoves():
    if not userHistory:
        return rd.choice(['rock', 'paper', 'scissors']) # for starting rounds where the userHistory is NIL.

    mostUsedMoves = max(userHistory, key= userHistory.get)

    counterMoves = {
        'rock' : 'paper',
        'paper' : 'scissors',
        'scissors' : 'rock'
    }

    return counterMoves[mostUsedMoves]

def printUserHistory():
    print(colorText("\n🤖 Do you know? Most players unconsciously prefer one move...", 'info'))
    print("📊 Let's see your choices so far--> ")
    for key, val in userHistory.items():
        print(f"{key.title()} : {val} times")
