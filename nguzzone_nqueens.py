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
    curBoard = board
    n = len(board)
    x = 0
    #loops infinitely until a solution is found or we get stuck
    while True:
        x += 1
       # print(f"climb-turn: {x}")
        boards = getAllBoards(curBoard)
        goodBoards = []
        #array of all the good heuristics. need to create a np.random_choice() probability to select which one should be bestBoard
        goodHeuristics = []
        goodDict = {}
        badBoards = []
        badHeuristics = []
        badDict = {}    
        gIndex = 0
        bIndex = 0
        for posBoard in boards:
            numCurQueens  = checkQueenPairs(curBoard)
            numPosQueens = checkQueenPairs(posBoard)
            if numPosQueens < numCurQueens:
                
                goodHeuristics.append(numPosQueens)
                goodBoards.append(posBoard)
                
                goodDict[gIndex] = (n * 2) - numPosQueens #it's n - numPosQueens because a low number is good for the hueristic, but you can't normalize 0. Thus we reverse it and make it so a large number is good.
                #have the boards be assigned to a number 
                #when we pick a number in selectBoard() then we choose the board in goodBoards whose index is that number
                gIndex += 1
            else:
                badBoards.append(posBoard)
                badHeuristics.append(numPosQueens)
                badDict[bIndex] = (n*2) - numPosQueens
                bIndex +=1
                
                
                
        #if there are no good boards then choose the best option out of the "bad" boards
        if goodBoards == []:
            #print("NO GOOD BOARDS")
            bestBoard = selectBoard(badDict, badBoards, n)
        #here we are always choosing the board with the lowest heuristic, however we should instead have a probability function that biasly chooses a board
        else:
            bestBoard = selectBoard(goodDict, goodBoards, n)
        #bestBoard = max(goodBoards, key=checkQueenPairs)
        viewBoard(bestBoard)
        
        if checkSolution(bestBoard): 
            return bestBoard
        
        if bestBoard == curBoard:
            return None
        #if statement where if we switch the board around more than n*2 times then random restart
        if x > (n*2):
            return None
        #print(bestBoard)
        curBoard = bestBoard
                
        
    return None

#Function takes in array of preffered boards and their heuristics, then assigned each of them a normalized probability based on the heuristic value
#If the heuristic is low, it will be towards at the front of the array. Boards to the front of the array should have the highest probability

def selectBoard(goodDict, goodBoards, n):

    #goodBoards should have the boards w the lowest heuristic at the front
    values = np.array(list(goodDict.values()))
    keys = np.array(list(goodDict.keys()))
    if len(values) > 1 or values[0] + (n*2) != 0:
       # print(f"heuristics: {values + (n*2)}")
        
        #get a factor to normalize all of the goodBoards based on their heuristic score
       # print(sum((goodDict.values())))
        #print(f"pre-values = {values}")
        probs = []
        for b in goodDict:
            if goodDict[b] == 0:
                return goodBoards[b]
            p = goodDict[b] / sum(goodDict.values())
            probs.append(p)
  
     
        
         
            
        #use np.random.choice() to randmoly choose one of the good boards based on this new normalized probability.
        
       # print(f"keys = {keys}")
       # print(f"prob_values = {probs}")
        choice = np.random.choice(keys, p = probs, replace=False)
        print(choice)
        return goodBoards[choice]
    else: 
        return None
    
    


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