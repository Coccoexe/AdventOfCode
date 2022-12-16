#Part-1 
import os,re
print("Advent of Code 2022 - Day 15")
print("Beacon Exclusion Zone")
print("--- Part 1 ---")

#functions

def sensors_to_compute(line):
    global sensors, beacons
    s,b = [],[]
    for i in range(len(sensors)):
        s_x, s_y = sensors[i][0], sensors[i][1]
        b_x, b_y = beacons[i][0], beacons[i][1]
        distance = abs(s_x - b_x) + abs(s_y - b_y)
        if s_y-distance <= line and s_y+distance >= line:
            s.append(sensors[i])
            b.append(beacons[i])  
    return s,b

def deat_zone_range(sensor,beacon,line):
    death_zone = None
    to_remove = None

    #coordinates of sensor and beacon
    s_x, s_y = sensor[0], sensor[1]
    b_x, b_y = beacon[0], beacon[1]

    #find distance
    distance = abs(s_x - b_x) + abs(s_y - b_y)

    if b_y == line:
        to_remove = b_x
    if s_y == line:
        to_remove = s_x
    death_zone = [s_x - (distance - abs(line-s_y)), s_x + (distance - abs(line-s_y))]

    return death_zone, to_remove

def mergeIntervals(intervals):
    # Sort the array on the basis of start values of intervals.
    intervals.sort()
    stack = []
    # insert first interval into stack
    stack.append(intervals[0])
    for i in intervals[1:]:
        # Check for overlapping interval,
        # if interval overlap
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
 
    return stack

def merge(intervals):
    intervals.sort()
    merged = []
    for interval in intervals:
        if not merged or merged[-1][-1] + 1 < interval[0]:
            merged.append(interval)
        else:
            merged[-1][-1] = max(merged[-1][-1], interval[-1])
    
    return merged

file = open(os.path.dirname(__file__) + "\input.txt", "r")
lines = file.readlines()

#Parse input
sensors, beacons = [], []
for line in lines:
    regex = re.findall(r"-*\d+",line)
    sensors.append([int(regex[0]),int(regex[1])])
    beacons.append([int(regex[2]),int(regex[3])])

#find sensors to compute
line_index = 10
s,b = sensors_to_compute(line_index)   

#compute death zone
death_zone = []
to_remove = []
for i in range(len(s)):
    tmp = deat_zone_range(s[i],b[i],line_index)
    if tmp[0] not in death_zone and tmp[0] != None:
        death_zone.append(tmp[0])
    if tmp[1] not in to_remove and tmp[1] != None:
        to_remove.append(tmp[1])


#merge intervals
death_zone = merge(death_zone)

#count death zones
count = 0
for interval in death_zone:
    count += interval[1] - interval[0] + 1
    for item in to_remove:
        if item >= interval[0] and item <= interval[1]:
            count -= 1
            to_remove.remove(item)
print(count)
print("")

# --- Part Two ---
# Your handheld device indicates that the distress signal is coming from a beacon nearby. The distress beacon is not detected by any sensor, but the distress beacon must have x and y coordinates each no lower than 0 and no larger than 4000000.
# 
# To isolate the distress beacon's signal, you need to determine its tuning frequency, which can be found by multiplying its x coordinate by 4000000 and then adding its y coordinate.
# 
# In the example above, the search space is smaller: instead, the x and y coordinates can each be at most 20. With this reduced search area, there is only a single position that could have a beacon: x=14, y=11. The tuning frequency for this distress beacon is 56000011.
# 
# Find the only possible position for the distress beacon. What is its tuning frequency?

print("--- Part 2 ---")

min_coord, max_coord = 0, 4000000

spot = []

for i in range(min_coord,max_coord+1):
    print(i)
    s,b = sensors_to_compute(i)   

    #compute death zone
    death_zone = []
    to_remove = []
    for j in range(len(s)):
        tmp = deat_zone_range(s[j],b[j],i)
        interval = [min(tmp[0]),max(tmp[0])] if tmp != None else None
        if interval not in death_zone and interval != None:
            death_zone.append(interval)
        if tmp[1] not in to_remove and tmp[1] != None:
            to_remove.append(tmp[1])


    #merge intervals
    death_zone = merge(death_zone)

    for interval in death_zone:
        if interval[1] < min_coord or interval[0] > max_coord:
            print("remove",interval)
            death_zone.remove(interval)
    
    if len(death_zone) > 1:
        for j in range(len(death_zone)-1):
            for k in range(death_zone[j][1]+1,death_zone[j+1][0]):
                spot.append([i,k])

print(spot)


    