import os
print("Advent of Code 2022 - Day 8")
print("Treetop Tree House")
print("--- Part 1 ---")

# FUNCTIONS ----------------------------------------------

#check if tree is visible
#check every direction if there is a tree visible in that direction return true
#otherwise check next direction
#return false if tree is not visible in any direction
def isVisible(i,j):

    #top
    for k in range(0,i):
        if matrix[i][j] <= matrix[k][j]:
            break
        if k == i-1:
            return True  
        
    #bottom
    for k in range(i+1,len(matrix)):
        if matrix[i][j] <= matrix[k][j]:
            break
        if k == len(matrix)-1:
            return True
    
    #left
    for k in range(0,j):
        if matrix[i][j] <= matrix[i][k]:
            break
        if k == j-1:
            return True

    #right
    for k in range(j+1,len(matrix[i])):
        if matrix[i][j] <= matrix[i][k]:
            break
        if k == len(matrix[i])-1:
            return True
    
    return False

def scenic_score(i,j):
    score = 1
    
    #top
    tree = 0
    for k in range(1,i+1):
        tree += 1
        if matrix[i][j] <= matrix[i-k][j]:
            break
    score = score * tree if tree > 0 else score
    
    #bottom
    tree = 0
    for k in range(i+1,len(matrix)):
        tree += 1
        if matrix[i][j] <= matrix[k][j]:
            break
    score = score * tree if tree > 0 else score
    
    #left
    tree = 0
    for k in range(1,j+1):
        tree += 1
        if matrix[i][j] <= matrix[i][j-k]:
            break
    score = score * tree if tree > 0 else score
    
    #right
    tree = 0
    for k in range(j+1,len(matrix[i])):
        tree += 1
        if matrix[i][j] <= matrix[i][k]:
            break
    score = score * tree if tree > 0 else score
    
    return score

# -------------------------------------------------------

file = open(os.path.dirname(__file__) + "/input.txt", "r")
lines = [line.strip() for line in file.read().splitlines()]
file.close()

#create matrix
matrix = [[] for i in range(len(lines))]
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if i == 0 or i == len(lines)-1 or j == 0 or j == len(lines[i])-1:
            matrix[i].append(int(lines[i][j]))
        else:
            matrix[i].append(int(lines[i][j]))

#count visible trees
visible = len(matrix[0]) * 2 + (len(matrix)-2) * 2

for i in range(1,len(matrix)-1):
    for j in range(1,len(matrix[i])-1):
        if isVisible(i,j):
            visible += 1
   
print("Number of visible trees: " + str(visible))
print()

print("--- Part 2 ---")

max_score = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        score = scenic_score(i,j)
        if score > max_score:
            max_score = score
        
print("Highest scenic score: " + str(max_score))
print()