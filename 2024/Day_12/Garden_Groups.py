#Part-1 
import os
print("Advent of Code 2024 - Day 12")
print("Garden Groups")
print("--- Part 1 ---")

data = [[c for c in line] for line in open(os.path.join(os.path.dirname(__file__), "input.txt")).read().split("\n")]

def compute_cost(region: set) -> int:
    _p, _a = 0, 0
    for y, x in region:
        p = 4
        if y-1 > -1 and (y-1,x) in region: p -= 1
        if y+1 < len(data) and (y+1,x) in region: p -= 1
        if x-1 > -1 and (y,x-1) in region: p -= 1
        if x+1 < len(data[y]) and (y,x+1) in region: p -= 1
        _p += p
        _a += 1
    return _p * _a

def compute_cost_discounted(region: set) -> int:


    return 0



cost = 0
cost_discounted = 0
region = set()
x, y = 0, 0
to_visit = set()
to_visit.add((y,x))
current = data[y][x]
while to_visit:
    y, x = to_visit.pop()
    
    if y-1 > -1 and data[y-1][x] == current: to_visit.add((y-1,x))
    if y+1 < len(data) and data[y+1][x] == current: to_visit.add((y+1,x))
    if x-1 > -1 and data[y][x-1] == current: to_visit.add((y,x-1))
    if x+1 < len(data[y]) and data[y][x+1] == current: to_visit.add((y,x+1))

    region.add((y,x))
    data[y][x] = "."

    if len(to_visit) == 0:
        cost += compute_cost(region)
        cost_discounted += compute_cost_discounted(region)
        region = set()
        # find next region
        found = False
        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] != ".":
                    current = data[y][x]
                    to_visit.add((y,x))
                    found = True
                    break
            if found: break
        if not found: break

print(cost)
print(cost_discounted)




#Part-2 
print("--- Part 2 ---")
