#Part-1 
import os, re, itertools
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpInteger, PULP_CBC_CMD
print("Advent of Code 2025 - Day 10")
print("Factory")
print("--- Part 1 ---")

def part_1(bits, buttons):
    n_btns = len(buttons)
    best = None
    best_count = float('inf')

    # tutte le combinazioni di bottoni premuti
    for r in range(1, n_btns+1):
        for combo in itertools.combinations(range(n_btns), r):
            state = [0]*len(bits)
            for i in combo:
                for var in buttons[i]:
                    state[var] ^= 1  # toggle
            if state == bits:
                if r < best_count:
                    best_count = r
                    best = combo
        if best is not None:
            break

    return best

def part_2(buttons, target):
    n_buttons = len(buttons)
    n_counters = len(target)
    
    prob = LpProblem("MinButtonPresses", LpMinimize)
    x = [LpVariable(f"x{i}", lowBound=0, cat=LpInteger) for i in range(n_buttons)]
    
    for j in range(n_counters):
        prob += lpSum(x[i] for i in range(n_buttons) if j in buttons[i]) == target[j]
    
    prob += lpSum(x)
    prob.solve(PULP_CBC_CMD(msg=False))
        
    return [int(xi.varValue) for xi in x]

data = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
s1 = 0
s2 = 0
for l in data:
    bits    = [ int(c=='#')                  for c in re.findall(r'\[([^\]]*)\]',l)[0] ]
    buttons = [ list(map(int, b.split(','))) for b in re.findall(r'\(([^)]*)\)',l) ]
    target  = [ int(t)                       for t in re.findall(r'\{([^}]*)\}', l)[0].split(',') ]
    
    p1 = part_1(bits,buttons)
    s1 += len(p1)
    
    p2 = part_2(buttons,target)
    s2 += sum(p2)
print(s1)

#Part-2 
print("--- Part 2 ---")
print(s2)