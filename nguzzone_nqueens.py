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
    x = 0
    while True:
        x += 1
        print(f"climb-turn: {x}")
        boards = getAllBoards(curBoard)
        
        goodBoards = []
        for posBoard in boards:
            if checkQueenPairs(posBoard) < checkQueenPairs(curBoard):
                goodBoards.append(posBoard)
        if goodBoards == []:
            return None
        bestBoard = max(goodBoards, key=checkQueenPairs)
        viewBoard(bestBoard)
        
        if checkSolution(bestBoard): 
            return bestBoard
        
        if bestBoard == curBoard:
            return None
        print(bestBoard)
        curBoard = bestBoard
                
        
    return None

def checkQueenPairs(board):
    n = len(board)
    count = 0
    for column in range(n):
        
        for row in range(column+1, n):

            if board[column] == board[row] :
                count +=1
            elif board[column] - column == board[row] - row:
                count += 1
            elif column + board[column] == board[row] + row:
                count += 1
            
    return count

def checkSolution(board):
    if checkQueenPairs(board) == 0:
        return True
    else:
        return False

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
    print("Board: ", end = "")
    print("[", end=" ")
    for i in board:
        print(i, end=" ")
    print("]")
    return None
    
def viewBoard(board):    
    n = len(board)

    print("+-" + "-" *(n*2) + "-+")
    for row in range(n):
        print("|", end="")
        for column in range(n):
            if row == board[column]:
                print(" Q",end="")
            else:
                print(" .",end="")
        print(" |")
    print("+-" + "-" *(2*n) + "-+")
    printBoard(board)
    print()


def main():
    print("starting program...")
    if len(sys.argv) != 2:
        print("Error: "'To use file type "nguzzone_nqueens.py n" where n is an integer')
        sys.exit(1)
        
    n = int(sys.argv[1])
    board = [random.randint(0, n-1) for _ in range(n)]
    print("initial board")
    viewBoard(board)
    
    goal = False
    
    x = 0
    while goal == False:
        print("=======================================")
        x += 1
        print()
        print()
        print(f" Main Turn {x}")
        print()
        
        #check for solution. Call hill climb or checkQueens here.
        
        solBoard = hillClimb(board)
        if solBoard != None:
            print()
            #printBoard(solBoard)
            print("Solved!!!")
            viewBoard(solBoard)
            break
        board = [random.randint(0, n-1) for _ in range(n)]
        print("RNG'd a new board:")
        viewBoard(board)
        
    
if __name__ =="__main__":
    main()