#Part-1 
import os
from functools import cache

@cache
def blink(stones, n=25):
    if n == 0: return 1
    if stones == 0: return blink(1, n-1)

    if len(str(stones)) % 2 == 1:
        return blink(stones*2024, n-1)
    
    l = stones // 10**(len(str(stones))//2)
    r = stones % 10**(len(str(stones))//2)
    return blink(l, n-1) + blink(r, n-1)



print("Advent of Code 2024 - Day 11")
print("Plutonian Pebbles")
print("--- Part 1 ---")
stones = map(int, open(os.path.join(os.path.dirname(__file__), "input.txt")).read().split(' '))
print(sum(map(blink, stones)))

#Part-2 
print("--- Part 2 ---")

# change the n value to 75