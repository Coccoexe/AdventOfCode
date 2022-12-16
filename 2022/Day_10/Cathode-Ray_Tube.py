import os
print("Advent of Code 2022 - Day 10")
print("Cathode-Ray Tube")
print("--- Part 1 ---")

# FUNCTIONS ----------------------------------------------

def cycling():
    global cycle
    cycle += 1
    return cycle * registry

def processing():
    global registry,signals

    if lines[i][0] == "addx":
        for j in range(2):
            signal = cycling()
            signals.append([cycle,signal])
        registry += int(lines[i][1])
        
    elif lines[i][0] == "noop":
        signal = cycling()
        signals.append([cycle,signal])

def draw_pixel(black="."):
    
    comparison = cycle%40 if cycle%40 != 0 else 40
    
    if comparison in [registry, registry+1, registry+2]:
        return "#"
    else:
        return black

def processing_draw(black="."):
    global registry

    d = ""

    if lines[i][0] == "addx":
        for j in range(2):
            cycling()
            d += draw_pixel(black)
        registry += int(lines[i][1])
        
    elif lines[i][0] == "noop":
        cycling()
        d += draw_pixel(black)
        
    return d

# CONSTANTS ----------------------------------------------

signal_to_misure = [20, 60, 100, 140, 180, 220]

# ---------------------------------------------------------
    
file = open(os.path.dirname(__file__) + "/input.txt", "r")
lines = [line.split(" ") for line in file.read().splitlines()]
file.close()

registry = 1
cycle = 0
i = 0
signals = []
          
while i < len(lines):
    processing()
    i += 1

sum = sum([signal[1] for signal in signals if signal[0] in signal_to_misure])
print("The sum of the signals to measue is: {}".format(sum))
print()
    
print("--- Part 2 ---")

registry = 1
cycle = 0
i = 0
display_width = 40
    
draw = ""
while i < len(lines):
    draw += processing_draw(black=" ")
    i += 1
    
out = open(os.path.dirname(__file__) + "/output.txt", "w")
    
for i in range(0,len(draw),display_width):
    print(draw[i:i+display_width])
    out.writelines(draw[i:i+display_width] + "\n")

out.close()