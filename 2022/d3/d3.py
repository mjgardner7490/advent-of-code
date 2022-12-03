priority = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 
        'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def prob1():
    with open('d3_in.txt','r') as file:
        sum = 0
        for inventory in file:
            mid = len(inventory) >> 1
            set1 = set(inventory[:mid].strip())
            set2 = set(inventory[mid:].strip())
            match = set1 & set2
            sum += priority.index(match.pop()) + 1
        print(sum)
         
def prob2(): 
    with open('d3_in.txt','r') as file:
        inventories = file.readlines()
        sum = 0 
        for i in range(0, len(inventories), 3):
            pack1 = set(inventories[i].strip())
            pack2 = set(inventories[i+1].strip())
            pack3 = set(inventories[i+2].strip())
            match = pack1 & pack2 & pack3
            
            sum += priority.index(match.pop()) + 1
        print(sum)

prob1()
prob2()

