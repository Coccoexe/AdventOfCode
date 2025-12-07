#Part-1 
import os
print("Advent of Code 2025 - Day 7")
print("Laboratories")
print("--- Part 1 ---")

data =  open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r').readlines()
sources = set([data[0].find('S')])

split = 0
for line in data[1:]:
    t = set()
    for i in sources:
        if line[i] == '.': t.add(i)
        if line[i] == '^':
            split += 1
            if i-1 > -1: t.add(i-1)
            if i+1 < len(line): t.add(i+1)
    sources = t
print(split)

#Part-2 
print("--- Part 2 ---")

from collections import Counter
paths = Counter()
start = data[0].find('S')
paths[start] = 1
L = len(data[0])
for line in data[1:]:
    next_path = Counter()
    for c, count in paths.items():
        col = line[c]
        if col == '.':
            next_path[c] += count
        elif col == '^':
            if c > 0:
                next_path[c-1] += count
            if c+1 < L:
                next_path[c+1] += count

    paths = next_path
print(sum(paths.values()))

'''
NAIVE - exponential time

paths = [[data[0].find('S')]]
for line in data[1:]:
    t = []
    for p in paths:
        c = p[-1]
        if line[c] == '.': t.append(p + [c])
        if line[c] == '^':
            if c-1 > -1: t.append(p + [c - 1])
            if c+1 < len(line): t.append(p + [c + 1])
    paths = t
print(len(paths))

'''