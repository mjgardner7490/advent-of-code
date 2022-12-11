from pprint import pprint

class Monkey:
    def __init__(self):
        self.s_items = []
        self.worry_mod = None
        self.test_num = None
        self.true_path = None
        self.false_path = None
        self.items_inspected = 0

    def create_monkey(self, description):
        for line in description.split('\n'):
            words = line.split() 
            if words[1] == "items:":
                for word in words[2:]:
                    word = word.strip(',')
                    self.s_items.append(int(word)) 
            if words[0] == "Operation:":
                self.worry_mod = words[4:]
            if words[0] == "Test:": 
                self.test_num = int(words[3])
            if words[1] == "true:":
                self.true_path = int(words[5])
            if words[1] == "false:":
                self.false_path = int(words[5])
        return self

def inspect(monkey, monkeys, common_divisor=None):
    for worry_level in monkey.s_items:
        monkey.items_inspected += 1
        if common_divisor:
            worry_level %= common_divisor

        if monkey.worry_mod[0] == "+":
            if monkey.worry_mod[1] == "old":
                worry_level += worry_level
            else:
                worry_level += int(monkey.worry_mod[1])

        if monkey.worry_mod[0] == "*":
            if monkey.worry_mod[1] == "old":
                worry_level *= worry_level
            else:
                worry_level *= int(monkey.worry_mod[1])

        if not common_divisor:
            worry_level = worry_level // 3

        if (worry_level % monkey.test_num == 0):
            monkeys[monkey.true_path].s_items.append(worry_level)
        else:
            monkeys[monkey.false_path].s_items.append(worry_level)
    monkey.s_items = []

def prob1():
    with open('d11_in.txt','r') as file:
        monkeys = []
        for monkey in file.read().split('\n\n'):
            new_monkey = Monkey()
            monkeys.append(new_monkey.create_monkey(monkey.strip())) 
        
        count = 20
        for _ in range(count):
            for monkey in monkeys:
                inspect(monkey, monkeys)
        
        inspections = []
        for m in monkeys:
            inspections.append(m.items_inspected)

        inspections.sort()
        print(inspections[-1] * inspections[-2])

def prob2(): 
    with open('d11_in.txt','r') as file:
        monkeys = []
        for monkey in file.read().split('\n\n'):
            new_monkey = Monkey()
            monkeys.append(new_monkey.create_monkey(monkey.strip())) 

        common_divisor = 1
        for m in monkeys:
            common_divisor = common_divisor * m.test_num
        
        count = 10000
        for _ in range(count):
            for monkey in monkeys:
                inspect(monkey, monkeys, common_divisor)
        
        inspections = []
        for m in monkeys:
            inspections.append(m.items_inspected)

        inspections.sort()
        print(inspections[-1] * inspections[-2])

prob1()
prob2()
            


