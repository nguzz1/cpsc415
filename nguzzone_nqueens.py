# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:04:00 2023

@author: nico
"""

import sys
import random
import numpy as np
from sklearn import preprocessing

board = []
#performs stoachastic hill climbing
def hillClimb(board):
    bestBoard = board
    curBoard = board
    n = len(board)
    x = 0
    bestH = n*10
    #loops infinitely until a solution is found or we get stuck
    while True:
        x += 1
        print(f"climb-turn: {x}")
        pStochastic = random.random()
        for index in range(n):
            curBoard[index] = random.randint(0, n-1)
            curNQueens = checkQueenPairs(curBoard)
            
            if curNQueens <= bestH:
                bestBoard = curBoard
                bestH = curNQueens 
                if bestH < 0:
                    return bestBoard
        if pStochastic < 0.2:
            curBoard = selectBoard(board, n)
                
        
    return None

#Function takes in array of preffered boards and their heuristics, then assigned each of them a normalized probability based on the heuristic value
#If the heuristic is low, it will be towards at the front of the array. Boards to the front of the array should have the highest probability

def selectBoard(board, n):
    #goodBoards should have the boards w the lowest heuristic at the front
    curNQueens = checkQueenPairs(board)
    bigN = n * (n - 1)
    selected = []
    sNum = []
    
    for column in range(n):
        for row in range(n):
            if board[column] != row:
                board[column] = row
                curNQueens = checkQueenPairs(board)
                x = 1 - (curNQueens / bigN)
                selected.append(board)
                sNum.append(x)
                if x < 0 or random.random() < 0:
                    return board
            board[column] = row
    return board
    
    
    


#counts and returns the number of attacking queen pairs on a given board
def checkQueenPairs(board):
    if board != None:
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
    else: 
        return None

#returns true if a given board is a solution and false otherwise
def checkSolution(board):
    if checkQueenPairs(board) == 0:
        return True
    else:
        return False

#get all possible new boards that could be made from a given board. 
#Returns an array of all the boards
def getAllBoards(board):
    if board != None:
        n = len(board)
        boards = []
        for column in range(n):
            for row in range(n):
                
                if board[column] != row:
                    testBoard = list(board)
                    testBoard[column] = row
                    boards.append(testBoard)
        return boards
    else: 
        return None
        

#prints the array of the board
def printBoard(board):
    print("Board: ", end = "")
    print("[", end=" ")
    for i in board:
        print(i, end=" ")
    print("]")
    return None
  
#prints a visual chessboard that is aesthetically pleasing to look at  
def viewBoard(board):    
    if board != None:
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
    #loops infinitely until a solution is found
    while goal == False:
        print("=======================================")
        x += 1
        print()
        print()
        print(f" Main Turn {x}")
        print()
        
        #check for solution. Call hill climb or checkQueens here.
        
        #perform hilllimbing
        solBoard = hillClimb(board)
        #check to see if a solution board was found
        if solBoard != None:
            #if a solution was found then return the solved board
            print()
            #printBoard(solBoard)
            print("Solved!!!")
            viewBoard(solBoard)
            break
        #if no solution was found then that means we got stuck hillclimbing. 
        #So generate a new random board and restart the hillclimbing process
        board = [random.randint(0, n-1) for _ in range(n)]
        print("RNG'd a new board:")
        viewBoard(board)
        
    
if __name__ =="__main__":
    main()