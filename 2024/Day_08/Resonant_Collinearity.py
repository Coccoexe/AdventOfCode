#Part-1 
import os, string
print("Advent of Code 2024 - Day 8")
print("Resonant Collinearity")
print("--- Part 1 ---")

def extract_data(data, c):
    return [[ch if c==ch else '.' for ch in line] for line in data]

def compute_antinodes(data, antinodes, p1=True):
        for r in range(len(data)):
            for c in range(len(data[r])):
                if data[r][c] == '.': continue
                
                # search another antenna
                for y in range(len(data)):
                    for x in range(len(data[y])):
                        # skip empty cells
                        if data[y][x] == '.': continue
                        # skip the same antenna
                        if x == c and y == r: continue
                        dx, dy = x-c, y-r

                        # add antinodes before this antenna
                        before, after = 1, 1
                        while True:
                            if p1 and before > 1: break
                            if c-before*dx < 0 or r-before*dy < 0 or r-before*dy > len(data)-1 or c-before*dx > len(data[r])-1: break
                            if data[r-before*dy][c-before*dx] != '.': continue
                            antinodes[r-before*dy][c-before*dx] = '#'
                            before += 1

                        # add antinodes after the other antenna
                        while True:
                            if p1 and after > 1: break
                            if x+after*dx < 0 or y+after*dy < 0 or y+after*dy > len(data)-1 or x+after*dx > len(data[y])-1: break
                            if data[y+after*dy][x+after*dx] != '.': continue
                            antinodes[y+after*dy][x+after*dx] = '#'
                            after += 1
                if not p1: antinodes[r][c] = '#'
                        
        return

def count_antinodes(antinodes):
    count = 0
    for r in range(len(antinodes)):
        for c in range(len(antinodes[r])):
            if antinodes[r][c] == '#': count += 1
    return count

data = [[c for c in line] for line in open(os.path.join(os.path.dirname(__file__), 'input.txt')).read().splitlines()]
char = list(string.ascii_letters + string.digits)

antinodes = [['.' for c in range(len(data[0]))] for r in range(len(data))]
for c in char:
    compute_antinodes(extract_data(data, c), antinodes)

print(count_antinodes(antinodes))


#Part-2 
print("--- Part 2 ---")

antinodes = [['.' for c in range(len(data[0]))] for r in range(len(data))]
for c in char:
    compute_antinodes(extract_data(data, c), antinodes, False)

print(count_antinodes(antinodes))