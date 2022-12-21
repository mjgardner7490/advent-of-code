from collections import deque

def prob1():
    with open('d20_in.txt','r') as file:
        init_list = []
        for line in file.readlines():
            init_list.append(int(line))
        
        d_list = init_list[:]
        i_list = list(range(len(init_list)))
        # print(i_list)
        # print(f'initial list: {init_list}')
        for index, number in enumerate(init_list):
            print(f'number:{number}')
            print(f'index:{index}')
            # i = d_list.index(number) 
            c_i = i_list[index]
            # print(f'c_i:{c_i}')
            if number < 0:
                for x in range(0, number, -1):
                    num_i = (c_i+x) % len(d_list)
                    num_swap_i = (c_i+x-1) % len(d_list)
                    
                    f_index = i_list.index((c_i-1+x) % len(d_list))
                    i_list[f_index] = ((i_list[f_index]+1) % len(d_list))
                    i_list[index] = ((i_list[index]-1) % len(d_list))

                    temp = d_list[num_swap_i]
                    d_list[num_swap_i] = d_list[num_i]
                    d_list[num_i] = temp
            else:
                for x in range(number):
                    num_i = (c_i+x) % len(d_list)
                    num_swap_i = (c_i+x+1) % len(d_list)
                    
                    f_index = i_list.index((c_i+1+x) % len(d_list))
                    i_list[f_index] = ((i_list[f_index]-1) % len(d_list))
                    i_list[index] = ((i_list[index]+1) % len(d_list))

                    temp = d_list[num_swap_i]
                    d_list[num_swap_i] = d_list[num_i]
                    d_list[num_i] = temp

        zero_i = d_list.index(0)
        first = d_list[(zero_i + 1000) % len(d_list)]
        second = d_list[(zero_i + 2000) % len(d_list)]
        third = d_list[(zero_i + 3000) % len(d_list)]
        print(first)
        print(second)
        print(third)
        print(sum([first, second, third]))

def prob2():
    with open('d20_in.txt','r') as file:
        init_list = []
        unique_zero = ()
        for index, line in enumerate(file.readlines()):
            number = int(line)*811589153
            init_list.append((number,index))
            if (number) == 0:
                unique_zero = (number, index)
        
        # print(init_list)
        d_list = init_list[:]
        # print(f'initial list: {init_list}')
        for _ in range(10):
            for number in init_list:
                curr_index = d_list.index(number)
                d_list.remove(number)
                new_index = (curr_index + number[0]) % len(d_list)
                d_list.insert(new_index, number) 
             

        zero_i = d_list.index(unique_zero)
        first = d_list[(zero_i + 1000) % len(d_list)][0]
        second = d_list[(zero_i + 2000) % len(d_list)][0]
        third = d_list[(zero_i + 3000) % len(d_list)][0]
        print(first)
        print(second)
        print(third)
        print(sum([first, second, third]))


# prob1()
prob2()
