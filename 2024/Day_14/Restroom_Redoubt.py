#Part-1 
import os, cv2, numpy as np
print("Advent of Code 2024 - Day 14")
print("Restroom Redoubt")
print("--- Part 1 ---")

lines = open(os.path.join(os.path.dirname(__file__), "input.txt")).readlines()

robots = []
for line in lines:
    p,v = line.split()[0][2:].split(',') , line.split()[1][2:].split(',')
    robots.append({'p':list(map(int,p)),'v':list(map(int,v))})

WIDTH = 101
HEIGHT = 103

def move(robots):
    for robot in robots:
        robot['p'][0] += robot['v'][0]
        robot['p'][1] += robot['v'][1]
        if robot['p'][0] < 0: robot['p'][0] = WIDTH + robot['p'][0]
        if robot['p'][0] >= WIDTH: robot['p'][0] = robot['p'][0] - WIDTH
        if robot['p'][1] < 0: robot['p'][1] = HEIGHT + robot['p'][1]
        if robot['p'][1] >= HEIGHT: robot['p'][1] = robot['p'][1] - HEIGHT
            
    return robots

def print_grid(robots):
    grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for robot in robots:
        grid[robot['p'][1]][robot['p'][0]] = grid[robot['p'][1]][robot['p'][0]] + 1 if grid[robot['p'][1]][robot['p'][0]] != '.' else 1
    for row in grid:
        print(''.join(map(str,row)))

def grid_png(robots,i):
    grid = np.zeros((HEIGHT,WIDTH,3), np.uint8)
    for robot in robots:
        grid[robot['p'][1],robot['p'][0]] = [255,255,255]
    cv2.imwrite(os.path.join(os.path.dirname(__file__), f"images/{i+1}.png"),grid)

def compute_area(robots):
    tl, tr, bl, br = 0,0,0,0
    for y in range(HEIGHT//2):
        for x in range(WIDTH//2):
            tl += sum([1 for robot in robots if robot['p'] == [x,y]])

        for x in range(WIDTH//2+1,WIDTH):
            tr += sum([1 for robot in robots if robot['p'] == [x,y]])

    for y in range(HEIGHT//2+1,HEIGHT):
        for x in range(WIDTH//2):
            bl += sum([1 for robot in robots if robot['p'] == [x,y]])

        for x in range(WIDTH//2+1,WIDTH):
            br += sum([1 for robot in robots if robot['p'] == [x,y]])

    return tl * tr * bl * br

for i in range(100):
    robots = move(robots)
    grid_png(robots,i)
print(compute_area(robots))


#Part-2 
print("--- Part 2 ---")

for i in range(100,10000):
    robots = move(robots)
    grid_png(robots,i)