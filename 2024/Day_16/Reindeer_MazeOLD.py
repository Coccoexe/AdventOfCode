#Part-1 
import os
print("Advent of Code 2024 - Day 16")
print("Reindeer Maze")
print("--- Part 1 ---")

data = open(os.path.join(os.path.dirname(__file__), "input.txt")).read().split('\n')
table = {}
dir = '>'
for r in range(len(data)):
    for c in range(len(data[r])):
        if data[r][c] == "S": start = (r,c)
        if data[r][c] == 'E': end = (r,c)
        table[(r,c)] = (float('inf'),None)

       

def heuristic(dir, curr, next, end):
    if dir in '^v':
        if curr[1] != next[1]: return 1001
        else: return 1
    if dir in '<>':
        if curr[0] != next[0]: return 1001
        else: return 1

 

def update_costs(table: dict, dir, curr, end):
    y, x = curr
    c_c, _ = table.get(curr)
    if data[y-1][x] != '#':
        cost = c_c + heuristic(dir,curr,(y-1,x),end)
        if table.get((y-1,x))[0] > cost:
            table[(y-1,x)] = (cost,'^')
    if data[y][x+1] != '#':
        cost = c_c + heuristic(dir,curr,(y,x+1),end)
        if table.get((y,x+1))[0] > cost:
            table[(y,x+1)] = (cost,'>')
    if data[y+1][x] != '#':
        cost = c_c + heuristic(dir,curr,(y+1,x),end)
        if table.get((y+1,x))[0] > cost:
            table[(y+1,x)] = (cost,'v')
    if data[y][x-1] != '#':
        cost = c_c + heuristic(dir,curr,(y,x-1),end)
        if table.get((y,x-1))[0] > cost:
            table[(y,x-1)] = (cost ,'<')  
    return

def get_next(table: dict, visited: set):
    min_k, min_v = None, float('inf')
    for k,v in table.items():
        if k in visited: continue
        if v[0] < min_v:
            min_k = k
            min_v = v[0]
    return min_k 

def print_table(visited: set):
    s = ' '+''.join(["{0:x}".format(i) for i in range(len(data))]) + '\n'
    for y in range(len(data)):
        s+="{0:x}".format(y)
        for x in range(len(data[y])):
            if data[y][x] == '.':
                s += 'O' if (y,x) in visited else '.'
            else:
                s+=data[y][x]
        s += '\n'
    print(s)

def print_costs(table: dict, visited: set):
    for k,v in table.items():
        if v[0] < float('inf') and k not in visited:
            print(k, v)

start, end = end, start
dir = 'v'

curr = start
table[curr] = (0,dir)
visited = set()
visited.add(curr)
while True:
    update_costs(table, dir, curr, end)
    next = get_next(table, visited)
    dir = table.get(next)[1]
    curr = next
    visited.add(curr)
    if end in visited:
        break

   

# backtrack
print(table[end])
path = set()
p = end
while True:
    d = table[p][1]
    path.add(p)
    match(d):
        case '^': p = (p[0]+1,p[1])
        case '>': p = (p[0],p[1]-1)
        case 'v': p = (p[0]-1,p[1])
        case '<': p = (p[0],p[1]+1)
    if p == start: break

print_table(path)

#Part-2 
print("--- Part 2 ---")
