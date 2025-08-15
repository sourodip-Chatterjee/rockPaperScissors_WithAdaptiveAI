# computerChoices.py.
import random as rd
from choices import choices

def getComputerChoice():
    compChoice = rd.choice(choices)
    return compChoice
