#Part-1 
import os
print("Advent of Code 2025 - Day 3")
print("Lobby")
print("--- Part 1 ---")

def highest_digits(bank, n):
    b = list(bank[:n])
    for i in range(n, len(bank)):
        for j in range(n-1):
            if b[j+1] > b[j]:
                b = b[:j] + b[j+1:] + [bank[i]]
                break
        else:
            if bank[i] > b[n-1]:
                b[n-1] = bank[i]
                
    return int(''.join(b))

with open(os.path.join(os.path.dirname(__file__), 'input.txt'),'r') as f:
    joltage = 0
    for bank in f.readlines():
        joltage += highest_digits(bank.strip(),2)
    print('Max joltage available:',joltage)

#Part-2 
print("--- Part 2 ---")

with open(os.path.join(os.path.dirname(__file__), 'input.txt'),'r') as f:
    joltage = 0
    for bank in f.readlines():
        joltage += highest_digits(bank.strip(),12)
    print('Max joltage available:',joltage)
