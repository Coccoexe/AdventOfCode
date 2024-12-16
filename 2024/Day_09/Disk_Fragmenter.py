#Part-1 
import os
print("Advent of Code 2024 - Day 9")
print("Disk Fragmenter")
print("--- Part 1 ---")

data = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()

def format_disk(data):
    disk = []
    count = 0
    for i in range(len(data)):
        if i % 2 == 0:
            disk += [str(count)]*int(data[i])
            count += 1
        else:
            disk += '.'*int(data[i])
    return disk

def checksum_disk(disk):
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == '.': continue
        checksum += int(disk[i])*i
    return checksum

disk = format_disk(data)

# compact disk
start, end = 0, len(disk)-1
while start < end:
    if disk[start] != '.':
        start += 1
        continue

    if disk[end] == '.':
        end -= 1
        continue

    disk[start], disk[end] = disk[end], disk[start]
    start, end = start+1, end-1

print("Checksum:", checksum_disk(disk))

#Part-2 
print("--- Part 2 ---")

def find_available_space(disk, end, length):
    for i in range(end):
        if disk[i] == '.':
            count = 0
            for j in range(i, end):
                if disk[j] == '.':
                    count += 1
                    if count == length:
                        return i
                else:
                    break
                
    return -1

disk = format_disk(data)

# compact disk
a, b = len(disk)-1, len(disk)-1
while a > 0:

    # find block
    while disk[a] == disk[b]:
        a -= 1
    while disk[b] == '.' and b > a+1:
        b -= 1

    if disk[b] == '.':
        b = a
        continue


    # find available space
    space = find_available_space(disk, b, b-a)
    if space == -1:
        b = a
        continue

    # move block
    disk[a+1:b+1], disk[space:space+b-a] = disk[space:space+b-a], disk[a+1:b+1]

    b = a

print("Checksum:", checksum_disk(disk))