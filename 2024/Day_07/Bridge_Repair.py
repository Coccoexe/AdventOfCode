#Part-1 
import os
from itertools import product
print("Advent of Code 2024 - Day 7")
print("Bridge Repair")
print("--- Part 1 ---")

equations = []
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
    data = file.read().splitlines()
    for eq in data:
        res, op = eq.split(':')
        op = op.strip().split(' ')
        equations.append((int(res), [int(o) for o in op]))

def evaluate(eq,operators):
    a = eq[0]
    for i in range(1,len(eq)):
        if operators[i-1] == '+':
            a += eq[i]
        elif operators[i-1] == '*':
            a *= eq[i]
        elif operators[i-1] == '|':
            a = int(str(a) + str(eq[i]))
    return a

def solve(eq, operators=None):
    res, values = eq
    op = list(product(operators,repeat=len(values)-1))

    for o in op:
        if evaluate(values,o) == res:
            return True
    return False
            
sum = 0 
for eq in equations:
    if solve(eq, '+*'): 
        sum += eq[0]
print(f"The total calibration test is {sum}")

#Part-2 
print("--- Part 2 ---")

sum = 0
for eq in equations:
    if solve(eq, '+*|'): 
        sum += eq[0]
print(f"The total calibration test is {sum}")