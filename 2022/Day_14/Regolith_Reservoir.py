# --- Day 14: Regolith Reservoir ---
# The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like it's coming from the waterfall itself, and that doesn't make any sense. However, you do notice a little path that leads behind the waterfall.
# 
# Correction: the distress signal leads you behind a giant waterfall! There seems to be a large cave system here, and the signal definitely leads further inside.
# 
# As you begin to make your way deeper underground, you feel the ground rumble for a moment. Sand begins pouring into the cave! If you don't quickly figure out where the sand is going, you could quickly become trapped!
# 
# Fortunately, your familiarity with analyzing the path of falling material will come in handy here. You scan a two-dimensional vertical slice of the cave above you (your puzzle input) and discover that it is mostly air with structures made of rock.
# 
# Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape of the path, where x represents distance to the right and y represents distance down. Each path appears as a single line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. For example:
# 
# 498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9
# This scan means that there are two paths of rock; the first path consists of two straight lines, and the second path consists of three straight lines. (Specifically, the first path consists of a line of rock from 498,4 through 498,6 and another line of rock from 498,6 through 496,6.)
# 
# The sand is pouring into the cave from point 500,0.
# 
# Drawing rock as #, air as ., and the source of the sand as +, this becomes:
# 
# 
#   4     5  5
#   9     0  0
#   4     0  3
# 0 ......+...
# 1 ..........
# 2 ..........
# 3 ..........
# 4 ....#...##
# 5 ....#...#.
# 6 ..###...#.
# 7 ........#.
# 8 ........#.
# 9 #########.
# Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes to rest. A unit of sand is large enough to fill one tile of air in your scan.
# 
# A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source.
# 
# So, drawing sand that has come to rest as o, the first unit of sand simply falls straight down and then stops:
# 
# ......+...
# ..........
# ..........
# ..........
# ....#...##
# ....#...#.
# ..###...#.
# ........#.
# ......o.#.
# #########.
# The second unit of sand then falls straight down, lands on the first one, and then comes to rest to its left:
# 
# ......+...
# ..........
# ..........
# ..........
# ....#...##
# ....#...#.
# ..###...#.
# ........#.
# .....oo.#.
# #########.
# After a total of five units of sand have come to rest, they form this pattern:
# 
# ......+...
# ..........
# ..........
# ..........
# ....#...##
# ....#...#.
# ..###...#.
# ......o.#.
# ....oooo#.
# #########.
# After a total of 22 units of sand:
# 
# ......+...
# ..........
# ......o...
# .....ooo..
# ....#ooo##
# ....#ooo#.
# ..###ooo#.
# ....oooo#.
# ...ooooo#.
# #########.
# Finally, only two more units of sand can possibly come to rest:
# 
# ......+...
# ..........
# ......o...
# .....ooo..
# ....#ooo##
# ...o#ooo#.
# ..###ooo#.
# ....oooo#.
# .o.ooooo#.
# #########.
# Once all 24 units of sand shown above have come to rest, all further sand flows out the bottom, falling into the endless void. Just for fun, the path any new sand takes before falling forever is shown here with ~:
# 
# .......+...
# .......~...
# ......~o...
# .....~ooo..
# ....~#ooo##
# ...~o#ooo#.
# ..~###ooo#.
# ..~..oooo#.
# .~o.ooooo#.
# ~#########.
# ~..........
# ~..........
# ~..........
# Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?

import os
from functools import cmp_to_key

print("Advent of Code 2022 - Day 14")
print("Regolith Reservoir")
print("--- Part 1 ---")

#constants
height = 300
width = 1000 # must be at least double the height from the source
source = [500,0]

#functions
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
    
#read file
file = open(os.path.dirname(__file__) + "/input.txt", "r")
lines = [line.split(" -> ") for line in file.read().splitlines()]

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

print(poured)
print("")

    
#write file to output.txt                
out = open(os.path.dirname(__file__) + "/output_1.txt", "w")
map = print_map(matrix,False)
for row in map:
    out.write(row + "\n")

# --- Part Two ---
# You realize you misread the scan. There isn't an endless void at the bottom of the scan - there's floor, and you're standing on it!
# 
# You don't have time to scan the floor, so assume the floor is an infinite horizontal line with a y coordinate equal to two plus the highest y coordinate of any point in your scan.
# 
# In the example above, the highest y coordinate of any point is 9, and so the floor is at y=11. (This is as if your scan contained one extra rock path like -infinity,11 -> infinity,11.) With the added floor, the example above now looks like this:
# 
#         ...........+........
#         ....................
#         ....................
#         ....................
#         .........#...##.....
#         .........#...#......
#         .......###...#......
#         .............#......
#         .............#......
#         .....#########......
#         ....................
# <-- etc #################### etc -->
# To find somewhere safe to stand, you'll need to simulate falling sand until a unit of sand comes to rest at 500,0, blocking the source entirely and stopping the flow of sand into the cave. In the example above, the situation finally looks like this after 93 units of sand come to rest:
# 
# ............o............
# ...........ooo...........
# ..........ooooo..........
# .........ooooooo.........
# ........oo#ooo##o........
# .......ooo#ooo#ooo.......
# ......oo###ooo#oooo......
# .....oooo.oooo#ooooo.....
# ....oooooooooo#oooooo....
# ...ooo#########ooooooo...
# ..ooooo.......ooooooooo..
# #########################
# Using your scan, simulate the falling sand until the source of the sand becomes blocked. How many units of sand come to rest?

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
    
print(poured)

    
#write file to output.txt                
out = open(os.path.dirname(__file__) + "/output_2.txt", "w")
map = print_map(matrix,False)
for row in map:
    out.write(row + "\n")

