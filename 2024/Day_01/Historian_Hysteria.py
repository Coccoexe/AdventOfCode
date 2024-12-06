#Part-1 
import os
print("Advent of Code 2024 - Day 1")
print("Historian Hysteria")
print("--- Part 1 ---")

a,b = [],[]
with open(os.path.dirname(__file__) + "/input.txt", "r") as file:
    for lines in file.readlines():
        i,j = lines.split()
        a.append(int(i))
        b.append(int(j))

a = sorted(a)
b = sorted(b)

s = 0
for i in range(len(a)):
    s += abs(a[i] - b[i])
print("The Total distance between the list is",s)

#Part-2 
print("--- Part 2 ---")
d = {}
for i in b:
    d[i] = d.get(i, 0) + 1

similarity = 0
for i in a:
    similarity += i * d.get(i, 0)
print("The similarity score is",similarity)