# -*- coding: utf-8 -*-.
"""
Created on Tue Sep  5 17:49:24 2023

@author: nicol
"""

from vacuum import VacuumAgent
import random

class NguzzoneVacuumAgent(VacuumAgent):
    clean_streak = 0
    start = 0

    movements = ['Left','Right','Up', 'Down']
    def __init__(self):
        super().__init__()
        #any initiliztion you want to do here
        self.last_move = ""
        self.past_choice = ""
        #if bumpDetected = 0 then no bump has been detected (we are floating)
        #if bumpDetected = 1 then bump has been detected ABOVE
        #if bumpDetected = 2 then a bump has been detected to the LEFT
        #if bumpDetected = 3 then a bump has been detected BELOW
        #if bumpDetected = 4 then a bump has been detected to the RIGHT
        self.bumpDetected = 0
        
        self.justSucked = 0
        

    
        
    def program(self, percept):
            # your amazing Ai vacuum cleaner code goes here
            
            #initial start sequence
            if NguzzoneVacuumAgent.start == 0:
                
                if percept[1] == 'Bump':
                    #bumpDetected = 0 means that a bump has been detected above. 
                    if self.last_move == 'Up' and self.bumpDetected == 0:
                        self.bumpDetected = 1
                        self.last_move = 'Left'
                        self.past_choice = 'Left'
                        return 'Left'
                    elif self.last_move == 'Left' and self.bumpDetected == 1:
                        self.bumpDetected = 2
                        self.last_move = 'Down'
                        self.past_choice = 'Down'
                        return'Down'
                    elif self.last_move == 'Down' and self.bumpDetected == 2:
                        self.bumpDetected = 3
                        self.last_move = 'Right'
                        self.past_choice = 'Right'
                        return 'Right'
                    elif self.last_move == 'Right' and self.bumpDetected == 3: 
                        self.bumpDetected = 4
                        self.last_move = 'Up'
                        self.past_choice = 'Up'
                        return 'Up'
                    elif self.last_move == 'Up' and self.bumpDetected != 0:
                        self.last_move = 'Left'
                        self.past_choice = 'Left'
                        self.bumpDetected = 0
                        return 'Left'
                    elif self.last_move == 'Left' and self.bumpDetected == 0:
                        self.last_move = 'Down'
                        self.past_choice = 'Down'
                        NguzzoneVacuumAgent.start = 1
                        return 'Down'
                    
                elif percept[0] == 'Dirty':
                    self.past_choice = 'Suck'
                    return 'Suck'
                elif percept[0] == 'Clean' and percept[1] == 'None':
                    return self.last_move
            elif NguzzoneVacuumAgent.start == 1:
                #go in a direction till you hit a bump or 10 clean tiles in a row
                if percept [0] == 'Dirty':
                    self.past_choice = 'Suck'
                    return 'Suck'
                elif percept[1] == 'None':
                    return self.last_move
                elif percept[1] == 'Bump': 
                    recent = NguzzoneVacuumAgent.movements.index(self.last_move)
                    r = random.randint(0, 3)
                    while r == recent:
                        r = random.randint(0,3)
                    rmove = NguzzoneVacuumAgent.movements[r]
                    self.last_move = rmove
                    self.past_choice = rmove
                    return rmove
                

            
     