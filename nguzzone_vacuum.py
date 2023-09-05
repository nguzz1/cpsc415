# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:49:24 2023

@author: nicol
"""

from vacuum import VacuumAgent

class nguzzoneVacuumAgent(VacuumAgent):
    
    def _init_(self):
        super().__init__()
        #any initiliztion you want to do here
        
        def program(self, percept):
            # your amazing Ai vacuum cleaner code goes here
            return 'NoOp'