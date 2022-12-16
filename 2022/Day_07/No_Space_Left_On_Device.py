import os

print("Advent of Code 2022 - Day 7")
print("No Space Left On Device")
print("--- Part 1 ---")

# FUNCTIONS --------------------------------------------

class Tree:
    def __init__(self,data,parent=None):
        self.data = data
        self.children = []
        self.parent = parent
        
    def __str__(self):
        return self.data
    
    def print_tree(self,spaces=1,separator="-"):
        r = str(self.data)
        for child in self.children:    
            if isinstance(child, Tree):
                r += "\n" + "  " * spaces + separator + child.print_tree(spaces=spaces+1)
            else:
                r += "\n" + "  " * spaces + separator + str(child)
        return r
            
    def add_child(self, obj):
        if isinstance(obj, Tree):
            obj.parent = self
            self.children.append(obj)
        else:
            self.children.append(obj)
        
    def get_children(self):
        return self.children    
    
    def get_parent(self):
        return self.parent
    
    def get_child_index(self, child_name):
        for i in range(len(self.children)):
            if isinstance(self.children[i], Tree):
                if self.children[i].data == child_name:
                    return i
            else:
                if self.children[i] == child_name:
                    return i
        return -1
 
def get_dir_size(dir):
    to_visit = [dir]
    sum = 0
    while len(to_visit) > 0:
        current = to_visit.pop()
        if not isinstance(current, Tree):
            sum += int(current[1])
        else:
            to_visit.extend(current.get_children())
    return sum

# CONSTANTS --------------------------------------------

max_size = 100000

# ------------------------------------------------------

file = open(os.path.dirname(__file__) + "/input.txt", "r")
lines = [line.strip() for line in file.read().splitlines()]
file.close()

root = Tree(lines[0].split("$ cd ")[1])

current = root
for line in lines[1:]:
    if line.startswith("$ cd"):
        if line.endswith(".."):
            current = current.get_parent()
        else:
            current = current.get_children()[current.get_child_index(line.split("$ cd ")[1])]
    elif line.startswith("$ ls"):
        continue
    else:
        if line.startswith("dir"):
            current.add_child(Tree(line.split("dir ")[1]))
        else:
            current.add_child([line.split(" ")[1],line.split(" ")[0]])

to_visit = [root]
sum = 0
while len(to_visit) > 0:
    current = to_visit.pop()
    if isinstance(current, Tree):
        to_visit.extend(current.get_children())
        if get_dir_size(current) <= max_size:
            sum += get_dir_size(current)

print("Sum of total sizes of directories with size <= " + str(max_size) + ": " + str(sum))
print()

print("--- Part 2 ---")

# CONSTANTS --------------------------------------------

space = 70000000
needed = 30000000

# ------------------------------------------------------

to_delete = needed - (space - get_dir_size(root))

best_dir = [root,get_dir_size(root)]
to_visit = [root]
while len(to_visit) > 0:
    current = to_visit.pop()
    if isinstance(current, Tree):
        to_visit.extend(current.get_children())
        current_size = get_dir_size(current)
        if current_size >= to_delete and current_size < best_dir[1]:
            best_dir = [current,current_size]
            
best = best_dir[1]
print("Total size of smallest directory to delete: " + str(best))
print()

out = open(os.path.dirname(__file__) + "/output.txt", "w")
out.write(root.print_tree())
out.close()


# ALTERNATIVE SOLUTIONS
#
# recursive solution
# def get_dir_size(dir):
#     if not isinstance(dir, Tree):
#         return int(dir[1])
#     
#     size = 0
#     children = dir.get_children()
#     for child in children:
#         size += get_dir_size(child)
#     return size 