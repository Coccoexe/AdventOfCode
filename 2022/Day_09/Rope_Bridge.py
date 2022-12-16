import os
print("Advent of Code 2022 - Day 9")
print("Rope Bridge")
print("--- Part 1 ---")

# FUNCTIONS ----------------------------------------------
def move_head(movement,position_H):
    if movement == "R":
        position_H[0] += 1
    elif movement == "L":
        position_H[0] -= 1
    elif movement == "U":
        position_H[1] += 1
    elif movement == "D":
        position_H[1] -= 1
    
def move_tail(position_H,position_T):
    
    if (position_H[0] - position_T[0])**2 + (position_H[1] - position_T[1])**2 > 2:
        if position_H[0] > position_T[0]:
            position_T[0] += 1
        elif position_H[0] < position_T[0]:
            position_T[0] -= 1
        if position_H[1] > position_T[1]:
            position_T[1] += 1
        elif position_H[1] < position_T[1]:
            position_T[1] -= 1
    return position_T

def print_positions(positions,prints=None):
    for j in range(15,-15,-1):
        line = ''
        for i in range(-15,15):
            if [i,j] in positions:
                line += str(positions.index([i,j])) if prints is None else prints
            elif [i,j] == [0,0]:
                line += 's'
            else:
                line += '.'
        print(line)
        
# CONSTANTS ----------------------------------------------

position_H = [0,0]
position_T = [0,0]

# --------------------------------------------------------

file = open(os.path.dirname(__file__) + "/input.txt", "r")
lines = [[line.split(" ")[0],int(line.split(" ")[1])] for line in file.read().splitlines()]
file.close()

movements = [[position_T[0],position_T[1]]]
for line in lines:
    for i in range(line[1]):
        move_head(line[0],position_H)
        tmp = move_tail(position_H,position_T)
        if [tmp[0],tmp[1]] not in movements:
            movements.append([tmp[0],tmp[1]])
            
print("The tail of the rope visited",len(movements),"positions at least once.")
print()

print("--- Part 2 ---")

# CONSTANTS ----------------------------------------------

number_of_knots = 10

# --------------------------------------------------------

positions = [[0,0] for i in range(number_of_knots)]
movements = [[] for i in range(number_of_knots)]
    
for line in lines:
    for i in range(line[1]):
        move_head(line[0],positions[0])
        for j in range(1,number_of_knots):
            tmp = move_tail(positions[j-1],positions[j])
            if [tmp[0],tmp[1]] not in movements[j]:
                movements[j].append([tmp[0],tmp[1]])

len_mov = len(movements[number_of_knots-1])
print("The tail visits {} positions at least once.".format(len_mov))
print()