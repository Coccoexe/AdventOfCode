#Part-1 
import os, re
from collections import deque

print("Advent of Code 2022 - Day 16")
print("Proboscidea Volcanium")
print("--- Part 1 ---")

# FUNCTIONS ----------------------------------------------

class Valve:
    def __init__(self, name, flow_rate, neighbors):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbors = neighbors
    
class State:
    def __init__(self, minute, position, opened, rate, total):
        self.minute = minute
        self.position = position
        self.opened = opened
        self.rate = rate
        self.total = total
    
    def flow(self, end=30):
        return self.total + self.rate * (end - self.minute + 1)

def distance(valves, a, b):
    if a == b:
        return 0
    
    visited = set()
    visited.add(a)
    to_visit = deque()
    for neighbor in valves[a].neighbors:
        visited.add(neighbor)
        to_visit.append((neighbor, 1))
    while to_visit:
        current, dist = to_visit.popleft()
        if current == b:
            return dist
        for neighbor in valves[current].neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                to_visit.append((neighbor, dist + 1))
    return None

# CONSTANTS ----------------------------------------------

start = "AA"
time = 30

# --------------------------------------------------------

file = open(os.path.dirname(__file__) + "\input.txt", "r")
lines = file.readlines()
file.close()

#parse input
valves = {}
for i in range(len(lines)):
    regex = re.findall(r"\d+|[A-Z]{2}", lines[i]) 
    valves[regex[0]] = Valve(regex[0],int(regex[1]),regex[2:])
    
#define pressurized valves and distances
pressurized_valves = [v.name for v in valves.values() if v.flow_rate > 0]
distances = {}
for v in valves.keys():
    distances[v] = {}
    for p in pressurized_valves:
        distances[v][p] = distance(valves, v, p)

#initialize state
initial_state = State(1, start, [], 0, 0)
max_flow = 0
states = [initial_state]

#search for max flow
while states:
    state = states.pop()
    max_flow = max(max_flow, state.flow())
    valve = valves[state.position]
    
    if state.minute == time:
        continue
    if state.position not in state.opened and valve.flow_rate > 0:
        states.append(
            State(
                state.minute + 1, 
                state.position, 
                state.opened[:] + [state.position], 
                state.rate + valve.flow_rate, 
                state.total + state.rate)
            )
        continue
    
    for next_valve in pressurized_valves:
        if next_valve in state.opened:
            continue
        distance = distances[state.position][next_valve]
        if (state.minute + distance) > time - 1:
            continue
        states.append(
            State(
                state.minute + distance,
                next_valve,
                state.opened,
                state.rate,
                state.total + (state.rate * distance)
            )
        )

print("Max flow:", max_flow)
print()

#Part-2 
print("--- Part 2 ---")

# CONSTANTS ----------------------------------------------

time_to_teach = 4

# --------------------------------------------------------

best_states = {}
all_states = {}
states = [initial_state]

while states:
    state = states.pop()
    valve = valves[state.position]
    
    if state.minute == time - time_to_teach:
        continue
    if state.position not in state.opened and valve.flow_rate > 0:
        state = State(
            state.minute + 1,
            state.position,
            state.opened[:] + [state.position],
            state.rate + valve.flow_rate,
            state.total + state.rate)
        states.append(state)
        opened = state.opened
        opened.sort()
        opened = tuple(opened)
        if best_states.get(opened,0) < state.flow(time-time_to_teach):
            best_states[opened] = state.flow(time-time_to_teach)
            all_states[opened] = state
        continue
    
    for next_valve in pressurized_valves:
        if next_valve in state.opened:
            continue
        distance = distances[state.position][next_valve]
        if (state.minute + distance) > time - 1:
            continue
        states.append(
            State(
                state.minute + distance,
                next_valve,
                state.opened,
                state.rate,
                state.total + (state.rate * distance)))

max_flow = 0
for human in all_states.values():
    for elephant in all_states.values():
        good_state = True
        for v in human.opened:
            if v in elephant.opened:
                good_state = False
                break
        if good_state:
            max_flow = max(max_flow, human.flow(time-time_to_teach) + elephant.flow(time-time_to_teach))
print("Max flow:", max_flow)
print()
