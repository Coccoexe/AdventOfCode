#Part-1 
import os, re
print("Advent of Code 2024 - Day 3")
print("Mull It Over")
print("--- Part 1 ---")

def eval_mul(mul):
    mul = mul.split(",")
    return int(mul[0][4:]) * int(mul[1][:-1])

memory = open(os.path.dirname(__file__) + "/input.txt", "r").read()

safe_mem = re.findall("mul\(\d+,\d+\)", memory)
sum = 0
for mul in safe_mem:
    sum += eval_mul(mul)
print(f"The sum of all safe multiplications in memory is: {sum}")

#Part-2 
print("--- Part 2 ---")

safe_mem = re.findall("do\(\)|mul\(\d+,\d+\)|don't\(\)", memory)
sum = 0
active = True
for mul in safe_mem:
    if mul == "do()":
        active = True
    elif mul == "don't()":
        active = False
    elif active:
        sum += eval_mul(mul)

print(f"The sum of all safe enabled multiplications in memory is: {sum}")

