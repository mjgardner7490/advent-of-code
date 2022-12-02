"""
X, A = Rock
Y, B = Paper
Z, C = Scissor
"""
strategy_guide = { 
        ('A','X'):1 + 3,
        ('A','Y'):2 + 6,
        ('A','Z'):3,
        ('B','X'):1,
        ('B','Y'):2 + 3,
        ('B','Z'):3 + 6,
        ('C','X'):1 + 6,
        ('C','Y'):2,
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
