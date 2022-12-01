def prob1(): 
    with open('day1_input.txt','r') as file:
        max_cals = 0
        curr_cals = 0
        for line in file:
            if line == "\n":
                if curr_cals > max_cals:
                    max_cals = curr_cals
                curr_cals = 0
            else:
                line_value = int(line)
                curr_cals = curr_cals + line_value

        print(f'Max Cals: {max_cals}')

def prob2():
    with open('day1_input.txt','r') as file:
        curr_cals = 0
        inventory = []
        for line in file:
            if line == "\n":
                inventory.append(curr_cals)
                curr_cals = 0
            else:
                line_value = int(line)
                curr_cals = curr_cals + line_value

        inventory.sort()
        top_cals = sum(inventory[-3:])
        print(f'Top 3 Cal Sum: {top_cals}')

prob1()
prob2()
            


