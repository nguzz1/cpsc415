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
        move = self.findBestMove(self.board, your_remaining_time, opp_remaining_time,)
        #print(move)
        return move
        
    
    def alphaBeta(self, board, depth, alpha, beta, maxPlayer):
        if depth == 0 or board.is_king_in_checkmate(self.color):
            return self.evaluateBoard(board, depth)
        
        if maxPlayer:
            maxEval = float(-99999)
            for move in board.get_all_available_legal_moves(self.color):
                newBoard = deepcopy(board)
                newBoard.make_move(*move)
                eval = self.alphaBeta(newBoard, depth - 1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            print(maxEval)
            return maxEval
        else:
            minEval = float(99999)
            for move in board.get_all_available_legal_moves('black' if self.color == 'white' else 'white'):
                newBoard = deepcopy(board)
                newBoard.make_move(*move)
                eval = self.alphaBeta(board, depth - 1, alpha, beta, True)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            print(minEval)
            return minEval    
            
    
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
        
    def findBestMove(self, board, your_remaining_time, opp_remaining_time,):
        print(your_remaining_time)
        if your_remaining_time > opp_remaining_time + opp_remaining_time/ 6 and  500 > your_remaining_time > 400:
            depth = 2
        elif your_remaining_time > opp_remaining_time + opp_remaining_time/ 6 or 175 > your_remaining_time < 400:
            depth = 3
        elif your_remaining_time > opp_remaining_time and your_remaining_time < 500:
            depth = 2
        elif opp_remaining_time > your_remaining_time or your_remaining_time > 500 or your_remaining_time > 30:
            depth = 1
        else:
            depth = 2
        
      #  print("findBest")
        bestMove = None
        bestValue = float(-99999) if self.color == 'white' else float(99999)
        color = deepcopy(self.color)
       # print(board.get_all_available_legal_moves(self.color))
        for move in board.get_all_available_legal_moves(self.color):
            
            newBoard = deepcopy(board)
            newBoard.make_move(*move)
            moveValue = self.alphaBeta(newBoard, depth, float(-99999), float(99999), self.color == 'white')
            if self.color == 'white' and moveValue > bestValue:
                bestValue = moveValue
                bestMove = move
            
            elif self.color == 'black' and moveValue < bestValue:
                bestValue = moveValue
                bestMove = move
        print(bestMove)
        return bestMove
    

    #inish thests comments then opitminze this rundtion. 


    def evaluateBoard(self, board, depth):
        e = 0
        for pos, piece in board.items():
            
            val = 0
            color = self.color
            if self.color == 'black' and board.is_king_in_checkmate(color):
                val = 99999
                return val
            elif self.color == 'black' and board.is_king_in_checkmate('white'):
                val = -99999
                return val
            elif self.color == 'white' and board.is_king_in_checkmate(color):
                val = -99999
                return val
            elif self.color == 'white' and board.is_king_in_checkmate('black'):
                val = 99999
                return val
            
            
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
    
         