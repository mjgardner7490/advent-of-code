from pprint import pprint

# Has a bug somewhere....... so close
def parse(line):
    list_map = {}
    parsed_list = []
    opened_list = 0
    for char in line:
        if char == "[":
            opened_list += 1 
            list_map[opened_list] = []
        if char == "]":
            if opened_list > 1:
                list_map[opened_list-1].append(list_map.pop(opened_list))
                opened_list -= 1
            elif opened_list == 1:
                parsed_list.append(list_map.pop(opened_list))
                opened_list -= 1
        if char.isnumeric():
            if opened_list > 0:
               list_map[opened_list] = list_map.get(opened_list, [])
               list_map[opened_list].append(int(char))
            else:
                parsed_list.append(int(char))
    return parsed_list
 
def compare_pair(pair: []):
    pair1 = pair[0]
    pair2 = pair[1]
    print('==================')
    print(f'pair1:{pair1}')
    print(f'pair2:{pair2}')
    print()
    
    for i in range(len(pair1)):
        print(f'Pair Index: {i}')
        if i == len(pair2):
            print("Right side ran out of items")
            return False

        print(f'ele1: {pair1[i]}')
        print(f'ele2: {pair2[i]}')

        # [] , [ 1, []], [[]], [1 , 2]  ------->  [] , [ 1, []], [[]], [1 , 2]
        if isinstance(pair1[i], list) and isinstance(pair2[i], list):
            print("Both elements are lists")
            outcome = compare_pair([pair1[i], pair2[i]])
            if outcome != None:
                return outcome

        # [] , [ 1, []], [[]], [1 , 2]  ------->  [1]
        elif isinstance(pair1[i], list):
            print("Pair 1 = List, Pair 2 = Num") 
            outcome = compare_pair([pair1[i], [pair2[i]]])
            if outcome != None:
                return outcome

        # [1] ------->  [] , [ 1, []], [[]], [1 , 2] 
        elif isinstance(pair2[i], list):
            print("Pair 1 = Num, Pair 2 = List") 
            # Right ran out of items
            outcome = compare_pair([[pair1[i]], pair2[i]])
            if outcome != None:
                return outcome
        else:
            print("Both are Nums")
            if pair2[i] < pair1[i]:
                print("Right < Left: False")
                return False
            if pair2[i] > pair1[i]:
                print("Right > Left: True")
                return True
        print('==================')
        
    if len(pair1) < len(pair2):
        print("Right side ran out of items")
        return True
    if len(pair1) > len(pair2):
        print("Left side ran out of items")
        return False
    return None

def prob1(): 
    with open('d13_in.txt','r') as file:
        parsed_pairs = [] 
        for pairs in file.read().split('\n\n'):
            pairs = pairs.splitlines()
            parsed_pairs.append((eval(pairs[0]),eval(pairs[1])))

        correct_indicies = []
        for index, pairs in enumerate(parsed_pairs):
            if compare_pair(pairs):
                correct_indicies.append(index + 1)

        print(correct_indicies)
        print(sum(correct_indicies))

def prob2():
    with open('d13_in.txt','r') as file:
        parsed_packets = [] 
        for pairs in file.read().split('\n\n'):
            pairs = pairs.splitlines()
            parsed_packets.append(eval(pairs[0]))
            parsed_packets.append(eval(pairs[1]))
        parsed_packets.append([[2]])
        parsed_packets.append([[6]])

        swappin = True
        while swappin:
            count = 0
            for i in range(len(parsed_packets)-1): 
                if not compare_pair([parsed_packets[i], parsed_packets[i+1]]):
                    temp = parsed_packets[i]
                    parsed_packets[i] = parsed_packets[i + 1]
                    parsed_packets[i+1] = temp
                    count += 1
            if count == 0:
                swappin = False
            else:
                count = 0

        print((parsed_packets.index([[2]]) + 1) * (parsed_packets.index([[6]]) + 1))
            


prob1()
print('----')
prob2()
            

