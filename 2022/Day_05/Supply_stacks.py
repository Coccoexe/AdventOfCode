import os
print("Advent of Code 2022 - Day 5")
print("Supply Stacks")
print("--- Part 1 ---")

file = open(os.path.dirname(__file__) + "/input.txt", "r")
lines = file.readlines()
file.close()

first_part = []
second_part = []

#divide first and second part of input file
i = 0
for i in range(len(lines)):
    if len(lines[i]) == 1:
        i += 1
        break
    first_part.append(lines[i])
for i in range(i, len(lines)):
    second_part.append(lines[i])
    
#rearrange first part for easier processing    
first_part = [[line[i:i+4] for i in range(0, len(line), 4)] for line in first_part]
first_part.pop()
first_part = list(reversed(first_part))

#finally create the stacks
stacks = [[] for i in range(len(first_part[0]))]

#add crates to stacks
for line in first_part:
    for i in range(len(line)):
        if line[i][1].isalpha():
            stacks[i].append(line[i][1])
            
#STACKS BACKUP FOR PART 2
import copy
stacks2 = copy.deepcopy(stacks)

#rearrange second part for easier processing  
second_part = [line.split() for line in second_part]
second_part = [[line[1], line[3], line[5]] for line in second_part]

#define function to move crates
def move_crate(quantity,from_stack,to_stack):
    for i in range(quantity):
        stacks[to_stack].append(stacks[from_stack].pop())

#move crates
for instruction in second_part:
    move_crate(int(instruction[0]),int(instruction[1])-1,int(instruction[2])-1)

#display result
message = ""
message = message.join([stacks[i][-1] for i in range(len(stacks))])
print("The message is: " + message)
print()
        
print("--- Part 2 ---")

#define new function to move crates
def move_crate2(quantity,from_stack,to_stack):
    tmp = []
    for i in range(quantity):
        tmp.append(stacks2[from_stack].pop())
    tmp = list(reversed(tmp))
    stacks2[to_stack].extend(tmp)
    
#move crates
for instruction in second_part:
    move_crate2(int(instruction[0]),int(instruction[1])-1,int(instruction[2])-1)

#display result
message = ""
message = message.join([stacks2[i][-1] for i in range(len(stacks2))])
print("The message is: " + message)
print()