import os
print("Advent of Code 2022 - Day 6")
print("Tuning Trouble")
print("--- Part 1 ---")

# FUNCTIONS ----------------------------------------------

#return string of unique characters in string
def unique_chars(chars):
    unique = ""
    for c in chars:
        if c not in unique:
            unique += c
    return unique

#return the index of the last character of the first marker
def find_marker(length):
    #buffer of previous 3 characters
    chars = lines[:length-1]
    i = length-1
    for c in lines[length-1:]:
        i += 1
        #if the buffer is unique and the current char is not in the buffer
        if len(unique_chars(chars)) > length-2 and c not in chars:
            break
        #otherwise, add the current char to the buffer and remove the oldest one
        else:
            chars = chars[1:] + c
    return i

# CONSTANTS ----------------------------------------------

packet_length = 4

# --------------------------------------------------------

file = open(os.path.dirname(__file__) + "/input.txt", "r")
lines = file.read()
file.close()

marker = find_marker(packet_length)
print("The first marker is at index " + str(marker) + " (" + lines[marker] + ")")
print()

print("--- Part 2 ---")

# CONSTANTS ----------------------------------------------

packet_length = 14

# --------------------------------------------------------

marker = find_marker(packet_length)
print("The first marker is at index " + str(marker) + " (" + lines[marker] + ")")
print()