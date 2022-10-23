#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PwP: Portfolio

Game of Noughts and Crosses

The board is represented as a string of length 9, made up of the characters
'o' (nought), 'x' (cross), and '.' (blank). The first 3 characters represent the top row, the next 3 the middle
row, and the last 3 the bottom row. For example, the string '..o.x....' represents the board on the right. You 
must use this representation exactly (e.g., don’t use 'O' or '0' for nought, or ' ' for blank).
YOu can specify positions on the board using tuples of integers, indexed by row and then column,
starting at 0. So the board shown above has a nought in position (0,2) and a cross in position (1,1).
"""

def blanks(board):
    # Using two FOR() functions one in another, to define blank square position tuples.
    # if there is "." in the board, this function adds a tuple into a list.
    # At the end we get returned list with all available places.
    counter = 0
    blanklist = [] 
    for a in range(3):
        for b in range(3):
            if(board[counter] == '.'):
                blanklist.append((a,b))
            counter += 1
    return blanklist

def make_move(board,p,a,b):
    # It uses IF() function to check if a given position is a blank square.
    # If true it replaces blank square with player's symol and adds to a new list.
    # If false it adds to a new list without changing the square.
    counter = 0 
    newboard = ""
    for i in range(3):
        for j in range(3):
            if(i == a and j == b and board[counter] == "."):
                newboard += board[counter].replace('.',p)
            else:
                newboard += board[counter]
            counter += 1
    return newboard

def has_won(board,p):
    # This function checks if any combination is fullfilled, if yes it returns a boolean.
    # checks rows
    if(board[0]==p and board[1]==p and board[2]==p):
        return True
    elif (board[3]==p and board[4]==p and board[5]==p):
        return True
    elif (board[6]==p and board[7]==p and board[8]==p):
        return True
    # checks columns
    elif (board[0]==p and board[3]==p and board[6]==p):
        return True
    elif (board[1]==p and board[4]==p and board[7]==p):
        return True
    elif (board[2]==p and board[5]==p and board[8]==p):
        return True
    # checks diagonals
    elif (board[0]==p and board[4]==p and board[8]==p):
        return True
    elif (board[2]==p and board[4]==p and board[6]==p):
        return True
    else:
        return False
    
def suggest_move(board,p):
    # This function suggests a random available blank square to a player.
    # Uses blanks function to get the list of positions of blank squares
    import random
    return random.choice(blanks(board))