def prob1():
    with open('d4_in.txt','r') as file:
        count = 0
        for sections in file:
            section1, section2 = sections.strip().split(',') 
            min1, max1 = [int(i) for i in section1.split('-')] 
            min2, max2 = [int(i) for i in section2.split('-')] 
            if (max2 >= max1) and (min2 <= min1):
                count += 1
                continue
            if (max1 >= max2) and (min1 <= min2):
                count += 1
        
        print(count)

def prob2():
    with open('d4_in.txt','r') as file:
        count = 0
        for sections in file:
            section1, section2 = sections.strip().split(',') 
            min1, max1 = [int(i) for i in section1.split('-')] 
            min2, max2 = [int(i) for i in section2.split('-')] 
            nums2 = {}
            for i in range(min1, max1+1):
                nums2[i] = True 
            for i in range(min2, max2+1):
                if nums2.get(i):
                    count += 1
                    break
        print(count)

prob1()
prob2()
