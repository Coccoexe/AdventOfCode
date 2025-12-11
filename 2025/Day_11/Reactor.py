#Part-1 
import os
print("Advent of Code 2025 - Day 11")
print("Reactor")
print("--- Part 1 ---")

graph, cache = {}, {}

# different path
def dp(start, end):
    global graph, cache
    if start == end: return 0                               
    if end in graph.get(start,[]): return 1                             # reached end node
    if (start, end) in cache: return cache[(start, end)]                # depth search cached
    
    res = sum(dp(neighbor, end) for neighbor in graph.get(start,[]))    # recursive search
    cache[(start,end)] = res                                            # save dp in cache
    return res

data = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

for l in data:
    f, t = l.split(':')
    graph[f] = []
    for i in t.strip().split(' '):
        graph[f].append(i)                                              # populate graph

print(dp('you','out'))                                                  # paths you -> out
    
#Part-2 
print("--- Part 2 ---")

from itertools import permutations

total = 0
for a, b in permutations(['dac','fft']):                                # paths svr->dac->fft->out, svr->fft->dac->out
    total += dp('svr', a) * dp(a, b) * dp(b, 'out')
print(total)