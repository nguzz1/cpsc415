# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:04:00 2023

@author: nicol
"""

import sys
import random
board = []

def hillClimb(board):
    curBoard = board
    while True:
        boards = getAllBoards(curBoard)
        goodBoards = []
        for posBoard in boards:
            if checkQueenPairs(posBoard) < checkQueenPairs(curBoard):
                goodBoards.append(posBoard)
                
        bestBoard = max(goodBoards, key=checkQueenPairs)
        printBoard(bestBoard)
        
        if checkQueenPairs(bestBoard) == 0: 
            return bestBoard
        
        if bestBoard == curBoard:
            return None
        
        curBoard = bestBoard
                
        
    return None

def checkQueenPairs(board):
    n = len(board)
    count = 0
    for column in range(n):
        
        for row in range(column+1,n):

            if board[column] == board[row] or board[column] - board[row] == column - row or board[row] - board[column] == row - column:
                count += 1
            
    return count

def getAllBoards(board):
    n = len(board)
    boards = []
    for column in range(n):
        for row in range(n):
            
            if board[column] != row:
                testBoard = list(board)
                testBoard[column] = row
                boards.append(testBoard)
    return boards
        

#maybe do this idk
def printBoard(board):
    return None
    
def viewBoard(board):    
    return None

def main():
    if len(sys.argv) != 2:
        print("Error: "'To use file type "nguzzone_nqueens.py n" where n is an integer')
        sys.exit(1)
        
    n = int(sys.argv[1])
    board = [random.randint(0, n-1) for i in range(n)]
    goal = False
    
    while goal == False:
        #check for solution. Call hill climb or checkQueens here.
        solBoard = hillClimb(board)
    return None 