
import os
from functools import cmp_to_key

print("Advent of Code 2022 - Day 14")
print("Regolith Reservoir")
print("--- Part 1 ---")

# FUNCTIONS --------------------------------------------

def print_map(matrix,display=True):
    global height
    count = '000'
    rows = [' '*len(str(height)) for i in range(3)]
    for x in range(len(matrix[0])):
        rows[0] += count[0]
        rows[1] += count[1]
        rows[2] += count[2]
        count = str(int(count) + 1)
        while len(count) < 3: count = "0" + count
    
    for y in range(len(matrix)):
        i = 3 - len(str(y))
        row = ' '*i + str(y)
        for x in range(len(matrix[y])):
            row += matrix[y][x]
        rows.append(row)
        
    if display:
        for row in rows:
            print(row)
    else:
        return rows

def pour_sand(matrix,source,depth,width):
    walls = ['~','#','o'] 
    current = [source[0],source[1]]

    while current[0] < width and current[1] < depth and current[0] >= 0 and current[1] >= 0:
        #check if sand can fall
        if matrix[current[1]+1][current[0]] not in walls:
            current[1] += 1
        
        #check if sand can fall left
        elif matrix[current[1]+1][current[0]-1] not in walls:
            current[0] -= 1
            current[1] += 1 
        
        #check if sand can fall right
        elif matrix[current[1]+1][current[0]+1] not in walls:
            current[0] += 1
            current[1] += 1
        
        #sand can't fall
        else:
            matrix[current[1]][current[0]] = 'o'
            return True
    return False

#pour from source
def pour_sand_from_source(matrix,source):
    walls = ['#','o'] 
    current = [source[0],source[1]]

    if matrix[current[1]][current[0]] == 'o':
        return False
    
    while True:
        if matrix[current[1]+1][current[0]] not in walls:
            current[1] += 1
        elif matrix[current[1]+1][current[0]-1] not in walls:
            current[0] -= 1
            current[1] += 1
        elif matrix[current[1]+1][current[0]+1] not in walls:
            current[0] += 1
            current[1] += 1
        else:
            matrix[current[1]][current[0]] = 'o'
            return True
        
# CONSTANTS --------------------------------------------

height = 300
width = 1000 # must be at least double the height from the source
source = [500,0]

# ------------------------------------------------------

#read file
file = open(os.path.dirname(__file__) + "/input.txt", "r")
lines = [line.split(" -> ") for line in file.read().splitlines()]
file.close()

#parse input
for i in range(len(lines)):
    tmp = []
    for wall in lines[i]:
        x,y = wall.split(",")[0], wall.split(",")[1]
        tmp.append([x,y])
    lines[i] = tmp

#create matrix  
matrix = [['.' for x in range(width)] for y in range(height)]

#add walls
for line in lines:
    for i in range(len(line)-1):
        start,end = line[i], line[i+1]
        dx,dy = int(end[0]) - int(start[0]), int(end[1]) - int(start[1])
        matrix[int(start[1])+dy][int(start[0])+dx] = '#'
        while dx != 0 or dy != 0:
            if dx > 0: dx -= 1
            elif dx < 0: dx += 1
            if dy > 0: dy -= 1
            elif dy < 0: dy += 1
            matrix[int(start[1])+dy][int(start[0])+dx] = '#'

#bottom-most wall
for i in range(len(matrix)-1,-1,-1):
    if "#" in matrix[i]:
        last_wall = i
        break

#right-most wall
for i in range(len(matrix[0])-1,-1,-1):
    if "#" in [matrix[j][i] for j in range(len(matrix))]:
        right_wall = i
        break

#add source of sand
matrix[source[1]][source[0]] = '+'
 
#pour sand
poured = 0
while True:
    if pour_sand(matrix,source,last_wall,right_wall):
        poured += 1
    else:
        break

print("Sand poured:", poured)
print()

#write file to output.txt                
out = open(os.path.dirname(__file__) + "/output_1.txt", "w")
map = print_map(matrix,False)
for row in map:
    out.write(row + "\n")

print("--- Part 2 ---")

#add floor
for i in range(len(matrix[0])):
    matrix[last_wall+2][i] = '#'

#pour sand
while True:
    if pour_sand(matrix,source,last_wall+2,right_wall):
        poured += 1
    else:
        break

while True:
    if pour_sand_from_source(matrix,source):
        poured += 1
    else:
        break   
    
print("Sand poured until source is blocked:", poured)
print()

#write file to output.txt                
out = open(os.path.dirname(__file__) + "/output_2.txt", "w")
map = print_map(matrix,False)
for row in map:
    out.write(row + "\n")

