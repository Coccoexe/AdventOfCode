# --- Day 7: No Space Left On Device ---
# You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?
# 
# The device the Elves gave you has problems with more than just its communication system. You try to run a system update:
# 
# $ system-update --please --pretty-please-with-sugar-on-top
# Error: No space left on device
# Perhaps you can delete some files to make space for the update?
# 
# You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:
# 
# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
# The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.
# 
# Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:
# 
# cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
# cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
# cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
# cd / switches the current directory to the outermost directory, /.
# ls means list. It prints out all of the files and directories immediately contained by the current directory:
# 123 abc means that the current directory contains a file named abc with size 123.
# dir xyz means that the current directory contains a directory named xyz.
# Given the commands and output in the example above, you can determine that the filesystem looks visually like this:
# 
# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)
# Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.
# 
# Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)
# 
# The total sizes of the directories above can be found as follows:
# 
# The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
# The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
# Directory d has total size 24933642.
# As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
# To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)
# 
# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

import os
import copy
print("Advent of Code 2022 - Day 7")
print("No Space Left On Device")
print("--- Part 1 ---")

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
 
#recursive solution
#def get_dir_size(dir):
#    if not isinstance(dir, Tree):
#        return int(dir[1])
#    
#    size = 0
#    children = dir.get_children()
#    for child in children:
#        size += get_dir_size(child)
#    return size 

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
  
file = open(os.path.dirname(__file__) + "/input.txt", "r")
lines = [line.strip() for line in file.read().splitlines()]

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
        if get_dir_size(current) <= 100000:
            sum += get_dir_size(current)
print(sum)
print("")

# --- Part Two ---
# Now, you're ready to choose a directory to delete.
# 
# The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.
# 
# In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.
# 
# To achieve this, you have the following options:
# 
# Delete directory e, which would increase unused space by 584.
# Delete directory a, which would increase unused space by 94853.
# Delete directory d, which would increase unused space by 24933642.
# Delete directory /, which would increase unused space by 48381165.
# Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.
# 
# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
print("--- Part 2 ---")

space = 70000000
needed = 30000000
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
print(best_dir[1])