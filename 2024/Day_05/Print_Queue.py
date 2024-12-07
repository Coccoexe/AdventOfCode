#Part-1 
import os
import networkx as nx
from math import floor
print("Advent of Code 2024 - Day 5")
print("Print Queue")
print("--- Part 1 ---")
 
def validate_update(update):
    for i in range(len(update)-1):
        if G.has_edge(int(update[i]), int(update[i+1])):
            return False
    return True

DEBUG = True
lines = open(os.path.dirname(__file__) + "/input.txt", "r").read().split("\n\n")
rules = [[int(r) for r in rule.split("|")] for rule in lines[0].split("\n")]
updates = [[int(l) for l in update.split(",")] for update in lines[1].split("\n")]
numbers = list({u for update in updates for u in update})

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(numbers)
for rule in rules:
    G.add_edge(rule[1], rule[0]) # an arc represents a rule

# check updates
sum = 0
invalid = []
for update in updates:
    if validate_update(update):
        if DEBUG: print(f"Valid: {update}")
        sum += update[len(update)//2]
    else:
        invalid.append(update)

print(sum)

if DEBUG:
    import matplotlib.pyplot as plt
    nx.draw(G, with_labels=True)
    plt.show()

#Part-2 
print("--- Part 2 ---")

def reorder_invalid(update):
    while not validate_update(update):
        for i in range(len(update)-1):
            for j in range(i+1, len(update)):
                if G.has_edge(update[i], update[j]):
                    update[i], update[j] = update[j], update[i]
    return update

    
sum = 0
for inv in invalid:
    ordered = reorder_invalid(inv)
    sum += ordered[len(ordered)//2]

print(sum)