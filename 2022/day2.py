"""
X, A = Rock
Y, B = Paper
Z, C = Scissor
"""
strategy_guide = { 
        ('A','X'):3 + 1,
        ('A','Y'):6 + 2,
        ('A','Z'):0 + 3,
        ('B','X'):0 + 1,
        ('B','Y'):3 + 2,
        ('B','Z'):6 + 3,
        ('C','X'):6 + 1,
        ('C','Y'):0 + 2,
        ('C','Z'):3 + 3,
}
def prob1():
    with open('day2_input.txt','r') as file:
        score = 0
        for round in file:
            opp_play, my_play = round.split()
            score += strategy_guide[(opp_play, my_play)]
        print(score)

"""
X = lose
Y = draw
Z = win
"""
"""
A = Rock = 1
B = Paper = 2
C = Scissor = 3
"""
strategy_guide_2 = {
        ('X','A'):3,
        ('X','B'):1,
        ('X','C'):2,
        ('Y','A'):1 + 3,
        ('Y','B'):2 + 3,
        ('Y','C'):3 + 3, 
        ('Z','A'):2 + 6,
        ('Z','B'):3 + 6,
        ('Z','C'):1 + 6, 
}

def prob2():
    with open('day2_input.txt','r') as file:
        score = 0
        for round in file:
            opp_play, my_play = round.split()
            score += strategy_guide_2[(my_play, opp_play)]
        print(score)

prob1()
prob2()
