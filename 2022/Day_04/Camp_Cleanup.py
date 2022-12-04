# --- Day 4: Camp Cleanup ---
# Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.
# 
# However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).
# 
# For example, consider the following list of section assignment pairs:
# 
# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8
# For the first few pairs, this list means:
# 
# Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
# The Elves in the second pair were each assigned two sections.
# The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
# This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:
# 
# .234.....  2-4
# .....678.  6-8
# 
# .23......  2-3
# ...45....  4-5
# 
# ....567..  5-7
# ......789  7-9
# 
# .2345678.  2-8
# ..34567..  3-7
# 
# .....6...  6-6
# ...456...  4-6
# 
# .23456...  2-6
# ...45678.  4-8
# Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.
# 
# In how many assignment pairs does one range fully contain the other?

import os
import numpy as np

print("Advent of Code 2022 - Day 4")
print("Camp Cleanup")
print("--- Part 1 ---")

file = open(os.path.dirname(__file__) + "/input.txt", "r")

lines = [line.strip() for line in file.read().splitlines()]
pairs = [line.split(",") for line in lines]

fully_contained = 0
for pair in pairs:
    first = pair[0].split("-")
    second = pair[1].split("-")
    start_difference = int(first[0]) - int(second[0])
    end_difference = int(first[1]) - int(second[1])
    
    # if the signs of the two differences are the different, then one of the ranges are fully contained in the other
    # also if one of the differences is 0, then the ranges are fully contained
    # 
    # 6-6,4-6 -> 2,0 it contains a 0 and in fact is fully contained
    #
    # 2-8,3-7 -> -1,1 signs are different, fully contained
    #
    # 2-4,6-8 -> -4,-4 the signs are the same, so it is not fully contained
    #
    if 0 not in [start_difference, end_difference]:
        if np.sign(start_difference) != np.sign(end_difference):
            fully_contained += 1
    else:
        fully_contained += 1

print(fully_contained)
print("")
    
# --- Part Two ---
# It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.
# 
# In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:
# 
# 5-7,7-9 overlaps in a single section, 7.
# 2-8,3-7 overlaps all of the sections 3 through 7.
# 6-6,4-6 overlaps in a single section, 6.
# 2-6,4-8 overlaps in sections 4, 5, and 6.
# So, in this example, the number of overlapping assignment pairs is 4.
# 
# In how many assignment pairs do the ranges overlap?

print("--- Part 2 ---")

not_overlaped = 0
for pair in pairs:
    first = pair[0].split("-")
    second = pair[1].split("-")
    if int(first[1]) < int(second[0]) or int(second[1]) < int(first[0]):
        not_overlaped += 1
            
print(len(pairs) - not_overlaped)
    

