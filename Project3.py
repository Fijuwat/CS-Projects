# File: Project3.py
# Student: Ting Wei Wu
# UT EID: tw28634
# Course Name: CS303E
# 
# Date: 2022/05/01
# Description of Program: This is a wordle game program 

import os.path
from random import random
import random


def playWordle( answer = None ):
    print()
    print('Welcome to WORDLE, the popular word game. The goal is to guess a')
    print('five letter word chosen at random from our wordlist. None of the')
    print('words on the wordlist have any duplicate letters.')
    print()
    print('You will be allowed 6 guesses. Guesses must be from the allowed')
    print('wordlist. We\'ll tell you if they\'re not.')
    print()
    print('Each letter in your guess will be marked as follows:')
    print()
    print('   x means that the letter does not appear in the answer')
    print('   ^ means that the letter is correct and in the correct location')
    print('   + means that the letter is correct, but in the wrong location')
    print()
    print('Good luck!')
    print()
    repeat = True
    while repeat == True:    
        oldFile = str(input("Enter the name of the file from which to extract the wordlist: "))
        if os.path.isfile(oldFile) == False:
            print("File does not exist. Try again!")
        else:
            newList, length = createWordlist("a.txt")
            repeat = False
            
    if answer == None:
        answer = random.choice(newList)
    else:
        if answer in newList: 
            theAnswer = answer
        else:
            print() 
            print("Answer supplied is not legal.")
            exit()
    print()
    a = 0
    j = 0
    while a < (6):
        if a == 0 and j == 0:
            guess = str(input('Enter your guess (' + str(a+1) + '): '))
            j += 1
        else:
            guess = str(input('\nEnter your guess (' + str(a+1) + '): '))
        uGuess = guess.lower()
        if uGuess in newList:
            for i in range (len(answer)):
                print (uGuess[i].upper() + " ", end = "")
            for i in range (len(answer)):
                if uGuess[i] == answer[i] and i == 0:
                    print ('\n^' + " ", end = "")
                    
                elif uGuess[i] == answer[i] and i != 0:
                    print ("^" + " ", end = "")
                    
                elif uGuess[i] in answer and i == 0:
                    print('\n+' + " ", end = '')
                    
                elif uGuess[i] in answer and i != 0:
                    print('+' + " ", end = '')
                    
                else:
                    if i == 0:
                        print('\nx' + " " , end = "")
                        
                    else:
                        print("x" + " " , end = "")
            a += 1
            j += 1
        else:
            print ("Guess must be a 5-letter word in the wordlist. Try again!", end ="") 
        if uGuess == answer or a == 6:
            if uGuess == answer:
                print('\nCONGRATULATIONS! You win!')
                break
            else:
                print ('\nSorry! The word was ' + answer + '. Better luck next time!')
        
       
            
                        
    
        
    
    
        


def createWordlist(filename): 
    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'.  Return
    the list of words and the number of words as a pair. """
    infile = open(filename, 'r')
    newlist = set()
    text = infile.read().split()
    for word in text:
        if len(word) == 5 and word[-1] != 's':    
            newlist.add(word)

    deleteword = set()
    for word in newlist:
        for char in word:
            if word.count(char) > 1:
                deleteword.add(word)
                
    finallist = list(newlist.difference(deleteword))
    
    return sorted(finallist), len(finallist)

def binarySearch(lst, key):
    low = 0 
    high = len(lst) - 1 
    while (high >= low):
        mid = (high+low) // 2
        if lst.index(key) < lst.index(lst[mid]):
            high = mid - 1 
        elif key == lst [mid]:
            return mid
        else:
            low = mid + 1 
    return -low -1 



playWordle('level')
