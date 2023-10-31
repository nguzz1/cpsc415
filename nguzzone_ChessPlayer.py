# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:33:20 2023

@author: nicol
"""

from chess_player import ChessPlayer

from copy import deepcopy

class nguzzone_ChessPlayer(ChessPlayer):

    def __init__(self, board, color):
        super().__init__(board, color)


    def get_move(self, your_remaining_time, opp_remaining_time, prog_stuff):
        move = self.findBestMove(self.board)
        #print(move)
        return move
        
    def minimax(self, board, depth, maxPlayer):
        # Recursively calculate the best move using the minimax algorithm to the specified depth (assuming depth is a positive integer)
        #If we have reached the specified depth, and 
        if depth == 0 or board.is_king_in_checkmate(self.color):
            return self.evaluateBoard(board)
        
        bestBoard = None
        
        if maxPlayer:
            
            maxEval = float(-99999)
        
            for move in board.get_all_available_legal_moves(self.color):
                
                new_board = deepcopy(board)
                new_board.make_move(*move)
                eval = self.minimax(new_board, depth - 1, False)
                #print("           WTFFFF                ")
                #print(eval)
                
                if eval == max(maxEval, eval):
                    bestBoard = deepcopy(new_board)    
                    maxEval = max(maxEval, eval)
            return maxEval
        
        else:
            minEval = float(99999)
            for move in board.get_all_available_legal_moves('black' if self.color == 'white' else 'white'):
                new_board = deepcopy(board)
                new_board.make_move(*move)
                

                
                eval = self.minimax(new_board, depth - 1, False)
                #print("           WTFFFF                ")
               # print(eval)
                if eval == min(minEval, eval):
                    minEval = min(minEval, eval)
                    bestBoard = deepcopy(new_board)
            return minEval
        
    def findBestMove(self, board):
      #  print("findBest")
        depth = 2
        bestMove = None
        bestValue = float(-99999) if self.color == 'white' else float(99999)
        color = deepcopy(self.color)
       # print(board.get_all_available_legal_moves(self.color))
        for move in board.get_all_available_legal_moves(self.color):
            
            newBoard = deepcopy(board)
            newBoard.make_move(*move)
            moveValue = self.minimax(newBoard, depth, self.color == 'white')
            if self.color == 'white' and moveValue > bestValue:
                bestValue = moveValue
                bestMove = move
            
            elif self.color == 'black' and moveValue < bestValue:
                bestValue = moveValue
                bestMove = move
        print(bestMove)
        return bestMove
    
    
    #inish thests comments then opitminze this rundtion. 
    
    def evaluateBoard(self, board):
        e = 0
        for pos, piece in board.items():
            
            val = 0
            
            if piece.get_notation() == 'K':
                val = 900
            elif piece.get_notation() == 'k':
                val = -900
            
            elif piece.get_notation() == 'Q':
                val = 90
            elif piece.get_notation() == 'q':
                val = -90
            elif piece.get_notation() == 'Y':
                val = 80
            elif piece.get_notation() == 'y':
                val = -80
            elif piece.get_notation() == 'S':
                val = 70
            elif piece.get_notation() == 's':
                val = -70
            elif piece.get_notation() == 'R':
                val = 50
            elif piece.get_notation() == 'r':
                val = -50
            elif piece.get_notation() in ('B','N','F'):
                val = 30
            elif piece.get_notation in ('b','n','f'):
                val = -30
            elif piece.get_notation() == 'P':
                val = 10
            elif piece.get_notation() == 'p':
                val = -10
            
            e += val
            
        return e
    
            