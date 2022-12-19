#Part-1 
import os, sys

# DEBUG --------------------------------------------------

DEBUG = True
if DEBUG:
    sys.tracebacklimit = 0

# --------------------------------------------------------

print("Advent of Code 2022 - Day 17")
print("Pyroclastic Flow")
print("--- Part 1 ---")

# FUNCTIONS ----------------------------------------------

def print_cave(to_terminal = False):
    display = []
    for i in range(len(matrix)-1,-1,-1):
        display.append('|'+"".join(matrix[i])+'|')
    display.append('+' + '-' * width + '+')
    
    if to_terminal:
        print("\n".join(display))
    else:
        return display

def move_rock_flow(direction, top, bottom):
    if direction == '<':
        move = True
        
        #check if there is space to move
        for y in range(bottom, top+1):
            for x in range(width-1):
                if matrix[y][x] == '#' and matrix[y][x+1] == '@':
                    move = False
                if x == 0 and matrix[y][x] == '@':
                    move = False
                
        #otherwise move
        if move:
            for y in range(bottom, top+1):
                for x in range(width-1):
                    if matrix[y][x+1] == '@':
                        matrix[y][x+1] = '.'
                        matrix[y][x] = '@'
                        
    elif direction == '>':
        move = True
        
        #check if there is space to move
        for y in range(bottom, top+1):
            for x in range(width-1):
                if matrix[y][x] == '@' and matrix[y][x+1] == '#':
                    move = False
                if x == width-2 and matrix[y][x+1] == '@':
                    move = False
        
        #otherwise move
        if move:
            for y in range(bottom, top+1):
                for x in range(width-1,0,-1):
                    if matrix[y][x-1] == '@':
                        matrix[y][x-1] = '.'
                        matrix[y][x] = '@'

def move_rock_fall(top, bottom):
    
    #check if there is space to fall
    if bottom == 0:
        return False
    
    for y in range(bottom, top+1):
        for x in range(width):
            if matrix[y][x] == '@' and matrix[y-1][x] == '#':
                return False
    
    #otherwise fall
    for y in range(bottom, top+1):
        for x in range(width):
            if matrix[y][x] == '@':
                matrix[y][x] = '.'
                matrix[y-1][x] = '@'    
    
    return True

def process_falling(rock):
    global flow_index
    
    #for the first rock
    top_most = -1
    
    #find top-most rock piece
    for i in range(len(matrix)-1,-1,-1):
        if "#" in matrix[i]:
            top_most = i
            break

    #be sure that there is enough space to add rock (3 lines)
    while top_most != len(matrix)-4:
        if top_most > len(matrix)-4:
            matrix[len(matrix)] = ['.'] * width
        else:
            del matrix[len(matrix)-1]        

    #index for place rocks on center of the line
    left_empty = 2
    right_empty = width - len(rock[0]) - left_empty
    
    #add rock on top of the cave
    len_m = len(matrix)
    for i in range(len(rock)-1,-1,-1):
        tmp = ['.' for _ in range(left_empty)]
        tmp.extend(rock[i].replace("#","@"))
        tmp.extend(['.' for _ in range(right_empty)])
        matrix[len_m + (len(rock)-1-i)] = tmp
    
    top_rock, bottom_rock = len(matrix)-1, len(matrix)-1-(len(rock)-1)

    #move rock until it stops
    while True:
        #move rock left or right
        move_rock_flow(flow[flow_index], top_rock, bottom_rock)

        #update flow index
        flow_index = flow_index + 1 if flow_index < len(flow) - 1 else 0
        
        #let rock fall
        if move_rock_fall(top_rock, bottom_rock):
            top_rock, bottom_rock = top_rock-1, bottom_rock-1
            
        else:
            #if cant fall anymore, change rock from @ to #
            for y in range(bottom_rock, top_rock+1):
                for x in range(width):
                    if matrix[y][x] == '@':
                        matrix[y][x] = '#'
            break
        

# CONSTANTS ----------------------------------------------

width = 7
to_fall = 2022 #use 100000 for part 2

# --------------------------------------------------------

#read rocks from file
file = open(os.path.dirname(__file__) + "\\rocks.txt", "r")
lines = file.readlines()
file.close()

#create rocks dictionary
rocks = {}
count = 0
for line in lines:
    if line == "\n":
        count += 1
        continue
    if count not in rocks:
        rocks[count] = []
    rocks[count].append(line.strip())

#read flow from file
file = open(os.path.dirname(__file__) + "\input.txt", "r")
flow = file.read()
file.close()

#create map of cave
matrix = {i: ['.'] * width for i in range(3)}

flow_index, rocks_index = 0, 0

#process falling
for i in range(to_fall):
    #rock
    rock = rocks[rocks_index]
    rocks_index = rocks_index + 1 if rocks_index < len(rocks) - 1 else 0

    #process
    process_falling(rock)

#write cave to file
out = open(os.path.dirname(__file__) + "\output.txt", "w")
display = print_cave()
for l in display:
    out.write(l + "\n")
out.close()

for i in range(len(matrix)-1,-1,-1):
    if "#" in matrix[i]:
        top_most = i
        break

print("Rocks tower height: " + str(top_most+1))
print()

#Part-2 
print("--- Part 2 ---")

# FUNCTIONS ----------------------------------------------

def height():
    for i in range(len(matrix)-1,-1,-1):
        if "#" in matrix[i]:
            h = i
            break
    return h + 1

def find_pattern(start):
    line_1 = "".join(matrix[start])
    
    matches = []
    for y in range(start+1,(len(matrix)-1-start)//2):
        to_match = "".join(matrix[start+y])
        if line_1 == to_match:
            matches.append(y)

    for match in matches:
        pattern = True
        for y in range(1, match):
            line_y = "".join(matrix[start+y])
            to_match_y = "".join(matrix[match+y])
            if line_y != to_match_y:
                pattern = False
                break
        if pattern:
            return match
    
    return -1

def matrix_to_string(index_from, index_to):
    str = ""
    for y in range(index_from, index_to+1):
        str += "".join(matrix[y])
    return str

# CONSTANTS ----------------------------------------------

to_fall_2 = 1000000000000

# --------------------------------------------------------

#try to find the pattern
#start from line 0, find first match
#if line 1 have a match in the line next to the first match, then continue
#if the match system continue until the line-1 of the first match, then we have a pattern
       
start,match = 0,-1
while start < len(matrix)//2:
    n_match = find_pattern(start)
    start += 1
    if n_match != -1:
        match = n_match
        break


#pattern string     
pattern = matrix_to_string(start, match)

#create map of cave
matrix = {i: ['.'] * width for i in range(3)}

flow_index, rocks_index = 0, 0

try:

    heigths = {}
    #process until first pattern is fallen
    rocks_fallen, rocks_before_pattern = 0, 0 
    while True:
        #rock
        rock = rocks[rocks_index]
        rocks_index = rocks_index + 1 if rocks_index < len(rocks) - 1 else 0

        #process
        process_falling(rock)
        
        rocks_fallen += 1
        
        heigths[rocks_fallen] = height()
        
        if len(matrix) > start-1 and matrix_to_string(start-1, start-1) == pattern[-width:]:
            if rocks_before_pattern == 0:
                rocks_before_pattern = rocks_fallen
        
        if len(matrix) > match and matrix_to_string(match, match) == pattern[-width:]:
            rocks_pattern = rocks_fallen - rocks_before_pattern
            break

except:
    print("+-----------------------------------------ERROR----------------------------------------+")
    print("| Be sure that first part calculate enough rocks to allow a pattern to exist           |")
    print("| If this error persist, try to increase the number of rocks to fall in the first part |")
    print("+--------------------------------------------------------------------------------------+")
    

# calculate useful values
pattern_heigth = heigths[rocks_fallen]-heigths[rocks_before_pattern]
before_pattern_heigth = heigths[rocks_before_pattern]
pattern_fallen = (to_fall_2-rocks_before_pattern)//rocks_pattern
remaining_rocks = (to_fall_2-rocks_before_pattern)%rocks_pattern
remaining_rocks_heigth = heigths[rocks_before_pattern+remaining_rocks]-heigths[rocks_before_pattern]

# calculate total height
total_heigth = before_pattern_heigth + pattern_heigth*pattern_fallen + remaining_rocks_heigth
print("Rocks tower height: " + str(total_heigth))
    








