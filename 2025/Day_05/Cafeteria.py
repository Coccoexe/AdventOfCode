#Part-1 
import os, copy
from collections import deque
print("Advent of Code 2025 - Day 5")
print("Cafeteria ")
print("--- Part 1 ---")

def merge_ranges(ranges):
    intervals = sorted((int(a), int(b)) for a, b in ranges)
    merged = []
    for start, end in intervals:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    ranges = deque()
    for line in f:
        if not (s := line.strip()): break
        ranges.append(tuple(s.split('-')))
      
    ids = deque(sorted(int(l.strip()) for l in f))  # !!!IMPORTANT!!! ids must be sorted for assumption in processing
ranges = deque(merge_ranges(ranges))

r = copy.deepcopy(ranges)
lb, ub = r.popleft()
stop = False
count = 0
while ids:
    c = ids.popleft()                   # next id
    
    while c > ub:                       # id over the last range
        if not r: stop = True
        if stop: break
        lb, ub = r.popleft()
    if stop: break
    
    if c < lb: continue                 # id below range
    
    if c <= ub: count += 1              # id in range
            
print(count)

#Part-2 
print("--- Part 2 ---")

count = 0
for lb,ub in ranges:
    count += ub-lb+1
print(count)