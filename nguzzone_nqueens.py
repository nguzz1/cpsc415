# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:04:00 2023

@author: nicol
"""

import sys
import random
board = []

def hillClimb(board):
    return None

def checkQueens(board):
    return None

def getColumn(board):
    return None

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
                
    return None 