#!/usr/bin/env python3

'''
CPSC 415 -- Homework #2 template
Nicolas Guzzone, University of Mary Washington, fall 2023
'''

from atlas import Atlas
import numpy as np
import sys
import math


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

    cities = atlas.get_num_cities()
    
    #Atlas Copy of the rows with boolean value of whethe ror not we have visited it
    #make all cities false since we have never visited them yet
    expanded = [False] * cities
    #keep track of all the actual distances of each city
  
    start = 0
    goal = cities - 1
    
    #list that keeps track of the entire path
    path = [start]
    total = 0
    
    
    curr_city = start 
    
    #while we are not in the goal keep trying to find the goal
    while curr_city != goal:
        
        #we have expanded the city we are currently at
        expanded[curr_city] = True
        
        #variable that keeps track of the smallest crows fly distance of the current row
        smallest = math.inf
        #next city we should visit
        go_here = None
        #loop through every city in the row
        for city in range(cities):
            # if we haven't expanded the city yet, then check its distances
            if not expanded[city]:
                rDist = atlas.get_road_dist(curr_city, city)
                cDist = atlas.get_crow_flies_dist(city, goal)
                #if a road exists between the cities, then check the heuristic
                if rDist < math.inf:
                    #check to see if the crow flys distance of this city is the smallest 
                    #if it is, we go to that city
                    if cDist < smallest:
                        smallest = cDist
                        go_here = city
        #afd the path cost to our total cost              
        total += atlas.get_road_dist(curr_city, go_here)
       
        #add the city to our path
        path.append(go_here)
        #update our current city
        curr_city = go_here
        
    total += atlas.get_road_dist(curr_city, go_here)
    path.append(go_here)
 

    
    #I need to restart. fuck this rabbithole
    return path, total

                
                
                

def djikstras(atlas):

    cities = atlas.get_num_cities()
    
    #Atlas Copy of the rows with boolean value of whethe ror not we have visited it
    #make all cities false since we have never visited them yet
    expanded = [False] * cities
    #keep track of all the actual distances of each city
  
    start = 0
    goal = cities - 1
    
    #list that keeps track of the entire path
    path = [start]
    total = 0
    
    
    curr_city = start 
    pq = [(0, start)]

    while pq:
        smallDist = math.inf
        smallIndex = None
        
        for i, (dist, city) in enumerate(pq):
            if dist < smallDist:
                smallDist = dist
                smallIndex = i
                
        dist, curr_city = pq.pop(smallIndex)
        
        
        if expanded[curr_city]:
            continue
        
        
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

