import os
import numpy as np

print("Advent of Code 2022 - Day 4")
print("Camp Cleanup")
print("--- Part 1 ---")

file = open(os.path.dirname(__file__) + "/input.txt", "r")

lines = [line.strip() for line in file.read().splitlines()]
pairs = [line.split(",") for line in lines]
file.close()

fully_contained = 0
for pair in pairs:
    first = pair[0].split("-")
    second = pair[1].split("-")
    start_difference = int(first[0]) - int(second[0])
    end_difference = int(first[1]) - int(second[1])
    
    # if the signs of the two differences are the different, then one of the ranges are fully contained in the other
    # also if one of the differences is 0, then the ranges are fully contained
    # 
    # 6-6,4-6 -> 2,0 it contains a 0 and in fact is fully contained
    #
    # 2-8,3-7 -> -1,1 signs are different, fully contained
    #
    # 2-4,6-8 -> -4,-4 the signs are the same, so it is not fully contained
    #
    if 0 not in [start_difference, end_difference]:
        if np.sign(start_difference) != np.sign(end_difference):
            fully_contained += 1
    else:
        fully_contained += 1

print("Fully contained pairs: " + str(fully_contained))
print()

print("--- Part 2 ---")

not_overlaped = 0
for pair in pairs:
    first = pair[0].split("-")
    second = pair[1].split("-")
    if int(first[1]) < int(second[0]) or int(second[1]) < int(first[0]):
        not_overlaped += 1

overlaped = len(pairs) - not_overlaped     
print("Overlaped pairs: " + str(overlaped))
print()
    

