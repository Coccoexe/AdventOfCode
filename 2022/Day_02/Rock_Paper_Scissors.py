import os

print("Advent of Code 2022 - Day 2")
print("Rock Paper Scissors")
print("--- Part 1 ---")

file = open(os.path.dirname(__file__) + "/input.txt", "r")

# A, X = Rock      = 1
# B, Y = Paper     = 2
# C, Z = Scissors  = 3

lines = file.readlines()
file.close()

score = 0
for line in lines:
    if line[2] == "X":
        score += 1
    elif line[2] == "Y":
        score += 2
    elif line[2] == "Z":
        score += 3
    
    if line[0] == "A":
        if line[2] == "X":
            score += 3
        elif line[2] == "Y":
            score += 6
        elif line[2] == "Z":
            score += 0
    elif line[0] == "B":
        if line[2] == "X":
            score += 0
        elif line[2] == "Y":
            score += 3
        elif line[2] == "Z":
            score += 6
    elif line[0] == "C":
        if line[2] == "X":
            score += 6
        elif line[2] == "Y":
            score += 0
        elif line[2] == "Z":
            score += 3
print("Total score:", score)
print()


print("--- Part 2 ---")

# X = Lose
# Y = Draw
# Z = Win

score2 = 0
for line in lines:
    if line[2] == "X":
        score2 += 0
        if line[0] == "A":
            score2 += 3
        elif line[0] == "B":
            score2 += 1
        elif line[0] == "C":
            score2 += 2
    elif line[2] == "Y":
        score2 += 3
        if line[0] == "A":
            score2 += 1
        elif line[0] == "B":
            score2 += 2
        elif line[0] == "C":
            score2 += 3
    elif line[2] == "Z":
        score2 += 6
        if line[0] == "A":
            score2 += 2
        elif line[0] == "B":
            score2 += 3
        elif line[0] == "C":
            score2 += 1
print("Total score:", score2)
print()
        
    
