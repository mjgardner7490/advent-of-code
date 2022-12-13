from pprint import pprint
import math
import copy

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def shortest_search(grid, unvisited_coords, curr_loc):
    next_coords = set()
    next_coords.add((curr_loc.x,curr_loc.y))

    while len(next_coords) !=0:
        coords = next_coords.pop()
        x = coords[0]
        y = coords[1]

        # Right
        if x < len(grid[0]) - 1:
            if grid[y][x + 1][1] == math.inf or grid[y][x + 1][1] > grid[y][x][1] + 1:
                if grid[y][x + 1][0] <= grid[y][x][0] + 1:
                    grid[y][x + 1] = (grid[y][x+1][0], grid[y][x][1] + 1)
                    unvisited_coords.add((x + 1, y))
                    next_coords.add((x + 1, y))

        # Left
        if x > 0:
            if grid[y][x - 1][1] == math.inf or grid[y][x - 1][1] > grid[y][x][1] + 1:
                if grid[y][x - 1][0] <= grid[y][x][0] + 1:
                    grid[y][x - 1] = (grid[y][x-1][0], grid[y][x][1] + 1)
                    unvisited_coords.add((x - 1, y))
                    next_coords.add((x - 1, y))
        # Up
        if y > 0:
            if grid[y - 1][x][1] == math.inf or grid[y - 1][x][1] > grid[y][x][1] + 1:
                if grid[y - 1][x][0] <= grid[y][x][0] + 1:
                    grid[y - 1][x] = (grid[y-1][x][0], grid[y][x][1] + 1)
                    unvisited_coords.add((x, y - 1))
                    next_coords.add((x, y - 1))
        # Down
        if y < len(grid) - 1:
            if grid[y + 1][x][1] == math.inf or grid[y + 1][x][1] > grid[y][x][1] + 1:
                if grid[y + 1][x][0] <= grid[y][x][0] + 1:
                    grid[y + 1][x] = (grid[y+1][x][0], grid[y][x][1] + 1)
                    unvisited_coords.add((x, y + 1))
                    next_coords.add((x, y + 1))

        unvisited_coords.remove((x,y)) 
    return grid


def prob1(): 
    with open('d12_in.txt','r') as file:
        start = None
        finish = None
        grid = []
        unvisited_coords = set()
        for y, line in enumerate(file.readlines()):
            grid.append([])
            for x, char in enumerate(line.strip()): 
                if char == 'S':
                    start = Location(x, y)
                    grid[y].append((ord('a'), 0))
                elif char == 'E':
                    finish = Location(x, y)
                    grid[y].append((ord('z'), math.inf))
                else:
                    grid[y].append((ord(char), math.inf))
                unvisited_coords.add((x,y))

        grid = shortest_search(grid, unvisited_coords, start)
        print(grid[finish.y][finish.x][1])

def prob2(): 
    with open('d12_in.txt','r') as file:
        finish = None
        grid = []
        unvisited_coords = set()
        for y, line in enumerate(file.readlines()):
            grid.append([])
            for x, char in enumerate(line.strip()): 
                if char == 'S':
                    grid[y].append((ord('a'), math.inf))
                elif char == 'E':
                    finish = Location(x, y)
                    grid[y].append((ord('z'), math.inf))
                else:
                    grid[y].append((ord(char), math.inf))
                unvisited_coords.add((x,y))

        paths = []
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col[0] == ord('a'):
                    grid_copy = copy.deepcopy(grid)
                    unvisited_coords_copy = copy.deepcopy(unvisited_coords)

                    grid_copy[y][x] = (grid_copy[y][x][0], 0)

                    new_grid = shortest_search(grid_copy, unvisited_coords_copy, Location(x,y))
                    if new_grid[finish.y][finish.x][1] != math.inf:
                        paths.append(new_grid[finish.y][finish.x][1])
        paths.sort()
        print(paths[0])

prob1()
prob2()
            


