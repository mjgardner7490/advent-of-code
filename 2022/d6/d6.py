def prob1():
    with open('d6_in.txt','r') as file:
        signal = file.readline().strip() 
        for i in range(len(signal)):
            marker = set(signal[i:i+4]) 
            if len(marker) == 4:
                print(i + 4)
                break

def prob2():
    with open('d6_in.txt','r') as file:
        signal = file.readline().strip() 
        for i in range(len(signal)):
            message = set(signal[i:i+14]) 
            if len(message) == 14:
                print(i + 14)
                break

prob1()
prob2()
