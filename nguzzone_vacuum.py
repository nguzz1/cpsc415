# -*- coding: utf-8 -*-.
"""
Created on Tue Sep  5 17:49:24 2023

@author: nicol
"""

from vacuum import VacuumAgent
import random

class NguzzoneVacuumAgent(VacuumAgent):
    clean_streak = 0
    start_val = 1
    map_walls_val = 0
    inside_val = 0
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
        self.past_position = (0,0)
        #if bumpDetected = 0 then no bump has been detected (we are floating)
        #if bumpDetected = 1 then bump has been detected ABOVE
        #if bumpDetected = 2 then a bump has been detected to the LEFT
        #if bumpDetected = 3 then a bump has been detected BELOW
        #if bumpDetected = 4 then a bump has been detected to the RIGHT
        self.bumpDetected = 0
        self.bumpDirection = ''
        self.position = (0,0)
        self.bumpStreak = 0

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
        elif self.last_move == 'Left' and percept[1] == 'Bump':
            self.bumpStreak += 1
            self.bumpDirection = self.last_move
            NguzzoneVacuumAgent.start_val = 0
            return None
        elif self.last_move == 'Up' and percept[1] == 'Bump':
            self.bumpDetected = 1
            self.bumpStreak += 1
            self.bumpDirection = self.last_move
            self.last_move = 'Left'
            self.past_choice = 'Left'
            NguzzoneVacuumAgent.updatePosition(self, self.last_direction)
            
            return 'Left'
        elif percept[1] == 'None':
            self.bumpStreak = 0
            self.last_move = 'Up'
            self.past_choice = 'Up'
            NguzzoneVacuumAgent.updatePosition(self, self.last_direction)
            return 'Up'
                    
        
    def map_walls(self, percept):
        if self.past_position in NguzzoneVacuumAgent.past_tiles:
            NguzzoneVacuumAgent.map_walls = 0
            return 'No More Walls Left!!!!!!!!'
        else:
            if percept[0] == 'Dirty':
                self.clean_streak = 0
                self.past_choice = 'Suck'
                return 'Suck'
            elif NguzzoneVacuumAgent.start_val == 0:
                
                self.last_direction = 'Down'
                self.last_move = 'Down'
                NguzzoneVacuumAgent.updatePosition(self, self.last_direction)
                return 'Down'
            
            elif percept[1] == 'Bump' and self.last_move != self.last_direction:
                self.bumpStreak += 1
                self.bumpDirection = self.last_move
                self.last_move = self.last_direction
                NguzzoneVacuumAgent.updatePosition(self, self.last_direction)
                return self.last_direction
                
            elif percept[1] == 'Bump' and self.last_move == self.last_direction:
                self.bumpStreak += 1
                self.bumpDirection = self.last_move
                NguzzoneVacuumAgent.newDirection(self, self.last_direction)
                return self.last_direction
            
            #if we didn't hit a bump and are no longer moving in the same direction as we were
            elif percept[1] == 'None' and self.last_move != self.last_direction:
                self.bumpStreak = 0
                holder = self.last_direction
                self.last_direction = self.last_move
                opposite = NguzzoneVacuumAgent.opp_pos(self, holder)
                self.last_move = opposite
                return self.last_move
                
            #if we didn't hit a bump and are still going in the og direction.
            elif percept[1] == 'None' and self.last_move == self.last_direction:
                self.bumpStreak = 0
                return self.bumpDirection
            
    def map_inside(self, percept):
        return 'Left'
            
    def opp_pos(self, direction):
        if direction in NguzzoneVacuumAgent.movements:
            
            if direction == 'Up':
                return 'Down'
            elif direction == 'Left':
                return 'Right'
            elif direction == 'Down':
                return 'Up'
            elif direction == 'Right':
                return 'Left'
            
        
        return None
            
    def updatePosition(self, direction):
        if direction in NguzzoneVacuumAgent.movements:
            self.clean_streak += 1
            self.past_position = self.position
            
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
        if direction in NguzzoneVacuumAgent.movements:
            if direction == 'Up':
                #if you hit a wall going up, try going to the left
                self.last_direction = 'Left'
            elif direction == 'Left':
                self.last_direction = 'Down' 
            elif direction == 'Down':
                self.last_direction = 'Right'
            elif direction == 'Right':
                self.last_direction = 'Up'
                

#Performs a depth first search 
    def program(self, percept):
        nextMove = ""
        if self.bumpStreak > 4:
            r = random.int(0,3)
            nextMove = NguzzoneVacuumAgent.movements[r]
            return nextMove
            
            # your amazing Ai vacuum cleaner code goes here
        if percept[0] == 'Dirty': 
            self.past_choice = 'Suck'
            return 'Suck'
        else:
            if NguzzoneVacuumAgent.start_val == 1:
                nextMove = NguzzoneVacuumAgent.start(self, percept)
                if nextMove == None:
                    NguzzoneVacuumAgent.start_val = 0
                    NguzzoneVacuumAgent.map_walls_val = 1
                    nextMove = NguzzoneVacuumAgent.map_walls(self, percept)
                return nextMove
            elif NguzzoneVacuumAgent.map_walls_val == 1:
                nextMove = NguzzoneVacuumAgent.map_walls(self, percept)
                if nextMove == None:
                    NguzzoneVacuumAgent.map_walls_val = 0
                    NguzzoneVacuumAgent.inside_val = 1
                return nextMove
            elif NguzzoneVacuumAgent.inside_val == 1:
                nextMove = NguzzoneVacuumAgent.map_inside(self, percept)
                return nextMove
            else: 
                return 'NoOp'
                    
                
            #initial start sequence
            
            
     