import os
print("Advent of Code 2022 - Day 12")
print("Hill Climbing Algorithm")
print("--- Part 1 ---")

# FUNCTIONS ----------------------------------------------

def weight_func(a, b, edge_dict):
    if grid[a[0]][a[1]] < grid[b[0]][b[1]] - 1:
        return None
    return 1

# --------------------------------------------------------

file = open(os.path.dirname(__file__) + "/input.txt", "r")
grid = [list(line.strip()) for line in file.readlines()]
file.close()

from networkx import grid_2d_graph
from networkx import shortest_path

source = None
all_sources = []
target = None
for row_n, row in enumerate(grid):
    for col_n, c in enumerate(row):
        if c == "S":
            source = (row_n, col_n)
            grid[row_n][col_n] = "a"
        if c == "E":
            target = (row_n, col_n)
            grid[row_n][col_n] = "z"
        if grid[row_n][col_n] == "a":
            all_sources.append((row_n, col_n))

g = grid_2d_graph(len(grid), len(grid[0]))

grid = [[ord(c)-ord("a") for c in row] for row in grid]

shortest_len = len(shortest_path(g, source, target, weight_func))-1
print("The shortest path from S to E is " + str(shortest_len) + " steps long.")
print()

print("--- Part 2 ---")

paths = []
for s in all_sources:
    try:
        paths.append(len(shortest_path(g, s, target, weight_func))-1)
    except:
        pass
shortest_len = min(paths)
print("The shortest path from any square with elevation a to E is " + str(shortest_len) + " steps long.")
print()