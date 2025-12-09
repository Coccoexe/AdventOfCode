#Part-1 
import os
from datetime import datetime
print("Advent of Code 2025 - Day 9")
print("TITLE")
print("--- Part 1 ---")

points = []
data = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
for l in data: points.append(list(map(int,l.strip().split(','))))

s = datetime.now()

N = len(points)
p1 = 0
p2 = 0
for i in range(N-1):
    for j in range(i+1, N):
        skip = False
        
        x1, y1 = points[i]
        x2, y2 = points[j]
        x1, x2 = min(x1,x2), max(x1,x2)
        y1, y2 = min(y1,y2), max(y1,y2)
        area = (x2-x1+1) * (y2-y1+1)
        if area > p1: p1 = area
        if area <= p2: continue
        
        for a in range(N):
            ax, ay = points[a]
            bx, by = points[(a+1)%N]
            
            if not ( 
                max(ax,bx) <= x1 or
                x2 <= min(ax,bx) or
                max(ay,by) <= y1 or
                y2 <= min(ay,by)
            ):
                skip = True
                break
        if skip: continue
        p2 = area
        
print(p1)

#Part-2 
print("--- Part 2 ---")

print(p2)

print(datetime.now() - s)