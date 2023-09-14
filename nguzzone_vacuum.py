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
    wall_start = 0
    past_tiles = set()
    past_notess = set() #set of strings containing letters reffering to what was perceived 
    
    movements = ['Up','Left','Down', 'Right']
    positions = [(0,1), (-1,0), (0,-1),(1,0)]
    def __init__(self):
        super().__init__()
        #any initiliztion you want to do here
        self.last_move = ""
        self.last_direction = ""
        self.past_choice = ""
        #if bumpDetected = 0 then no bump has been detected (we are floating)
        #if bumpDetected = 1 then bump has been detected ABOVE
        #if bumpDetected = 2 then a bump has been detected to the LEFT
        #if bumpDetected = 3 then a bump has been detected BELOW
        #if bumpDetected = 4 then a bump has been detected to the RIGHT
        self.bumpDetected = 0
        self.position = (0,0)
        self.justSucked = 0
        

        #if cur_move = 0 then go up
        self.cur_move = 0
        #if cur_move = 1 then go left
        #if cur_move = 2 then go down
        #if cur_move = 3 then go right
        
        
#Theory: Make it map the room in a 2d space and go around obstacles as needed. Make an algortihm that hugs the wwalls and goes around. Then comes back to the origin spot.
#How would it hug the walls? if it runs into a bump, go in a direction next to the og direction that you went when you hit the bump. However evertime you move, first move in the 
#og direction to make sure the wall is still there.

#go Up to the ceiling then try and map the walls of the room by going left and calling the map_walls function.
    def start(self, percept):
        if percept[0] == 'Dirty':
            self.clean_streak = 0
            self.past_choice = 'Suck'
            return 'Suck'
        elif percept[1] == 'Bump':
            self.bumpDetected = 1
            self.clean_streak += 1
            self.last_move = 'Left'
            self.past_choice = 'Left'
            self.position = (self.position[0] - 1, self.position[1])
            NguzzoneVacuumAgent.past_tiles.add(self.position)
            NguzzoneVacuumAgent.start = 1
            return 'Left'
        elif percept[1] == 'None':
            self.clean_streak += 1
            self.last_move = 'Up'
            self.past_choice = 'Up'
            self.position = (self.position[0], self.position[1] + 1)
            NguzzoneVacuumAgent().past_tiles.add(self.position)
            return 'Up'
                    
        
    def map_walls(self, percept):
        if percept[0] == 'Dirty':
            self.clean_streak = 0
            self.past_choice = 'Suck'
            return 'Suck'
        elif NguzzoneVacuumAgent.wall_start = 0:
            self.last_direction = 'Down'
            self.last_move = 'Down'
            updatePosition(self, self.last_direction)
            return 'Down'
        
        elif percept[1] == 'Bump' and self.last_move != self.last_direction:
            self.last_move = self.last_direction
            updatePosition(self, self.last_direction)
        elif percept[1] == 'Bump' and self.last_mov == self.last_direction:
        
    def updatePosition(self, direction):
        if direction in NguzzoneVacuumAgent.movements:
            if direction == 'Up':
                self.position = (self.position[0], self.position[1] + 1)
                NguzzoneVacuumAgent.past_tiles.add(self.position)
                return 1
            elif direction == 'Left':
                self.position = (self.position[0] - 1, self.position[1])
                NguzzoneVacuumAgent.past_tiles.add(self.position)
                return 2
            elif direction == 'Down':
                self.position = (self.position[0], self.position[1] + 1)
                NguzzoneVacuumAgent.past_tiles.add(self.position)
                return 3
            elif direction == 'Right':
                self.position = (self.position[0] + 1, self.position[1])
                NguzzoneVacuumAgent.past_tiles.add(self.position)
                return 4
            
        else:
            return 0
        
        def newDirection(self, direction):
            

#Performs a depth first search 
    def program(self, percept):
            # your amazing Ai vacuum cleaner code goes here
            if percept[0] == 'Dirty': 
                self.past_choice = 'Suck'
                return 'Suck'
            else:
                x,y = self.position
                if self.cur_move == 0:
                    newX, newY = x, y + 1
                    self.last_move = 'Up'
                    
                
            #initial start sequence
            
            
     