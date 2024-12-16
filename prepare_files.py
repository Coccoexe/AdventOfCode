import os

year = 2024

for i in range(1,25):
    path = os.path.dirname(__file__) + "/{}/Day_".format(year) + str(i) if i >= 10 else os.path.dirname(__file__) + "/{}/Day_0".format(year) + str(i)
    if not os.path.exists(path):
        os.makedirs(path)
        file = open(path + "/input.txt", "w")
        file.close()
        file = open(path + "/instructions.txt", "w")
        file.close
        file = open(path+"/RENAME_ME.py", "w")
        file.write("#Part-1 \n")
        file.write("import os\n")
        file.write(f"print(\"Advent of Code {year} - Day "+ str(i) +"\")\n")
        file.write("print(\"TITLE\")\n")
        file.write("print(\"--- Part 1 ---\")\n")
        file.write("\n")
        file.write("#Part-2 \n")
        file.write("print(\"--- Part 2 ---\")\n")
        file.close
        