import os

print("Advent of Code 2022 - Day 3")
print("Rucksack Reorganization")
print("--- Part 1 ---")

# ord(item) return the ASCII value of the item
# 96 is the ASCII value of 'a' so we need to subtract 96 to get the priority
# 64 is the ASCII value of 'A' so we need to subtract 38 to get the priority
def find_priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

file = open(os.path.dirname(__file__) + "/input.txt", "r")
lines = [line.strip() for line in file.read().splitlines()]
file.close()

rucksacks = []
for line in lines:
    rucksacks.append([line[:len(line)//2], line[len(line)//2:]])

priority = 0
for rucksack in rucksacks:
    for item in rucksack[0]:
        if item in rucksack[1]:
            priority += find_priority(item)
            break #to avoid double counting
            
print("The sum of the priorities of the item types that appear in both compartments is", priority)
print()

print("--- Part 2 ---")

groups = []
for i in range(0, len(lines), 3):
    groups.append([lines[i], lines[i+1], lines[i+2]])

priority_group = 0
for group in groups:
    for item in group[0]:
        if item in group[1] and item in group[2]:
            priority_group += find_priority(item)
            break
        
print("The sum of the priorities of the item types that appear in all three rucksacks is", priority_group)
print()