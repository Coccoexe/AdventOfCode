#Part-1 
import os, copy
print("Advent of Code 2022 - Day 20")
print("Grove Positioning System")
print("--- Part 1 ---")

# FUNCTIONS ----------------------------------------------

def move_items():
    #for every item in original list
    for i in range(len(lines)):
        item = lines[i]

        #find where it is in the modified list
        index = to_modify.index([i,item])

        #remove the item from the modified list
        to_modify.pop(index)
        
        #move the item
        if index + item >= len(to_modify):
            to_modify.insert(index+item-len(to_modify),[i,item])
        elif index + item <= 0:
            to_modify.insert(index+item+len(to_modify),[i,item])
        else:
            to_modify.insert(index+item,[i,item])

def find_items():
    
    #find 0 in the modified list
    for item in to_modify:
        if item[1] == 0:
            index = to_modify.index(item)
            break

    for c in coordinates:
        tmp = c%len(to_modify)
        print(tmp)
        if index + tmp >= len(to_modify):
            yield to_modify[index+tmp-len(to_modify)][1]
        elif index + tmp <= 0:
            yield to_modify[index+tmp+len(to_modify)][1]
        else:
            yield to_modify[index+tmp][1]

# CONSTANTS ----------------------------------------------

coordinates = [1000,2000,3000]

# --------------------------------------------------------

file = open(os.path.dirname(__file__) + "\input.txt", "r")
lines = [int(x) for x in file.readlines()]
file.close()

#copy the original list to the one we will modify
to_modify = [[x,lines[x]] for x in range(len(lines))]

#move the items in the to_modify list
move_items()

#find the item in the coordinates list
sum = sum(find_items())
print("The sum of the items in the coordinates is: " + str(sum))

for i in to_modify:
    print(i[1],end=" ")

#Part-2 
print("--- Part 2 ---")
