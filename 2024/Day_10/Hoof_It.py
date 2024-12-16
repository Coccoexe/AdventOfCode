#Part-1 
import os
print("Advent of Code 2024 - Day 10")
print("Hoof It")
print("--- Part 1 ---")

data = []

trailhead = []

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    for line in f.read().split('\n'):
        t = []
        for i in range(len(line)):
            t += [int(line[i])]
            if int(line[i]) == 0:
                trailhead += [(len(data),i)]
        data += [t]

score = 0
score_pt2 = 0
for y,x in trailhead:
    to_visit = [(y,x)]
    peaks = {}
    while to_visit:
        c_y,c_x = to_visit.pop()

        if data[c_y][c_x] == 9:
            peaks[(c_y,c_x)] = peaks.get((c_y,c_x),0) + 1
            continue

        # find node to explore
        if c_y - 1 > -1:
            if data[c_y-1][c_x] == data[c_y][c_x] + 1: to_visit += [(c_y-1, c_x)]
        if c_y + 1 < len(data):
            if data[c_y+1][c_x] == data[c_y][c_x] + 1: to_visit += [(c_y+1, c_x)]
        if c_x - 1 > -1:
            if data[c_y][c_x-1] == data[c_y][c_x] + 1: to_visit += [(c_y, c_x-1)]
        if c_x + 1 < len(data[c_y]):
            if data[c_y][c_x+1] == data[c_y][c_x] + 1: to_visit += [(c_y, c_x+1)]
    score += len(peaks)
    score_pt2 += sum(peaks.values())

print(score)

#Part-2 
print("--- Part 2 ---")
print(score_pt2)
