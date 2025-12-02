#Part-1 
import os
print("Advent of Code 2025 - Day 2")
print("Gift Shop")
print("--- Part 1 ---")

with open(os.path.join(os.path.dirname(__file__), 'input.txt'),'r') as f:
    
    a = 0
    for r in f.read().split(','):
        i,j = r.split('-')      
        
        for n in range(int(i), int(j)+1):
            s = len(str(n))
            if s%2 == 1: continue
            if str(n)[:s//2] == str(n)[s//2:]: a += n
    print(a)

#Part-2 
print("--- Part 2 ---")

def is_valid(n: int) -> int:
    s = str(n)
    l = len(s)
    for step in range(1, l):
        if l%step != 0: continue
        parts = [s[i:i+step] for i in range(0, l, step)]
        if len(set(parts)) == 1: return n
    return 0

with open(os.path.join(os.path.dirname(__file__), 'input.txt'),'r') as f:
    
    a = 0
    for r in f.read().split(','):
        i,j = r.split('-')      
        
        for n in range(int(i), int(j)+1):
            a += is_valid(n)
                
    print(a)