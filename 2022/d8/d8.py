from pprint import pprint

def eval_vis(x, y, tree_grid) -> int:
    # print(f'x: {x}, y:{y}')
    # print(f'tree: {tree_grid[y][x]}')
    y_len = len(tree_grid)
    x_len = len(tree_grid[0])
    
    vis_right = True
    if x != x_len - 1:
        for i in range(x+1, x_len):
            # print(f'right comp:{tree_grid[y][i]}')
            if tree_grid[y][x] <= tree_grid[y][i]:
                vis_right = False
                break
    
    vis_left = True
    if x != 0:
        for i in range(x-1, -1, -1):
            # print(f'left comp:{tree_grid[y][i]}')
            if tree_grid[y][x] <= tree_grid[y][i]:
                vis_left = False
                break

    vis_top = True
    if y != 0:
        for i in range(y-1, -1, -1):
            # print(f'top comp:{tree_grid[i][x]}')
            if tree_grid[y][x] <= tree_grid[i][x]:
                vis_top = False
                break

    vis_bot = True
    if y != y_len -1:
        for i in range(y+1, y_len):
            # print(f'bot comp:{tree_grid[i][x]}')
            if tree_grid[y][x] <= tree_grid[i][x]:
                vis_bot = False
                break

    # print(f'right: {vis_right}, left:{vis_left}')
    # print(f'top: {vis_top}, bot:{vis_bot}')
    if vis_right or vis_left or vis_bot or vis_top:
        return 1
    else:
        return 0


def prob1():
    with open('d8_in.txt','r') as file:
        tree_grid = [[]]
        tree_rows = []
        visible = 0
        for index, tree_row in enumerate(file):
            tree_row = tree_row.strip()
            tree_rows.append(tree_row)
            tree_grid.append([])
            for tree in tree_row:
                tree_grid[index].append(int(tree))
        
        tree_grid = tree_grid[:-1]
        # print(tree_rows)
        pprint(tree_grid)

        for y, tree_row in enumerate(tree_grid):
            for x, tree in enumerate(tree_row):
                visible += eval_vis(x, y, tree_grid)
                print('--------')

        print(visible)

def eval_scenic_score(x, y, tree_grid) -> int:
    y_len = len(tree_grid)
    x_len = len(tree_grid[0])
    
    vis_right = 0
    if x != x_len - 1:
        for i in range(x+1, x_len):
            if tree_grid[y][x] > tree_grid[y][i]:
                vis_right += 1
            elif tree_grid[y][x] <= tree_grid[y][i]:
                vis_right += 1
                break
            else:
                break
    
    vis_left = 0
    if x != 0:
        for i in range(x-1, -1, -1):
            if tree_grid[y][x] > tree_grid[y][i]:
                vis_left += 1
            elif tree_grid[y][x] <= tree_grid[y][i]:
                vis_left +=1
                break
            else:
                break

    vis_top = 0
    if y != 0:
        for i in range(y-1, -1, -1):
            if tree_grid[y][x] > tree_grid[i][x]:
                vis_top += 1
            elif tree_grid[y][x] <= tree_grid[i][x]:
                vis_top += 1
                break
            else:
                break

    vis_bot = 0
    if y != y_len -1:
        for i in range(y+1, y_len):
            if tree_grid[y][x] > tree_grid[i][x]:
                vis_bot += 1
            elif tree_grid[y][x] <= tree_grid[i][x]:
                vis_bot += 1
                break
            else:
                break

    print(f'right: {vis_right}, left:{vis_left}')
    print(f'top: {vis_top}, bot:{vis_bot}')
    test = vis_right * vis_left * vis_top * vis_bot
    print(test)
    return vis_right * vis_left * vis_top * vis_bot

def prob2():
    with open('d8_in.txt','r') as file:
        tree_grid = [[]]
        tree_rows = []
        for index, tree_row in enumerate(file):
            tree_row = tree_row.strip()
            tree_rows.append(tree_row)
            tree_grid.append([])
            for tree in tree_row:
                tree_grid[index].append(int(tree))
        
        tree_grid = tree_grid[:-1]
        pprint(tree_grid)

        scenic_scores = []
        for y, tree_row in enumerate(tree_grid):
            for x, tree in enumerate(tree_row):
                scenic_scores.append(eval_scenic_score(x, y, tree_grid))

        test = scenic_scores.sort()
        print(scenic_scores)
        print(scenic_scores[-1])



# prob1()
prob2()
