#Part-1 
import os
print("Advent of Code 2024 - Day 15")
print("Warehouse Woes")
print("--- Part 1 ---")

data = open(os.path.join(os.path.dirname(__file__), "input.txt")).read().split('\n')
table = []
moves = []
flag = False
for r in range(len(data)):
    t = []
    if data[r] == '': flag = True
    for c in range(len(data[r])):
        if flag: moves += data[r][c]
        else: t += data[r][c]
        if data[r][c] == "@": pos = (r,c)
    if not flag: table += [t]


def to_move(dir, pos):
    y, x = pos
    while True:
        if table[y][x] == '#': break
        match(dir):
            case '^': y-=1
            case '>': x+=1
            case 'v': y+=1
            case '<': x-=1
        if table[y][x] == '.': break
    return (y, x)
     

def move(dir, pos, to):
    _y, _x = pos
    y, x = to
    while y != _y or x != _x:        
        match(dir):
            case '^':
                if table[y][x] == '.':
                    table[y][x], table[y+1][x] = table[y+1][x], table[y][x]
                y+=1
            case '>':
                if table[y][x] == '.':
                    table[y][x], table[y][x-1] = table[y][x-1], table[y][x]
                x-=1
            case 'v':
                if table[y][x] == '.':
                    table[y][x], table[y-1][x] = table[y-1][x], table[y][x]
                y-=1
            case '<':
                if table[y][x] == '.':
                    table[y][x], table[y][x+1] = table[y][x+1], table[y][x]
                x+=1

    match(dir):
            case '^':
                if table[y-1][x] == '@': return (y-1,x)
            case '>':
                if table[y][x+1] == '@': return (y,x+1)
            case 'v':
                if table[y+1][x] == '@': return (y+1,x)
            case '<':
                if table[y][x-1] == '@': return (y,x-1)
    return (y,x)

def compute_GPS(table):
    count = 0
    for y in range(len(table)):
        for x in range(len(table[y])):
            if table[y][x] in 'O[': count += y*100 + x
    print(count)

def print_table():
    s = ''
    for row in table:
        for c in row:
            s += c
        s += '\n'
    print(s)

for m in moves:
    to = to_move(m, pos)
    pos = move(m,pos,to)

compute_GPS(table)
print_table()

#Part-2 
print("--- Part 2 ---")

table = []
flag = False
for r in range(len(data)):
    t = []
    if data[r] == '': flag = True
    for c in range(len(data[r])):
        if flag: continue
        else: 
            match data[r][c]:
                case '#': t += ['#','#']
                case 'O': t += ['[',']']
                case '.': t += ['.','.']
                case '@': t += ['@','.']
            if data[r][c] == "@": pos = (r,2*c)
    if not flag: table += [t]

def to_move_2(dir, pos):
    check = set()
    check.add(pos)
    tm = set()
    while True:
        if len(check) == 0: break
        y, x = check.pop()
        match(dir):
            case '^': 
                if table[y-1][x] == '[': 
                    tm.add((y,x))
                    check.add((y-1,x))
                    check.add((y-1,x+1))
                elif table[y-1][x] == ']': 
                    tm.add((y,x))
                    check.add((y-1,x))
                    check.add((y-1,x-1)) 
                elif table[y-1][x] == '.': 
                    tm.add((y,x))
                elif table[y-1][x] == '#': 
                    return set()
            case '>':
                if table[y][x+1] in '[]':
                    tm.add((y,x))
                    check.add((y,x+1))
                elif table[y][x+1] == '.': 
                    tm.add((y,x))
                elif table[y][x+1] == '#':
                    return set()
            case 'v':
                if table[y+1][x] == '[': 
                    tm.add((y,x))
                    check.add((y+1,x))
                    check.add((y+1,x+1))
                elif table[y+1][x] == ']': 
                    tm.add((y,x))
                    check.add((y+1,x))
                    check.add((y+1,x-1))
                elif table[y+1][x] == '.':
                    tm.add((y,x))
                elif table[y+1][x] == '#':
                    return set()
            case '<':
                if table[y][x-1] in '[]':
                    tm.add((y,x))
                    check.add((y,x-1))
                elif table[y][x-1] == '.':
                    tm.add((y,x))
                elif table[y][x-1] == '#':
                    return set()

    return tm

def move_2(dir, pos, tm):

    match(dir):
        case '^':
            l = sorted(tm, key=lambda x: (x[0], x[1]))
        case '>':
            l = sorted(tm, key=lambda x: (x[1],x[0]), reverse=True)
        case 'v':
            l = sorted(tm, key=lambda x: (x[0],x[1]), reverse=True)
        case '<':
            l = sorted(tm, key=lambda x: (x[1],x[0]))


    for i in range(len(l)):
        y, x = l[i]
        match dir:
            case '^':
                table[y][x], table[y-1][x] = table[y-1][x], table[y][x]
            case '>':
                table[y][x], table[y][x+1] = table[y][x+1], table[y][x]
            case 'v':
                table[y][x], table[y+1][x] = table[y+1][x], table[y][x]
            case '<':
                table[y][x], table[y][x-1] = table[y][x-1], table[y][x]

    y, x = pos
    match(dir):
            case '^':
                if table[y-1][x] == '@': return (y-1,x)
            case '>':
                if table[y][x+1] == '@': return (y,x+1)
            case 'v':
                if table[y+1][x] == '@': return (y+1,x)
            case '<':
                if table[y][x-1] == '@': return (y,x-1)
    return pos

for m in moves:
    tm = to_move_2(m, pos)
    if len(tm) == 0: continue
    pos = move_2(m,pos,tm)
compute_GPS(table)
print_table()