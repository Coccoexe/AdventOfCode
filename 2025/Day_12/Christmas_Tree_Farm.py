#Part-1 
import os, re
print("Advent of Code 2025 - Day 12")
print("Christmas Tree Farm")
print("--- Part 1 ---")


data = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r').read().split('\n\n')

# Fortunally for this puzzle is enough to check if the requested presents would fit in the total available area
# This is not the proper solution but is the best i can get, not feasible to check every placement :)

presents = [sum(c == '#' for c in block) for block in data[:6]]
total = 0   
for region in data[6].split('\n'):
    area   = eval(region.split(':')[0].replace('x','*'))
    area_p = (sum( r*p for r,p in zip(map(int, region.split(':')[1].split()), presents) ))
    total += area > area_p
print(total)

#Part-2 
print("--- Part 2 ---")

print("Happy Chriymn, Merry Chrysler")
