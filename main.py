# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 03:02:40 2017

@author: anktrivedi
"""

import pandas as pd
import os

def convertToDash(inText,guessedLetters=[]):
    VisibleLetters = ['A','E','I','O','U',' ']
    VisibleLetters.extend(guessedLetters)
    inText = "".join([i if i in VisibleLetters else "_" for i in inText])
    inText = " / ".join(inText.split(" "))
    return inText

def playGame(movieName):
    ChancesLeft = "BOLLYWOOD"
    remainingLetters = set([i for i in movieName if i not in ['A','E','I','O','U',' ']])
    guessedLetters=[]
    enteredLetters=[]
    if len(remainingLetters)>=1:
        print(convertToDash(movieName,guessedLetters))
        while len(remainingLetters)>=1 and ChancesLeft!='':
            in_char = input("Guess a letter: ")
            in_char = in_char.upper()
            if in_char in enteredLetters:
                print("You already had used this character for guessing")
                continue
            enteredLetters.append(in_char)
            if in_char in remainingLetters:
                guessedLetters.append(in_char)
                remainingLetters.remove(in_char)
                print("Correct Guess")
            else:
                ChancesLeft = ChancesLeft[1:]
                print("Wrong. ",ChancesLeft)
                
            print(convertToDash(movieName,guessedLetters))
        if len(remainingLetters)>=1:
            print("You lost the Game. Better Luck next time.")
            print("Movie was ",convertToDash(movieName,guessedLetters+list(remainingLetters)))
        else:
            print("You are awesome. You Won.")

#A = "_A__A_"
#data = pd.read_csv("BollywoodFilmNames.csv",usecols=['Name'])
#data['asdf'] = pd.Series(map(convertToDash,data.Name))
#print(data[data.asdf==A.upper()].Name.unique())

data = pd.read_csv("BollywoodFilmNames.csv",usecols=['Name'])
playGame(data.sample(n=1).squeeze())
