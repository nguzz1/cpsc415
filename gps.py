#!/usr/bin/env python3

'''
CPSC 415 -- Homework #2 template
Nicolas Guzzone, University of Mary Washington, fall 2023
'''

from atlas import Atlas
import numpy as np
import math
import sys


def find_path(atlas, alg):
    '''Finds a path from src to dest using a specified algorithm, and
    based on costs from the atlas provided. The second argument must be one
    of the values "greedy", "Dijkstras", or "A*".

    Returns a tuple of two elements. The first is a list of city numbers,
    starting with 0 and ending with atlas.num_cities-1, that gives the
    optimal path between those two cities. The second is the total cost
    of that path.'''

    print(atlas)
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
    pastNode = (0,0)
    shortestCrow = 0
    shortestRDist = 0
    total = 0
    path = []
    rowsVisited = []
    deadEnds = []
    goal = False
    goal_city = Atlas.get_num_cities(atlas) - 1 #this number is the goal city and the number of rows and columns in the matrix
    recentDist = 0
    print(f"The goal city is: {goal_city}")
    #While we have not entered the goal state/city, keep searching
    short_i = 0
    short_j = 0
    w = 0
    while goal == False:
        #loop through every column in the current row
        w += 1
        print("===============================")
        print(f'while loop: {w}')
        infCount = 0
        
        for i in range(Atlas.get_num_cities(atlas)):
            print()
            print()
            #calculate the crowFlys distance for this node
            cFly = Atlas.get_crow_flies_dist(atlas, i, j)
            print(f"i : {i} , j : {j}")
            
            if i in deadEnds:
                print("deadend detected...")
                

                
            #if the crowFlys distance is the shortest we've come across on this row or is the first save it
            elif(shortestCrow != 0 and cFly < shortestCrow) or shortestCrow == 0:
                print( f"is {cFly} < {shortestCrow} or its 0")
                rDist = Atlas.get_road_dist(atlas,i, j)
                heuristicNode = (j,i)
                '''
                if i in rowsVisited:
                    print("already visited this row...")
                    
                    #Add code here that will allow us to visit a row we have been to before
                    
                    if rDist != math.inf and rDist != 0 and rDist != recentDist:
                        #save the distances of this node as the current shortest distances we have come across, as well as the position of it.
                        shortestRDist = rDist
                        shortestCrow = cFly
                        short_i = i
                        short_j = j
                        print(f"short i and j: {short_i} , {short_j}")
                    elif rDist == math.inf:
                        infCount += 1
                        print(f"number of inf: {infCount}")
                '''          
                #node where we found the shortest crows fly distance of the current row
                
                #get the road distance of the current node since it has the lowest heuristic
               
               # print(f"heuristic i: {heuristicNode[0]}, j: {heuristicNode[1]}")
                print(f"rDist : {rDist}")
                #if a road exists to the city with the smallest crows fly distance and we havent been to this city before, then go to it
                if rDist != math.inf and rDist != 0 and rDist != recentDist:
                    #save the distances of this node as the current shortest distances we have come across, as well as the position of it.
                    shortestRDist = rDist
                    shortestCrow = cFly
                    short_i = i
                    short_j = j
                    print(f"short i and j: {short_i} , {short_j}")
                elif rDist == math.inf:
                    infCount += 1
                    print(f"number of inf: {infCount}")
        #once we have reached the end of the row, update our node, distance and path with that of the node with the lowest heuristic             
        heuristicNode = (short_j, short_i)
        rowsVisited.append(j)
        if infCount ==  goal_city - 1:
            print("HIT A DEAD END!!!!!")
            shortestRDist = recentDist
            print(f"deadend_recentDist = {recentDist}")
            deadEnds.append(j)
            j = short_j
            print(f"j = {j}, pastNode = {pastNode}")
            
        else: 
            j = short_i
        recentDist = shortestRDist
        pastNode = (short_i,short_j)
        #move to the row of the city we just decided to go to
        path.append(heuristicNode)
        total += shortestRDist
        
        
        print(f"shortestHeuristic = {heuristicNode}")
        print(f"shortestRDist = {shortestRDist}")
        print(f"new j / row = {j}")
        print(f"recentDist = {recentDist}")
        #print("heuristicNode info: {heuristicNode[0],heuristicNode[1]")
        #reset shortestCrow and closestNode
        shortestCrow = 0
        heuristicNode = (0,0)
        
           
        #check to see if we have entered the goal state/city/row 
        if j == goal_city:
            goal = True
        print(goal)
       # if w > 7:
          #  goal = True
    return path, total

                
                
                
            

def djikstras(atlas):
    return "Unimplemented"

def aStar(atlas):
    return "Unimplemented"


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

