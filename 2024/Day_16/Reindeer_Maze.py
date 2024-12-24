#Part-1 
import os
from collections import defaultdict
from heapq import heappop, heappush
print("Advent of Code 2024 - Day 16")
print("Reindeer Maze")
print("--- Part 1 ---")

data = open(os.path.join(os.path.dirname(__file__), "input.txt")).read().split('\n')

table = {}
for r in range(len(data)):
    for c in range(len(data[r])):
        if data[r][c] == '#': continue
        if data[r][c] == 'S': start = r+c*1j
        if data[r][c] == 'E': end = r+c*1j
        table[r+c*1j] = data[r][c]

visited = []
best = 1e9
cost = defaultdict(lambda: 1e9)
todo = [(0, t:=0, start, 1j, [start])]
while todo:
    val, _, pos, dir, path = heappop(todo)

    if val > cost[pos, dir]: continue
    else: cost[pos, dir] = val

    if table[pos] == 'E' and val <= best:
        visited += path
        best = val

    for r, v in (1, 1), (+1j, 1001), (-1j, 1001):
        v, t, p, d = val+v, t+1, pos + dir*r, dir*r
        if p not in table: continue
        heappush(todo, (v, t, p, d, path + [p]))


print("Shortest path:", best)

#Part-2 
print("--- Part 2 ---")
print("Visited:", len(set(visited)))