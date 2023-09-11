# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:49:24 2023

@author: nicol
"""

from vacuum import VacuumAgent
import random

class NguzzoneVacuumAgent(VacuumAgent):
    clean_streak = 0
    movements = ['Left','Right','Up', 'Down']
    def __init__(self):
        super().__init__()
        #any initiliztion you want to do here
        self.last_move = ""
        self.past_choice = ""
        
    def program(self, percept):
            # your amazing Ai vacuum cleaner code goes here
            
            print(percept[0], percept[1])
            #if the square is clean and we haven't hit anything then continue moving as you were going
            #if this is our first action in the sequence then pick a random direction and move in it
            
            if(percept[0] == 'Clean' and percept[1] == 'None'):
                NguzzoneVacuumAgent.clean_streak += 1
                if NguzzoneVacuumAgent.clean_streak > 10:
                    r = random.randint(0, 3)
                    rmove = NguzzoneVacuumAgent.movements[r]
                    self.last_move = rmove
                    self.past_choice = rmove
                    print(rmove)
                    return rmove
                if self.past_choice in NguzzoneVacuumAgent.movements:
                    print(self.past_choice)
                    return self.past_choice
                
                elif self.past_choice == 'Suck' and self.last_move != "":
                    print(self.last_move)
                    return self.last_move
                else:
                    r = random.randint(0, 3)
                    rmove = NguzzoneVacuumAgent.movements[r]
                    self.last_move = rmove
                    self.past_choice = rmove
                    print(rmove)
                    return rmove
                
            elif (percept[0] == 'Clean' and percept[1] == 'Bump'):
                NguzzoneVacuumAgent.clean_streak += 1
                if NguzzoneVacuumAgent.clean_streak > 8:
                    if self.last_move == 'Left':
                        self.last_move = 'Up'
                        self.past_choice = 'Up'
                        print('Up')
                        return 'Up'
                    elif self.last_move == 'Down':
                        self.last_move = 'Left'
                        self.past_choice = 'Left'
                        print('Left')
                        return 'Left'
                    elif self.last_move == 'Right':
                        self.last_move = 'Down'
                        self.past_choice = 'Down'
                        print('Down')
                        return 'Down'
                    elif self.last_move == 'Up':
                        self.last_move = 'Right'
                        self.past_choice = 'Right'
                        print('Right')
                        return 'Right'
                    return rmove
                if self.last_move == 'Left':
                    self.last_move = 'Down'
                    self.past_choice = 'Down'
                    print('Down')
                    return 'Down'
                elif self.last_move == 'Down':
                    self.last_move = 'Right'
                    self.past_choice = 'Right'
                    print('Right')
                    return 'Right'
                elif self.last_move == 'Right':
                    self.last_move = 'Up'
                    self.past_choice = 'Up'
                    print('Up')
                    return 'Up'
                elif self.last_move == 'Up':
                    self.last_move = 'Left'
                    self.past_choice = 'Left'
                    print('Left')
                    return 'Left'
            elif (percept[0] == 'Dirty'):
                NguzzoneVacuumAgent.clean_streak = 0
                self.past_choice = 'Suck'
                print('Suuuuuuck')
                return 'Suck'
            return 'NoOp'