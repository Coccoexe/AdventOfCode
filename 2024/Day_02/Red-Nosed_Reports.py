#Part-1 
import os
print("Advent of Code 2024 - Day 2")
print("Red-Nosed Reports")
print("--- Part 1 ---")

lines = []
with open(os.path.dirname(__file__) + "/input.txt", "r") as file:
    for l in file.readlines():
        lines.append([int(a) for a in l.split()])

def is_safe(l):
    asc = l[0] <= l[1]
    for i in range(1, len(l)):
        if abs(l[i]-l[i-1]) > 3:
            return False, i
        if asc and l[i] <= l[i-1]:
            return False, i
        if not asc and l[i] >= l[i-1]:
            return False, i
    return True, None

safe = 0
for l in lines:       
    s, _ = is_safe(l)
    safe += s

print(f"There are {safe} safe reports")

#Part-2 
print("--- Part 2 ---")

safe = 0
for l in lines:
    # Check if the list is safe
    s, i = is_safe(l)
    if s: 
        safe += 1
        continue
    s, _ = is_safe(l[:i] + l[i+1:])
    if s:
        safe += 1
        continue

    # check in reversed for the first value
    reversed_list = l[::-1]
    s, i = is_safe(reversed_list)
    if s: 
        safe += 1
        continue
    s, _ = is_safe(reversed_list[:i] + reversed_list[i+1:])

    safe += s
print(f"There are {safe} safe reports after fixing")
