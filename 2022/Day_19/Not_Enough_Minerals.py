#Part-1 
import os, re
print("Advent of Code 2022 - Day 19")
print("Not Enough Minerals")
print("--- Part 1 ---")

# FUNCTIONS ----------------------------------------------

# CONSTANTS ----------------------------------------------

minutes = 24

# --------------------------------------------------------

#read file
file = open(os.path.dirname(__file__) + "\input.txt", "r")
lines = file.read().splitlines()
file.close()

#parse input
blueprints = {} #blueprints = {id: [ore, clay, obsidian_1, obsidian_2, geode_1, geode_2]}
for line in lines:
    regex = re.findall(r"\d+", line)
    blueprints[regex[0]] = [regex[1], regex[2], regex[3], regex[4], regex[5], regex[6]]

for b in blueprints:
    for m in range(minutes):
        #process blueprints to discover quality level
        break
    
#choose the best quality level

#Part-2 
print("--- Part 2 ---")
