#Part-1 
import os, re
print("Advent of Code 2024 - Day 4")
print("Ceres Search")
print("--- Part 1 ---")

def count_XMAS(string):
    count = 0
    for i in range(len(string) - 3):
        if string[i:i + 4] == "XMAS": count += 1
    return count


# create rows, cols and diagonals from input
rows = open(os.path.dirname(__file__) + "/input.txt", "r").read().split("\n")
cols = [''.join(row[i] for row in rows) for i in range(len(rows[0]))]
diagonals = []
n = len(rows)
m = len(cols)
diagonals = []
for d in range(-(n - 1), m):
    temp = ''
    for i in range(max(0, d), min(n, m + d)):
        temp += rows[i][i - d]
    diagonals.append(temp)
for d in range(-(n - 1), m):
    temp = ''
    for i in range(max(0, d), min(n, m + d)):
        temp += rows[i][m - i + d - 1]
    diagonals.append(temp)

count = 0
for item in rows:
    count += count_XMAS(item)
    count += count_XMAS(item[::-1])
for item in cols:
    count += count_XMAS(item)
    count += count_XMAS(item[::-1])
for item in diagonals:
    count += count_XMAS(item)
    count += count_XMAS(item[::-1])
print(f"The Word XMAS appears {count} times.")

#Part-2 
print("--- Part 2 ---")

matrix = [list(row) for row in rows]

def is_MAS(string):
    if string == "MAS": return True
    if string == "SAM": return True
    return False

count = 0
for i in range(len(matrix)-2):
    for j in range(len(matrix[0])-2):

        if is_MAS(matrix[i][j] + matrix[i+1][j+1] + matrix[i+2][j+2]) and is_MAS(matrix[i+2][j] + matrix[i+1][j+1] + matrix[i][j+2]):
            count += 1

print(f"The Shape X-MAS appears {count} times.")
