#Part-1 
import os, copy
from collections import deque
print("Advent of Code 2025 - Day 5")
print("Cafeteria ")
print("--- Part 1 ---")


with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    data = [l.replace('\n',' ') for l in f.readlines()]

#  The first part consider the operation in rows: 123*45*6, 328+64+89, ...
#
#   123 328  51 64 
#    45 64  387 23 
#     6 98  215 314
#   *   +   *   +  

s = 0
f = 0                                                                       # pointer to first digit of current operation
for i in range(1, len(data[0])-1):                                          # iterate over height (except for the operators line)
    if data[-1][i] != ' ':                                                  # if found the next operator (i points to new operations)
        a = f'{data[-1][f]}'.join([v[f:i-1].strip() for v in data[:-1]])    # takes digit in each row from pointer f to i-1 and joins with operators -> output is an operation
        s += eval(a)                                                        # evaluate the operation and increase the total
        f = i
a = f'{data[-1][f]}'.join([v[f::].strip() for v in data[:-1]])              # join for the last row
s += eval(a)
print(s)


#Part-2 
print("--- Part 2 ---")

#  The second part consider the operation in column: 1*24*356, 369+248+8, ...
#
#   123 328  51 64 
#    45 64  387 23 
#     6 98  215 314
#   *   +   *   +  

s = 0
f = 0                                                                                                               # pointer to first digit of current operation
for i in range(1, len(data[0])-1):                                                                                  
    if data[-1][i] != ' ':
        a = f'{data[-1][f]}'.join([''.join(str(row[j]) for row in data[:-1]).strip() for j in range(f, i-1)])       # takes digit in column and join columns into an operation
        s += eval(a)
        f = i
a = f'{data[-1][f]}'.join([''.join(str(row[j]) for row in data[:-1]).strip() for j in range(f, len(data[0])-1)])
s += eval(a)
print(s)