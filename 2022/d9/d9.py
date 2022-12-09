def is_adjacent(xh, yh, xt, yt) -> bool:
    # On top of 
    if (xh == xt) and (yh == yt):
        return True
    # Left
    if (xh - xt == 1) and (yh == yt):
        return True
    # Right
    if (xt - xh == 1) and (yh == yt):
        return True
    # Above
    if (yh - yt == 1) and (xh == xt):
        return True
    # Below
    if (yt - yh == 1) and (xh == xt):
        return True
    # upper left
    if (yh - yt == 1) and (xh - xt == 1):
        return True
    # upper right
    if (yh - yt == 1) and (xt - xh == 1):
        return True
    # lower right
    if (yt - yh == 1) and (xt - xh == 1):
        return True
    # lower left
    if (yt - yh == 1) and (xh - xt == 1):
        return True
    return False

def move(xh, yh, xt, yt):
    # Right
    if (xh - xt > 1) and (yh == yt):
        xt = xh - 1
    # Left
    if (xt - xh > 1) and (yh == yt):
        xt = xh + 1
    # Down
    if (yh - yt > 1) and (xh == xt):
        yt = yh - 1 
    # Up
    if (yt - yh > 1) and (xh == xt):
        yt = yh + 1
    
    # right far & up/down
    if (abs(yh - yt) == 1) and (xh - xt > 1): 
        yt = yh
        xt = xh - 1
    # left far & up/down
    if (abs(yh - yt) == 1) and (xt - xh > 1): 
        yt = yh
        xt = xh + 1
    # down far & left/right
    if (yh - yt > 1) and (abs(xh - xt) == 1):
        xt = xh
        yt = yh - 1
    # up far & left/right
    if (yt - yh > 1) and (abs(xt - xh) == 1):
        xt = xh
        yt = yh + 1
        
    # far up and far right
    if (yt - yh > 1) and (xh - xt > 1):
        xt = xt + 1
        yt = yt - 1
    # far up and far left
    if (yt - yh > 1) and (xt - xh > 1):
        xt = xt - 1
        yt = yt - 1
    # far down and far right
    if (yh - yt > 1) and (xh - xt > 1):
        xt = xt + 1
        yt = yt + 1
    # far down and far left
    if (yh - yt > 1) and (xt - xh > 1):
        xt = xt - 1
        yt = yt + 1

    return xt,yt

def prob1():
    with open('d9_in.txt','r') as file:
        xh, yh, xt, yt =  0, 0, 0, 0
        locs = set((0,0))
        for movement in file:
            dir, mag = movement.strip().split()
            mag = int(mag)
            for _ in range(mag):
                if dir == "R":
                    xh += 1 
                if dir == "L":
                    xh -= 1
                if dir == "D":
                    yh += 1
                if dir == "U":
                    yh -= 1
                if not is_adjacent(xh, yh, xt, yt):
                    x, y = move(xh, yh, xt, yt)
                    yt = y
                    xt = x
                    locs.add((xt,yt))
        print(len(locs))


def prob2():
    with open('d9_in.txt','r') as file:
        knots = []
        for _ in range(10):
            knots.append([0, 0])
        locs = set((0,0))
        for movement in file:
            dir, mag = movement.strip().split()
            mag = int(mag)
            for _ in range(mag):
                if dir == "R":
                    knots[0][0] = knots[0][0] + 1
                if dir == "L":
                    knots[0][0] = knots[0][0] - 1
                if dir == "D":
                    knots[0][1] = knots[0][1] + 1
                if dir == "U":
                    knots[0][1] = knots[0][1] - 1
                for index, knot in enumerate(knots[1:]):
                    if not is_adjacent(knots[index][0], knots[index][1], knot[0], knot[1]):  
                        x, y = move(knots[index][0], knots[index][1], knot[0], knot[1])
                        knot[1] = y
                        knot[0] = x
                        if index == 8:
                            locs.add((x, y))
        print(len(locs))

prob1()
prob2()

