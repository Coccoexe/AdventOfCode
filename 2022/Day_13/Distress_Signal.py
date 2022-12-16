import os
print("Advent of Code 2022 - Day 13")
print("Distress Signal")
print("--- Part 1 ---")

# FUNCTIONS ----------------------------------------------

def compare_pair(left,right,verbose=False):
    l,r = 0,0
    while l < len(left) and r < len(right):
        if verbose: print("Compare", left[l], "vs", right[r])
        
        if type(left[l]) == type(right[r]) and type(left[l]) == int:
            if left[l] < right[r]:
                if verbose: print("Left side is smaller, so inputs are in the right order")
                return True
            elif left[l] > right[r]:
                if verbose: print("Right side is smaller, so inputs are not in the right order")
                return False
        else:
            if type(left[l]) != type(right[r]):
                if type(left[l]) != list:
                    left[l] = [left[l]]
                else:
                    right[r] = [right[r]]
                    
            tmp = compare_pair(left[l], right[r])
            if tmp != None:
                return tmp
        
        l,r = l+1,r+1
        
    if l <= len(left) and r < len(right):
        if verbose: print("Left side ran out of items, so inputs are in the right order")
        return True
    elif l < len(left) and r <= len(right):
        if verbose: print("Right side ran out of items, so inputs are not in the right order")
        return False 

def compare(packet1,packet2):
    tmp = compare_pair(packet1,packet2)
    if tmp == True:
        return -1
    elif tmp == False:
        return 1
    else:
        return 0

# CONSTANTS ----------------------------------------------

verbose = False

# --------------------------------------------------------

file = open(os.path.dirname(__file__) + "/input.txt", "r")
lines = file.read().splitlines()
file.close()

pairs = []
for i in range(0, len(lines), 3):
    pairs.append([lines[i], lines[i+1]]) 

c = 1
sum = 0
for p in pairs:
    if verbose: print("== Pair " + str(c) + " ==")
    if verbose: print("Compare", p[0], "vs", p[1])
    if compare_pair(eval(p[0]), eval(p[1]),verbose):
        sum += c
    c += 1
print("Sum of indices of pairs in the right order:", sum)
print()
          
print("--- Part 2 ---")

from functools import cmp_to_key

# CONSTANTS ----------------------------------------------

to_append = [
    '[[2]]',
    '[[6]]'
]

# --------------------------------------------------------

to_append = [eval(item) for item in to_append]

packets = [item for item in to_append]
for p in pairs:
    packets.append(eval(p[0]))
    packets.append(eval(p[1]))
    
sorted_packets = sorted(packets,key=cmp_to_key(compare))
to_append_index = [i for i in range(len(sorted_packets)) if sorted_packets[i] in to_append]
result = (to_append_index[0]+1) * (to_append_index[1]+1)
print("Decoder key:", result)
print()