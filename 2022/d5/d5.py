def create_stacks(lines: list[str]):
    stack_num = len(lines.pop(-1)) -1
    stacks = [[] for _ in range(stack_num)]
    for line in lines[::-1]:
        for i in range(1, len(line), 4):
            if line[i] != " " and line[i] != "\n":
                stacks[i >> 2].append(line[i])
    return stacks
    
def prob1():
    with open('d5_in.txt','r') as file:
        lines = file.readlines()
        stacks = [[]]
        index = 0
        for i, line in enumerate(lines):
            if line == "\n":
                index = i 
                stacks = create_stacks(lines[:i])
                break
        for line in lines[index+1:]:
            instructions = line.split()
            new_stack = int(instructions[5]) - 1
            old_stack = int(instructions[3]) - 1
            moves = int(instructions[1])
            for i in range(moves):
                stacks[new_stack].append(stacks[old_stack].pop())
        for stack in stacks:
            if stack:
                print(stack[-1])
                
def prob2():
    with open('d5_in.txt','r') as file:
        lines = file.readlines() 
        stacks = [[]]
        index = 0
        for i, line in enumerate(lines):
            if line == "\n":
                index = i 
                stacks = create_stacks(lines[:i])
                break
        for line in lines[index+1:]:
            instructions = line.split()
            new_stack = int(instructions[5]) - 1
            old_stack = int(instructions[3]) - 1
            moves = int(instructions[1])

            stacks[new_stack] += stacks[old_stack][-moves:]
            for i in range(moves):
                stacks[old_stack].pop() 
        for stack in stacks:
            if stack:
                print(stack[-1])



prob1()
print('----------------------')
prob2()
