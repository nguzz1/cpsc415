# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:49:24 2023

@author: nicol
"""

from vacuum import VacuumAgent

class NguzzoneVacuumAgent(VacuumAgent):

    movements = ['Left','Right','Up', 'Down']
    def _init_(self):
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
                if self.past_choice in movements:
                    return self.past_choice
                
                elif self.past_choice == 'Suck':
                    return self.last_move
            return 'NoOp'