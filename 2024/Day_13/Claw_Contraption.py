#Part-1 
import os, re
print("Advent of Code 2024 - Day 13")
print("Claw Contraption")
print("--- Part 1 ---")

def solve(x_a, y_a, x_b, y_b, x_p, y_p, add=0):
    x_p += add
    y_p += add
    a = (y_b*x_p - x_b*y_p) / (x_a*y_b - x_b*y_a)
    b = (-y_a*x_p + x_a*y_p) / (x_a*y_b - x_b*y_a)

    # unsolvable in linear
    if a%1 or b%1: return None, None

    return a,b    

def cost(machines):
    cost = 0
    for a,b in machines:
        if a is None: continue
        cost += a*3 + b*1
    return int(cost)
 
lines = open(os.path.join(os.path.dirname(__file__), "input.txt")).readlines()
machines = []

for i in range(0,len(lines),4):
    x_a, y_a = re.findall('\d+',lines[i])
    x_b, y_b = re.findall('\d+',lines[i+1])
    x_p, y_p = re.findall('\d+',lines[i+2])
    machines.append(solve(int(x_a), int(y_a), int(x_b), int(y_b), int(x_p), int(y_p),10000000000000))

print(cost(machines))

#Part-2 
print("--- Part 2 ---")

# change add factor to 10000000000000