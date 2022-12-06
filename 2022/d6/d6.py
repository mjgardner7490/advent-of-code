def prob1():
    with open('d6_in.txt','r') as file:
        signal = file.readline()
        marker = []
        received = 0
        for index, char in enumerate(signal):
            if char not in marker:
                marker.append(char)
                if len(marker) == 4:
                    received = index + 1
                    break
            else:
                dup = marker.index(char)
                marker = marker[dup+1:] 
                marker.append(char)
        print(received)




def prob2():
    with open('d6_in.txt','r') as file:
        signal = file.readline()
        marker = []
        received = 0
        print(signal)
        for index, char in enumerate(signal):
            if char not in marker:
                marker.append(char)
                if len(marker) == 14:
                    received = index + 1
                    break
            else:
                dup = marker.index(char)
                marker = marker[dup+1:] 
                marker.append(char)
        print(received)

prob1()
prob2()
