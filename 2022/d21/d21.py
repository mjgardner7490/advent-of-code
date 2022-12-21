def prob1(): 
    with open('d21_in.txt','r') as file:
        m_dep_map = {}
        m_num_map = {}
        m_op_map = {}
        for line in file.readlines():
            words = line.strip().split()
            if words[1].isdigit():
                m_num_map[words[0].strip(':')] = int(words[1])
            else:
                m_dep_map[words[0].strip(':')] = [words[1], words[3]]
                m_op_map[words[0].strip(':')] = words[2]

        depRemains = True
        while depRemains:
            for m, dep in m_dep_map.items():
                if (dep[0] in m_num_map.keys()) and (dep[1] in m_num_map.keys()):
                    if m_op_map[m] == "+":
                        m_num_map[m] = m_num_map[dep[0]] + m_num_map[dep[1]] 
                    if m_op_map[m] == "-":
                        m_num_map[m] = m_num_map[dep[0]] - m_num_map[dep[1]] 
                    if m_op_map[m] == "*":
                        m_num_map[m] = m_num_map[dep[0]] * m_num_map[dep[1]] 
                    if m_op_map[m] == "/":
                        m_num_map[m] = m_num_map[dep[0]] / m_num_map[dep[1]] 
            if "root" in m_num_map.keys():
                depRemains = False
        
        print(m_num_map["root"])

def prob2():
    with open('d21_in.txt','r') as file:
        m_dep_map = {}
        m_num_map = {}
        m_op_map = {}
        for line in file.readlines():
            words = line.strip().split()
            if words[1].isdigit():
                m_num_map[words[0].strip(':')] = int(words[1])
            else:
                m_dep_map[words[0].strip(':')] = [words[1], words[3]]
                m_op_map[words[0].strip(':')] = words[2]

        # I feel shame...
        m_num_map["humn"] = 3243420789721 
        depRemains = True
        while depRemains:
            for m, dep in m_dep_map.items():
                if (dep[0] in m_num_map.keys()) and (dep[1] in m_num_map.keys()):
                    if m_op_map[m] == "+":
                        m_num_map[m] = m_num_map[dep[0]] + m_num_map[dep[1]] 
                    if m_op_map[m] == "-":
                        m_num_map[m] = m_num_map[dep[0]] - m_num_map[dep[1]] 
                    if m_op_map[m] == "*":
                        m_num_map[m] = m_num_map[dep[0]] * m_num_map[dep[1]] 
                    if m_op_map[m] == "/":
                        m_num_map[m] = m_num_map[dep[0]] / m_num_map[dep[1]] 
            if "root" in m_num_map.keys():
                depRemains = False
        
        print(f'trying to match: {m_num_map["hppd"]}')
        print(f'num to match:    {m_num_map["czdp"]}')


prob1()
prob2()
            


