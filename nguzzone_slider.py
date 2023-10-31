
'''
CPSC 415 -- Homework #2.667 template
Stephen Davies, University of Mary Washington, fall 2023
'''

from puzzle import Puzzle
import numpy as np
import sys
from copy import deepcopy

#Calculates the number of tiles out of place
def h1(puzzle):

    grid = puzzle.grid
    n = len(grid)
    count = 0
    
    #loop through each tile
    for i in range(n):
        for j in range(n):
            if grid[i,j] != -1 and grid[i,j] != i * n + j + 1:
                count += 1
                
    return count

#Calculates the sum of distances of tiles from their correct positions
def h2(puzzle):
  
    grid = puzzle.grid
    n = len(grid)
    totalDist = 0
    
    # Loop through every tile in the grid.
    for i in range(n):
        for j in range(n):
            # If the tile isn't the blank space.
            if grid[i,j] != -1:
                # Calculate the correct row and column for the tile.
                goalI = (grid[i,j] - 1) // n
                goalJ = (grid[i,j] - 1) % n

                # Calculate the number of moves/tiles away the current tile is from its goal position
                totalDist += abs(i - goalI) + abs(j - goalJ)

    # Return the total calculated distance.
    return totalDist


#Inserts move sequence into the frontier in the right position
def updateFrontier(frontier, frontierEstimates, moves, estimate):
  
    index = 0
    #go through all estimates until we reac hthe position where the newEst should be inserted
    for e in frontierEstimates.values():
        if e > estimate:
            break
        index += 1
    frontier.insert(index, moves)
    frontierEstimates[moves] = estimate
    
    
def solve(p):
    '''A* search with h2 heuristic to solve the puzzle.'''
    frontier = [()]
    frontierEstimates = {(): h2(p)}
    frontierPuzzles = {(): deepcopy(p)}
    
    # Keep track of visited states
    visited = set()
    visited.add(str(p.grid))  
    
    #while the frontier isn't empty keep loopin
    while frontier:
        #get first node in frontier and info of that node
        node = frontier.pop(0)
        curP = frontierPuzzles[node]
     
        #check for solution. if so we end loop
        if curP.is_solved():
            return list(node)

        #go through all legal moves 
        for move in curP.legal_moves():
            copy_of_puzzle = deepcopy(curP)
            copy_of_puzzle.move(move)

            # Check if we've already visited this state
            if str(copy_of_puzzle.grid) in visited:
                continue  # Skip this state if we have
            
            # Mark this state as visited
            visited.add(str(copy_of_puzzle.grid))
            
            new_node = node + (move,)
            
            #if the new node isnt in the frontier then update the frontier
            if new_node not in frontierPuzzles:
                newEst = len(new_node) + h2(copy_of_puzzle)
                updateFrontier(frontier, frontierEstimates, new_node, newEst)
                frontierPuzzles[new_node] = copy_of_puzzle
    #return nothing for no solution
    return []



if __name__ == '__main__':

    if (len(sys.argv) not in [2,3]  or
        not sys.argv[1].isnumeric()  or
        len(sys.argv) == 3 and not sys.argv[2].startswith("seed=")):
        sys.exit("Usage: puzzle.py dimensionOfPuzzle [seed=###].")

    n = int(sys.argv[1])

    if len(sys.argv) == 3:
        seed = int(sys.argv[2][5:])
    else:
        seed = 123

    # Create a random puzzle of the appropriate size and solve it.
    puzzle = Puzzle.gen_random_puzzle(n, seed)
    print(puzzle)
    solution = solve(puzzle)
    if puzzle.has_solution(solution):
        input("Yay, this puzzle is solved! Press Enter to watch.")
        puzzle.verify_visually(solution)
    else:
        print(f"Sorry, {''.join(solution)} does not solve this puzzle.")