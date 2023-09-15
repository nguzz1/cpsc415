# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:49:24 2023

@author: nicolas guzzone

"""



#Note: this is the final verison I am turning in, however it was not intended to be. I was working on 
# a much more complex and intuitive algorithm  but didn't get it working in time and thus shbmitted this one. 

from vacuum import VacuumAgent
import random

class NguzzoneVacuumAgent(VacuumAgent):
    #clean streak keeps track of how many clean tiles the roomba has hit in a row.
    clean_streak = 0
    movements = ['Left','Right','Up', 'Down']
    
    def __init__(self):
        super().__init__()
        #any initiliztion you want to do here
        #most recent move that the vacuum made. It can only be Down, Left, Right or Suck
        self.last_move = ""
        #most recent choice that the vacuum made. It could be a move or 'suck' or 'NoOp'
        self.past_choice = ""
        
    def program(self, percept):
            # your amazing Ai vacuum cleaner code goes here
            
            #print(percept[0], percept[1])
            #if the square is clean and we haven't hit anything then continue moving as you were going
            #if this is our first action in the sequence then pick a random direction and move in it
            
            
            
            if(percept[0] == 'Clean' and percept[1] == 'None'):
                NguzzoneVacuumAgent.clean_streak += 1
                #if the roomba has been on 10+ clean tiles in a row, then go in a random direction. 
                if NguzzoneVacuumAgent.clean_streak > 10:
                    r = random.randint(0, 3)
                    rmove = NguzzoneVacuumAgent.movements[r]
                    #loop infinitley repeats till we generate a random direction that is not the same that we have gone 
                    while rmove == self.last_move:
                        r = random.randint(0, 3)
                        rmove = NguzzoneVacuumAgent.movements[r]
                    self.last_move = rmove
                    self.past_choice = rmove
                    #print(rmove)
                    return rmove
                
                #if the inputted choice is a movement then just keep going
                # I use choice instead of move here since sucking is an action. Incase we just cleaned a tile we keep going in the same direction
                if self.past_choice in NguzzoneVacuumAgent.movements:
                    #print(self.past_choice)
                    return self.past_choice
                
                #if we just sucked then continue moving in the direction we were moving before sucking
                elif self.past_choice == 'Suck' and self.last_move != "":
                    #print(self.last_move)
                    return self.last_move
                else:
                    #if we just started or for any other case just go in a random direction
                    r = random.randint(0, 3)
                    rmove = NguzzoneVacuumAgent.movements[r]
                    while rmove == self.last_move:
                        r = random.randint(0, 3)
                        rmove = NguzzoneVacuumAgent.movements[r]
                    self.last_move = rmove
                    self.past_choice = rmove
                    #print(rmove)
                    return rmove
            #if we just bumped into wall and are on a clean tile then turn left. 
            #Unless we have hit 8 clean tiles in a row then turn right.
            elif (percept[0] == 'Clean' and percept[1] == 'Bump'):
                NguzzoneVacuumAgent.clean_streak += 1
                if NguzzoneVacuumAgent.clean_streak > 8:
                    if self.last_move == 'Left':
                        self.last_move = 'Up'
                        self.past_choice = 'Up'
                     #   print('Up')
                        return 'Up'
                    elif self.last_move == 'Down':
                        self.last_move = 'Left'
                        self.past_choice = 'Left'
                        #print('Left')
                        return 'Left'
                    elif self.last_move == 'Right':
                        self.last_move = 'Down'
                        self.past_choice = 'Down'
                        #print('Down')
                        return 'Down'
                    elif self.last_move == 'Up':
                        self.last_move = 'Right'
                        self.past_choice = 'Right'
                        #print('Right')
                        return 'Right'
                    return rmove
                if self.last_move == 'Left':
                    self.last_move = 'Down'
                    self.past_choice = 'Down'
                    #print('Down')
                    return 'Down'
                elif self.last_move == 'Down':
                    self.last_move = 'Right'
                    self.past_choice = 'Right'
                    #print('Right')
                    return 'Right'
                elif self.last_move == 'Right':
                    self.last_move = 'Up'
                    self.past_choice = 'Up'
                    #print('Up')
                    return 'Up'
                elif self.last_move == 'Up':
                    self.last_move = 'Left'
                    self.past_choice = 'Left'
                    #print('Left')
                    return 'Left'
            #suck any dirt we come accross
            elif (percept[0] == 'Dirty'):
                NguzzoneVacuumAgent.clean_streak = 0
                self.past_choice = 'Suck'
                #print('Suuuuuuck')
                return 'Suck'
            return 'NoOp'