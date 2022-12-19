#Part-1 
import os
print("Advent of Code 2022 - Day 18")
print("Boiling Boulders")
print("--- Part 1 ---")

# FUNCTIONS ----------------------------------------------

def calculate_surface(points):
    surface = 0
    for x,y,z in points:
        surface += 6
        for dx,dy,dz in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
            if (x+dx,y+dy,z+dz) in points:
                surface -= 1
    return surface

# CONSTANTS ----------------------------------------------

mask = [
    (1,0,0),
    (-1,0,0),
    (0,1,0),
    (0,-1,0),
    (0,0,1),
    (0,0,-1)
]

# --------------------------------------------------------

#read file
file = open(os.path.dirname(__file__) + "\input.txt", "r")
obsidian = set([(int(line.split(',')[0]),int(line.split(',')[1]),int(line.split(',')[2])) for line in file.read().splitlines()])
file.close()

#find surface area
surface = calculate_surface(obsidian)
print("Surface area:", surface)
print()

#Part-2 
print("--- Part 2 ---")

#find bounds
max_x = max(obsidian, key=lambda x: x[0])[0]
max_y = max(obsidian, key=lambda x: x[1])[1]
max_z = max(obsidian, key=lambda x: x[2])[2]
max_coord = max(max_x, max_y, max_z)

#find air pockets
area = {(x,y,z) for x in range(max_coord+1) for y in range(max_coord+1) for z in range(max_coord+1)}
empty = list(area-obsidian)
air = []
while empty:
    to_visit = [empty[0]]
    current_air = set()
    
    while to_visit:
        next_air = to_visit.pop()
        if next_air in empty:
            empty.remove(next_air)
            current_air.add(next_air)
            x,y,z = next_air
            for dx,dy,dz in mask:
                to_visit.append((x+dx,y+dy,z+dz))
    if (0,0,0) not in current_air:
        air.append(current_air)

full = calculate_surface(obsidian)
air_pocket = [calculate_surface(x) for x in air]

print("Surface excluding air pockets:", full-sum(air_pocket))
print()