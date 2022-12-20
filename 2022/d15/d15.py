def prob1():
    with open('d15_in.txt', 'r') as file:  
        s_map = {}
        b_map = {}
        for index, line in enumerate(file.readlines()):
            data = line.strip().split() 
            s_x = data[2][2:-1] 
            s_y = data[3][2:-1]
            b_x = data[-2][2:-1]
            b_y = data[-1][2:]
            s_map[index] = (int(s_x), int(s_y))
            b_map[index] = (int(b_x), int(b_y))

        row = 2000000
        comp_list = []
        d_map = {}
        for key, s_coords in s_map.items():
            b_coords = b_map[key]
            d = abs(s_coords[0] - b_coords[0]) + abs(s_coords[1] - b_coords[1])
            if (s_coords[1] <= row <= s_coords[1] + d) or (s_coords[1] >= row >= s_coords[1] - d):
                comp_list.append(key) 
                d_map[key] = d

        # compute affect coords for row
        affected_coords = set()
        for index in comp_list:
            r_dist = abs(s_map[index][1] - row)
            range_x = d_map[index] - r_dist
            s_x = s_map[index][0]
            for x in range((s_x - range_x), (s_x + range_x + 1)):
                affected_coords.add((x,row))

        for coord in affected_coords.copy():
            if coord in b_map.values():
                affected_coords.remove(coord)
        
        print(len(affected_coords))

from collections import OrderedDict

def prob2():
    with open('d15_in.txt', 'r') as file:  
        s_map = {}
        b_map = {}
        for index, line in enumerate(file.readlines()):
            data = line.strip().split() 
            s_x = data[2][2:-1] 
            s_y = data[3][2:-1]
            b_x = data[-2][2:-1]
            b_y = data[-1][2:]
            s_map[index] = (int(s_x), int(s_y))
            b_map[index] = (int(b_x), int(b_y))

        # calculate distances from sensor to beacons
        d_map = {}
        for key, s_coords in s_map.items():
            b_coords = b_map[key]
            d = abs(s_coords[0] - b_coords[0]) + abs(s_coords[1] - b_coords[1])
            d_map[key] = d
        
        low_x = 0
        high_x = 4000000
        low_y = 0
        high_y = 4000000

        # map the covered ranges of coords for each row
        cov_map = {i:[] for i in range(4000001)}
        for key, sensor in s_map.items():
            x = sensor[0]
            y = sensor[1]
            d = d_map[key]
            row_range = 0
            for row_index in range(y-d, y+d+1):
                if row_index < low_y or row_index > high_y:
                    continue

                row_range = d - abs(y-row_index)
                x_s = x - row_range
                x_f = x + row_range

                if x_s > high_x or x_f < low_x:
                    continue
                if x_s < low_x:
                    x_s = low_x
                if x_f > high_x:
                    x_f = high_x
                cov_map[row_index].append((x_s,x_f))
        
        # Find the only uncovered coord by doing a union on the ranges for each row
        beacon_coords = ()
        for index, coord_ranges in cov_map.items():
            union_range = []
            for s, f in sorted(coord_ranges):
                if union_range and union_range[-1][1] >= s -1:
                    union_range[-1][1] = max(union_range[-1][1], f)
                else:
                    union_range.append([s,f])
            if len(union_range) > 1:
                beacon_x = (union_range[1][0]+union_range[0][1])//2
                beacon_coords = (beacon_x, index)

        print(beacon_coords)


prob1()
prob2()
