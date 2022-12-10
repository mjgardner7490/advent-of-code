from pprint import pprint

def is_desired_cycle(x):
    if x == 20 or x == 60 or x == 100 or x == 140 or x == 180 or x == 220:
        return True
    return False

def prob1(): 
    with open('d10_in.txt','r') as file:
        x = 1
        cycle = 0
        cycle_measurements = []
        for instruction in file.readlines():
            commands = instruction.strip().split()
            if commands[0] == "noop":
                cycle += 1
                if is_desired_cycle(cycle):
                    cycle_measurements.append(cycle * x)
            if commands[0] == "addx":
                for _ in range(2):
                    cycle += 1
                    if is_desired_cycle(cycle):
                        cycle_measurements.append(cycle * x)
                x += int(commands[1])

        print(sum(cycle_measurements))

def draw(crt, x, cycle):
    draw_pixel_loc = (cycle -1) % 40
    if x == draw_pixel_loc or x == draw_pixel_loc - 1 or x == draw_pixel_loc + 1:
        crt[cycle // 40][draw_pixel_loc] = "#"

def prob2():
    with open('d10_in.txt','r') as file:
        crt = [['.' for col in range(40)] for row in range(6)]
        x = 1
        cycle = 0
        for instruction in file.readlines():
            commands = instruction.strip().split()
            if commands[0] == "noop":
                cycle += 1
                draw(crt, x, cycle)
            if commands[0] == "addx":
                for _ in range(2):
                    cycle += 1
                    draw(crt, x, cycle)
                x += int(commands[1])
        pprint(crt, width = 300)
        

prob1()
prob2()
            


