from pprint import pprint
import time

def draw_paths(grid, rock_coords, norm_factor):
    for rock_path in rock_coords:
        for i in range(len(rock_path) - 1):
            c1 = rock_path[i]
            c2 = rock_path[i+1]
            if c1[0] > c2[0]: 
                for x in range(c2[0], c1[0]+1):
                    grid[c1[1]][x-norm_factor] = "#"
            # # right
            if c1[0] < c2[0]: 
                for x in range(c1[0], c2[0]+1):
                    grid[c1[1]][x-norm_factor] = "#"
            # # down
            if c1[1] < c2[1]: 
                for y in range(c1[1], c2[1]+1):
                    grid[y][c1[0]-norm_factor] = "#"
            # # up 
            if c1[1] > c2[1]: 
                for y in range(c2[1], c1[1]+1):
                    grid[y][c1[0]-norm_factor] = "#"
    return grid

def sand_simulator(grid, last_rock_height, norm_factor):
    sand_count = 0
    falling_into_abyss = False
    while not falling_into_abyss:
        curr_x = 500-norm_factor 
        curr_y = 0
        if grid[curr_y][curr_x] == "o":
            falling_into_abyss = True
        at_rest = False
        while not at_rest:
            if grid[curr_y+1][curr_x] == ".":
                curr_y += 1
                if curr_y == last_rock_height:
                    falling_into_abyss = True
                    at_rest=True
            elif grid[curr_y+1][curr_x-1] == ".":
                curr_x -= 1
                curr_y += 1
                if curr_y == last_rock_height:
                    falling_into_abyss = True
                    at_rest=True
            elif grid[curr_y+1][curr_x+1] == ".":
                curr_x += 1
                curr_y += 1
                if curr_y == last_rock_height:
                    falling_into_abyss = True
                    at_rest=True
            else:
                grid[curr_y][curr_x] = "o"
                at_rest=True
        if not falling_into_abyss:
            sand_count += 1
        # pprint(grid, width=600)
        # time.sleep(0.5)
    return sand_count, grid

def prob1():
    with open('d14_in.txt', 'r') as file:  
        columns = 500
        rows = 500
        norm_factor = 500 - columns//2
        grid = [['.' for col in range(columns)] for row in range(rows)] 
        rock_coords = []
        for line in file.readlines():
            coords = line.strip().split('->')
            clean_coords = [c.strip().split(',') for c in coords]
            rock_coords.append([(int(c[0]),int(c[1])) for c in clean_coords])
        
        grid = draw_paths(grid, rock_coords, norm_factor)
        last_rock_height = 0
        for index, line in enumerate(grid):
            for char in line:
                if char == "#":
                    if last_rock_height < index:
                        last_rock_height = index
        
        sand_count, grid = sand_simulator(grid, last_rock_height, norm_factor)
        print(sand_count)
        
def prob2():
    with open('d14_in.txt', 'r') as file:  
        columns = 500
        rows = 500
        norm_factor = 500 - columns//2
        grid = [['.' for col in range(columns)] for row in range(rows)] 
        rock_coords = []
        for line in file.readlines():
            coords = line.strip().split('->')
            clean_coords = [c.strip().split(',') for c in coords]
            rock_coords.append([(int(c[0]),int(c[1])) for c in clean_coords])
        
        grid = draw_paths(grid, rock_coords, norm_factor)
        last_rock_height = 0
        for index, line in enumerate(grid):
            for char in line:
                if char == "#":
                    if last_rock_height < index:
                        last_rock_height = index
        
        grid[last_rock_height+2] = ["#" for _ in range(len(grid[0]))]
        
        sand_count, grid = sand_simulator(grid, last_rock_height+2, norm_factor)
        print(sand_count)

prob1()
prob2()
