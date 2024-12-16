#Part-1 
import os
import time


print("Advent of Code 2024 - Day 6")
print("Guard Gallivant")
print("--- Part 1 ---")

data = open(os.path.join(os.path.dirname(__file__), "input.txt")).read().split("\n")
table = {}
for r,row in enumerate(data):
    for c, v in enumerate(row):
        table[(r,c)] = v
        if v == "^": start = (r,c)

seen = set()
seen.add(start)

queue = [(*start,-1,0)]
dr,dc = (-1,0)                                                  # initial direction
dt = {(-1,0):(0,1),(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0)}      # direction transformation

def path(p1=True):
    queue = [(*start,-1,0)]
    dr,dc = (-1,0)
    for r, c, dr, dc in queue:
        if (r,c,dr,dc) in seen: return _, 1
        if p1: seen.add((r,c))
        else: seen.add((r,c,dr,dc))
        nr, nc = r+dr, c+dc
        if (nr,nc) not in table: return seen, 0
        elif table[(nr,nc)] == "#":
            dr, dc = dt[(dr,dc)]
            queue.append((r,c,dr,dc))
        else:
            queue.append((nr,nc,dr,dc))

visited, _ = path()
print(len(visited))

#Part-2 
print("--- Part 2 ---")
counter = 0
for p in visited: 
    if table[p] in "^#": continue
    table[p] = "#"
    seen = set()
    seen.add(start)
    _, c = path(False)
    counter += c
    table[p] = "."
print(counter)
