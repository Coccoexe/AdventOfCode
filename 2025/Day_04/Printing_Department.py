#Part-1 
import os
from math import inf
from collections import deque

print("Advent of Code 2025 - Day 4")
print("Printing Department")
print("--- Part 1 ---")

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    data = [list(line.rstrip('\n')) for line in f]
X = len(data[0])
Y = len(data)

NEIGHBOURS = [(-1,-1),(0,-1),(1,-1),
              (-1, 0),       (1, 0),
              (-1, 1),(0, 1),(1, 1)]

table = [[0]*X for _ in range(Y)]                   # weights initialization

for y in range(Y):
    for x in range(X):
        if data[y][x] == '.':                       # empty space
            table[y][x] = inf
            continue

        for dx,dy in NEIGHBOURS:                    # add weights to neighbours
            nx, ny = x+dx, y+dy
            if 0 <= nx < X and 0 <= ny < Y:
                table[ny][nx] += 1
 
# removable paper rolls
r = set()
for y in range(Y):
    for x in range(X):
        if table[y][x] < 4:
            r.add((x,y))
print(len(r))

#Part-2 
print("--- Part 2 ---")

c = 0
queue = deque(r)
visited = set(r)
while queue:
    x, y = queue.popleft()

    if table[y][x] == inf:
        continue                                    # già rimosso da una iterazione precedente

    table[y][x] = inf                               # remove a paper roll
    c += 1

    for dx,dy in NEIGHBOURS:                        # decreas neighbours weights
        nx, ny = x+dx, y+dy
        if 0 <= nx < X and 0 <= ny < Y and table[ny][nx] != inf:
            table[ny][nx] -= 1
            if table[ny][nx] < 4 and (nx,ny) not in visited:    # update removable rolls
                visited.add((nx,ny))
                queue.append((nx,ny))
                       
print(c)