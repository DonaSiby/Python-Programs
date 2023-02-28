"""
Created on Tue Feb 28 18:35:51 2023

@author: donac
"""
def pattern1():
    word = "PROGRAM"
    letters = len(word)
    for row in range (letters):
        for col in range (letters):
            if row==col or row+col==6:
                print(word[col],end=' ')
            else:
                print(" ",end=' ')
        print()
        
pattern1()
