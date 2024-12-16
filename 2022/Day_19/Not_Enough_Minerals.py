#Part-1 
import os, re, math
print("Advent of Code 2022 - Day 19")
print("Not Enough Minerals")
print("--- Part 1 ---")

# FUNCTIONS ----------------------------------------------

def get_proportion(blueprint_id, blueprints):
    #ore
    ore = [1]
    #clay
    clay = [1]
    #obsidian
    if blueprints[blueprint_id][2] < blueprints[blueprint_id][3]:
        obsidian = [1,math.ceil(blueprints[blueprint_id][3] // blueprints[blueprint_id][2])]
    else:
        obsidian = [math.ceil(blueprints[blueprint_id][2] // blueprints[blueprint_id][3]),1]
    #geode
    if blueprints[blueprint_id][4] < blueprints[blueprint_id][5]:
        geode = [1,math.ceil(blueprints[blueprint_id][5] // blueprints[blueprint_id][4])]
    else:
        geode = [math.ceil(blueprints[blueprint_id][4] // blueprints[blueprint_id][5]),1]
    return {"ore": ore, "clay": clay, "obsidian": obsidian, "geode": geode}

def choose_robot(type, blueprint_id, robots, materials, proportion):
    
    #available materials
    ore = materials["ore"]
    clay = materials["clay"]
    obsidian = materials["obsidian"]

    #available robots
    ore_r = robots["ore"]
    clay_r = robots["clay"]
    obsidian_r = robots["obsidian"]

    p = proportion[type]

    #choose robot to build
    if type == "geode":
        if ore >= blueprints[blueprint_id][4] and obsidian >= blueprints[blueprint_id][5]:
            return type
        else:
            if ore_r < p[0] or obsidian_r < p[1]:
                if ore_r < p[0]:
                    print("need ore")
                    choose_robot("ore", blueprint_id, robots, materials, proportion)
                if obsidian_r < p[1]:
                    print("need obsidian")
                    choose_robot("obsidian", blueprint_id, robots, materials, proportion)
            else: 
                return None

    elif type == "obsidian":
        if ore >= blueprints[blueprint_id][2] and clay >= blueprints[blueprint_id][3]:
            return type
        else:
            if ore_r < p[0] or clay_r < p[1]:
                if ore_r < p[0]:
                    print("need ore")
                    choose_robot("ore", blueprint_id, robots, materials, proportion)
                if clay_r < p[1]:
                    print("need clay")
                    choose_robot("clay", blueprint_id, robots, materials, proportion)
            else: 
                return None

    elif type == "clay":
        if ore >= blueprints[blueprint_id][1]:
            return type
        else:
            if ore_r < p[0]:
                print("need ore")
                choose_robot("ore", blueprint_id, robots, materials, proportion)
            else: 
                return None
    
    elif type == "ore":
        if ore >= blueprints[blueprint_id][0]:
            return type
        else:
            return None

def collecting_ore(robots, materials):

    for r in robots:
        if r == "ore":
            materials["ore"] += robots[r]
        elif r == "clay":
            materials["clay"] += robots[r]
        elif r == "obsidian":
            materials["obsidian"] += robots[r]
        elif r == "geode":
            materials["geode"] += robots[r]

def build_robot(new_robots, blueprint_id, robots, materials):
    
    if new_robots == "ore":
        robots["ore"] += 1
        materials["ore"] -= blueprints[blueprint_id][0]
    elif new_robots == "clay":
        robots["clay"] += 1
        materials["clay"] -= blueprints[blueprint_id][1]
    elif new_robots == "obsidian":
        robots["obsidian"] += 1
        materials["obsidian"] -= blueprints[blueprint_id][2]
        materials["clay"] -= blueprints[blueprint_id][3]
    elif new_robots == "geode":
        robots["geode"] += 1
        materials["ore"] -= blueprints[blueprint_id][4]
        materials["obsidian"] -= blueprints[blueprint_id][5]



# CONSTANTS ----------------------------------------------

minutes = 24

# --------------------------------------------------------

#read file
file = open(os.path.dirname(__file__) + "\input.txt", "r")
lines = file.read().splitlines()
file.close()

#parse input
#                                   ore  ore   ore         clay        ore      obsidian
blueprints = {} #blueprints = {id: [ore, clay, obsidian_1, obsidian_2, geode_1, geode_2]}
for line in lines:
    regex = re.findall(r"\d+", line)
    blueprints[int(regex[0])] = [int(regex[1]), int(regex[2]), int(regex[3]), int(regex[4]), int(regex[5]), int(regex[6])]

for b in blueprints:
    robots = {
        "ore": 1,
        "clay": 0,
        "obsidian": 0,
        "geode": 0
        }
    materials = {
        "ore": 0,
        "clay": 0,
        "obsidian": 0,
        "geode": 0
        }
    proportion = get_proportion(b,blueprints)

    for m in range(1,minutes):
        #process blueprints to discover quality level
        print("Minute", m)

        new_robots = choose_robot("geode", b, robots, materials, proportion)
        print("new_robots", new_robots)
        collecting_ore(robots, materials)
        print("materials", materials)
        build_robot(new_robots, b, robots, materials)

        input()
    
    print("Blueprint", b, ":", robots, materials)

    
#choose the best quality level

#Part-2 
print("--- Part 2 ---")
