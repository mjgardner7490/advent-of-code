class Directory(object):
    def __init__(self, data, parent=None):
        self.data = data
        self.size = 0
        self.actual_size = 0
        self.children = []
        self.parent = parent

    def add_child(self, data):
        new_child = Directory(data, parent=self)
        self.children.append(new_child)
        return new_child

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.children

def calc_stuff(tree, smalls):
    if tree.actual_size != 0:
        return tree.actual_size

    if tree.is_leaf():
        tree.actual_size = tree.size
        if tree.actual_size <= 100000:
            smalls.append(tree.actual_size)
        return tree.actual_size
    else:
        size = 0
        for child in tree.children:
            size += calc_stuff(child, smalls)
        
        tree.actual_size = tree.size + size
        if tree.actual_size <= 100000:
            smalls.append(tree.actual_size)
        return tree.actual_size
    

def prob1():
    with open('d7_in.txt','r') as file:
        tree = Directory("/")
        file.readline()
        for command in file:
            options = command.split() 
            if options[0] == '$' and options[1] == 'cd':
                if options[2] != '..':
                    for t in tree.children:
                        if t.data == options[2]:
                            tree = t
                else:
                    tree = tree.parent
            if options[0] == 'dir':
                tree.add_child(options[1])
            if options[0].isdigit():
                tree.size += int(options[0])

        while !tree.is_root():
            tree = tree.parent
        
        smalls = []
        root_size = calc_stuff(tree, smalls)
        
        print(sum(smalls)) 

def calc_stuff2(tree, free, needed):
    if tree.actual_size >= needed:
        free.append(tree.actual_size)
    
    if len(tree.children) >= 0:
        for child in tree.children:
            calc_stuff2(child, free, needed)

def prob2():
    with open('d7_in.txt','r') as file:
        tree = Directory("/")
        file.readline()
        for command in file:
            options = command.split() 
            if options[0] == '$' and options[1] == 'cd':
                if options[2] != '..':
                    for t in tree.children:
                        if t.data == options[2]:
                            tree = t
                else:
                    tree = tree.parent
            if options[0] == 'dir':
                tree.add_child(options[1])
            if options[0].isdigit():
                tree.size += int(options[0])

        while tree.parent != None:
            tree = tree.parent
        
        smalls = []
        root_size = calc_stuff(tree, smalls)
        
        avail = 70000000 - root_size
        needed = 30000000 - avail

        free = []
        free.append(root_size)
        
        calc_stuff2(tree, free, needed)
        
        free.sort()
        print(free[0])
         
prob1()
prob2()
