def eval_vis(x, y, tree_grid) -> bool:
    y_len = len(tree_grid)
    x_len = len(tree_grid[0])
    
    vis_right = True
    if x != x_len - 1:
        for i in range(x+1, x_len):
            if tree_grid[y][x] <= tree_grid[y][i]:
                vis_right = False
                break
    
    vis_left = True
    if x != 0:
        for i in range(x-1, -1, -1):
            if tree_grid[y][x] <= tree_grid[y][i]:
                vis_left = False
                break

    vis_top = True
    if y != 0:
        for i in range(y-1, -1, -1):
            if tree_grid[y][x] <= tree_grid[i][x]:
                vis_top = False
                break

    vis_bot = True
    if y != y_len -1:
        for i in range(y+1, y_len):
            if tree_grid[y][x] <= tree_grid[i][x]:
                vis_bot = False
                break

    return vis_right or vis_left or vis_bot or vis_top


def prob1():
    with open('d8_in.txt','r') as file:
        trees_visible = 0
        tree_rows = []
        for tree_row in file:
            tree_row = tree_row.strip()
            tree_rows.append(tree_row)
        
        for y, tree_row in enumerate(tree_rows):
            for x, _ in enumerate(tree_row):
                if eval_vis(x, y, tree_rows):
                    trees_visible += 1

        print(trees_visible)

def eval_scenic_score(x, y, tree_grid) -> int:
    y_len = len(tree_grid)
    x_len = len(tree_grid[0])
    
    vis_right = 0
    if x != x_len - 1:
        for i in range(x+1, x_len):
            vis_right += 1
            if tree_grid[y][x] <= tree_grid[y][i]:
                break
    
    vis_left = 0
    if x != 0:
        for i in range(x-1, -1, -1):
            vis_left +=1
            if tree_grid[y][x] <= tree_grid[y][i]:
                break

    vis_top = 0
    if y != 0:
        for i in range(y-1, -1, -1):
            vis_top += 1
            if tree_grid[y][x] <= tree_grid[i][x]:
                break

    vis_bot = 0
    if y != y_len -1:
        for i in range(y+1, y_len):
            vis_bot += 1
            if tree_grid[y][x] <= tree_grid[i][x]:
                break

    return vis_right * vis_left * vis_top * vis_bot

def prob2():
    with open('d8_in.txt','r') as file:
        tree_rows = []
        for tree_row in file:
            tree_row = tree_row.strip()
            tree_rows.append(tree_row)
        
        scenic_scores = []
        for y, tree_row in enumerate(tree_rows):
            for x, _ in enumerate(tree_row):
                scenic_scores.append(eval_scenic_score(x, y, tree_rows))
                    
        scenic_scores.sort()
        print(scenic_scores[-1])

prob1()
prob2()
