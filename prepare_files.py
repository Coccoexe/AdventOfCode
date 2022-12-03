import os

for i in range(1,26):
    path = os.path.dirname(__file__) + "/Day_" + str(i)
    if not os.path.exists(path):
        os.makedirs(path)
        file = open(path + "/input.txt", "w")
        file.close()
        file = open(path+"/RENAME_ME.py", "w")
        file.write("#Part-1 \n")
        file.write("import os\n")
        file.write("\"Advent of Code 2022 - Day x\"\n")
        file.write("\"TITLE\"\n")
        file.write("\"--- Part 1 ---\"\n")
        file.write("\n")
        file.write("#Part-2 \n")
        file.write("\"--- Part 2 ---\"\n")
        file.close