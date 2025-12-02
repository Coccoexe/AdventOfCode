#Part-1 
import os
print("Advent of Code 2025 - Day 1")
print("Secret Entrance")
print("--- Part 1 ---")

with open(os.path.join(os.path.dirname(__file__), 'input.txt'),'r') as f:
    i = 50
    c = 0
    for l in f.readlines():
        i += int(l.strip()[1::]) if l[0] == 'R' else -int(l.strip()[1::])
        while i > 99: i -= 100
        while i < 0:  i += 100
        if i == 0:    c += 1 
    print('Password:',c)

#Part-2 
print("--- Part 2 ---")

with open(os.path.join(os.path.dirname(__file__), 'input.txt'),'r') as f:
    i = 50
    c = 0
    for l in f.readlines():
        a = int(l.strip()[1::])
        s = 1 if l[0] == 'R' else -1
        for _ in range(0,a):
            i += s
            if i == 100: i = 0
            if i == -1: i = 99
            if i == 0: c += 1
    print('Password:',c)
