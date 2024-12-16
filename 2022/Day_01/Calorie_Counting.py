import os

print("Advent of Code 2022 - Day 1")
print("Calorie Counting")
print("--- Part 1 ---")

file = open(os.path.dirname(__file__) + "/input.txt", "r")
lines = file.readlines()
file.close()

Elf_Calories = [0]
i = 0

for line in lines:
    if line == '\n':
        Elf_Calories.append(0)
        i += 1
    else:
        Elf_Calories[i] += int(line)

max = max(Elf_Calories)     
print("The most Calories are being carried by the Elf carrying " + str(max) + " Calories.")
print()

print("--- Part 2 ---")

max = sorted(Elf_Calories, reverse=True)[:3]
print("The top three Elves are carrying " + str(max[0]) + ", " + str(max[1]) + ", and " + str(max[2]) + " Calories, for a total of " + str(sum(max)) + " Calories.")
print()
