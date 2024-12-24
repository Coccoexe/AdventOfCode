#Part-1 
import os, math
print("Advent of Code 2024 - Day 17")
print("Chronospatial Computer")
print("--- Part 1 ---")

data = open(os.path.join(os.path.dirname(__file__), "input.txt")).read().split('\n')

A = int(data[0].split(' ')[-1])
B = int(data[1].split(' ')[-1])
C = int(data[2].split(' ')[-1])
P = list(map(int,data[4].split(' ')[-1].split(',')))
pointer = 0
out = []

def get_combo_code(operand):
    global A, B, C
    match(operand):
        case 0: return 3
        case 4: return A
        case 5: return B
        case 6: return C
        case _: return operand

def execute(opcode, operand):
    global A, B, C, pointer
    match(opcode):
        case 0:
            A = math.floor(A / (2**get_combo_code(operand)))
        case 1:
            B = B ^ operand
        case 2:
            B = get_combo_code(operand) % 8
        case 3:
            if A != 0: pointer = operand - 2
        case 4:
            B = B ^ C
        case 5:
            out.append(get_combo_code(operand) % 8)
        case 6:
            B = math.floor(A / (2**get_combo_code(operand)))
        case 7:
            C = math.floor(A / (2**get_combo_code(operand)))      

while pointer < len(P):
    execute(P[pointer],P[pointer+1])
    pointer += 2

print(','.join(map(str,out)))

#Part-2 
print("--- Part 2 ---")

g = list( map( int, open(os.path.join(os.path.dirname(__file__), "input.txt") ).read().split()[ -1 ].split( ',' ) ) )

def solve( p, r ):
    if p < 0:
        print( r )
        return True
    for d in range( 8 ):
        a, i = r << 3 | d, 0
        while i < len( g ):
            if   g[ i + 1 ] <= 3: o = g[ i + 1 ]
            elif g[ i + 1 ] == 4: o = a
            elif g[ i + 1 ] == 5: o = b
            elif g[ i + 1 ] == 6: o = c
            if   g[ i ] == 0: a >>= o
            elif g[ i ] == 1: b  ^= g[ i + 1 ]
            elif g[ i ] == 2: b   = o & 7
            elif g[ i ] == 3: i   = g[ i + 1 ] - 2 if a != 0 else i
            elif g[ i ] == 4: b  ^= c
            elif g[ i ] == 5: w   = o & 7; break
            elif g[ i ] == 6: b   = a >> o
            elif g[ i ] == 7: c   = a >> o
            i += 2
        if w == g[ p ] and solve( p - 1, r << 3 | d ):
            return True
    return False

solve( len( g ) - 1, 0 )