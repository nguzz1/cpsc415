#!/usr/bin/env python3

'''
CPSC 415 -- Homework #2 template
Nicolas Guzzone, University of Mary Washington, fall 2023
'''

from atlas import Atlas
import numpy as np
import sys


def find_path(atlas, alg):
    '''Finds a path from src to dest using a specified algorithm, and
    based on costs from the atlas provided. The second argument must be one
    of the values "greedy", "Dijkstras", or "A*".

    Returns a tuple of two elements. The first is a list of city numbers,
    starting with 0 and ending with atlas.num_cities-1, that gives the
    optimal path between those two cities. The second is the total cost
    of that path.'''

    # THIS IS WHERE YOUR AMAZING CODE GOES
    if alg == 'greedy':
        return greedy(atlas)
    elif alg == 'Dijkstras':
        return djikstras(atlas)
    elif alg == 'A*':
        return aStar(atlas)
    
    

    # Here's a (bogus) example return value:
    return ([0,3,2,4],970)


def greedy(atlas):
    i = 0
    j = 0
    heuristicNode = (i,j)
    shortestCrow = 0
    total = 0
    path = []
    goal = False
    goal_city = Atlas.get_num_cities() - 1 #this number is the goal city and the number of rows and columns in the matrix
    
    
    #While we have not entered the goal state/city, keep searching
    while goal == False:
        #loop through every column in the current row
        
        for i in range(goal_city):
            #calculate the crowFlys distance for this node
            cFly = Atlas.get_crow_flies_dist(i, j)
            
            #if the crowFlys distance is the shortest we've come across on this row, save it
            if cFly < shortestCrow or shortestCrow == 0:
                shortestCrow = cFly
                #node where we found the shortest crows fly distance of the current row
                heuristicNode = (i,j)
                
            #if we are at the final column in the row, expand the column who has the shortest crow flys distance to the goal
            if i == goal_city: 
                #add the road distance to the total distance of the path taken
                total += Atlas.get_road_dist(heuristicNode[0], heuristicNode[1])
                #add the node we expanded to our path
                path.append(heuristicNode)
                #move the the row of the new city we just decided to go to
                j = heuristicNode[i]
                #reset shortestCrow and closestNode
                shortestCrow = 0
                heuristicNode = (0,0)
        #check to see if we have entered the goal state/city/row 
        if j == goal_city:
            goal = True
            
    return path, total
                
                
                
            
    return None

def djikstras(atlas):
    return None

def aStar(atlas):
    return None


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage: gps.py numCities|atlasFile algorithm.")
        sys.exit(1)

    if len(sys.argv) > 2:
        if sys.argv[2] not in ['greedy', 'Dijkstras', 'A*']:
            print(f'Algorithm must be one of: "greedy", "Dijkstras", or "A*".'
                f' (You put "{sys.argv[2]}".)')
            sys.exit(2)
        else:
            alg = sys.argv[2]

    try:
        num_cities = int(sys.argv[1])
        print(f'Building random atlas with {num_cities} cities...')
        usa = Atlas(num_cities)
        print('...built.')
    except:
        print(f'Loading atlas from file {sys.argv[1]}')
        usa = Atlas.from_filename(sys.argv[1])
        print('...loaded.')

    path, cost = find_path(usa, alg)
    print(f'The {alg} path from 0 to {usa.get_num_cities()-1}'
        f' costs {cost}: {path}.')
    ne = usa._nodes_expanded
    print(f'It expanded {len(ne)} nodes: {ne}')

