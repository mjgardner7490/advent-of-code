class Directory(object):
    def __init__(self, data, parent=None):
        self.data = data
        self.file_size = 0
        self.size = 0
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

def calc_dir_size(tree, small_files):
    if tree.size != 0:
        return tree.size

    if tree.is_leaf():
        tree.size = tree.file_size
        if tree.size <= 100000:
            small_files.append(tree.size)
        return tree.size
    else:
        size = 0
        for child in tree.children:
            size += calc_dir_size(child, small_files)
        
        tree.size = tree.file_size + size
        if tree.size <= 100000:
            small_files.append(tree.size)
        return tree.size
    

def prob1():
    with open('d7_in.txt','r') as file:
        file.readline()
        tree = Directory("/")
        for command in file:
            options = command.split() 
            if options[0] == '$' and options[1] == 'cd':
                if options[2] == '..':
                    tree = tree.parent
                else:
                    for t in tree.children:
                        if t.data == options[2]:
                            tree = t
            if options[0] == 'dir':
                tree.add_child(options[1])
            if options[0].isdigit():
                tree.file_size += int(options[0])

        while not tree.is_root():
            tree = tree.parent
        
        small_files = []
        root_size = calc_dir_size(tree, small_files)
        
        print(sum(small_files)) 

def find_free_space(tree, free, needed):
    if tree.size >= needed:
        free.append(tree.size)
    
    if not tree.is_leaf():
        for child in tree.children:
            find_free_space(child, free, needed)

def prob2():
    with open('d7_in.txt','r') as file:
        file.readline()
        tree = Directory("/")
        for command in file:
            options = command.split() 
            if options[0] == '$' and options[1] == 'cd':
                if options[2] == '..':
                    tree = tree.parent
                else:
                    for t in tree.children:
                        if t.data == options[2]:
                            tree = t
            if options[0] == 'dir':
                tree.add_child(options[1])
            if options[0].isdigit():
                tree.file_size += int(options[0])

        while not tree.is_root():
            tree = tree.parent
        
        root_size = calc_dir_size(tree, [])
        
        avail = 70000000 - root_size
        needed = 30000000 - avail

        free = []
        free.append(root_size)
        
        find_free_space(tree, free, needed)
        
        free.sort()
        print(free[0])
         
prob1()
prob2()
