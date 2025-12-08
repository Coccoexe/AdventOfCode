#Part-1 
import os, math
from collections import defaultdict, deque
print("Advent of Code 2025 - Day 8")
print("Playground")
print("--- Part 1 ---")

CONNECTIONS = 1000
TOP_CONN = 3

class Point:
    def __init__(self, coord):
        self.x = int(coord[0])
        self.y = int(coord[1])
        self.z = int(coord[2])
    def __repr__(self):
        return f'X: {self.x}, Y: {self.y}, Z: {self.z}'
def distance(p1: Point, p2: Point): return abs( (p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2 )

points = dict()
data = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
for i,l in enumerate(data): points[i] = Point(l.strip().split(','))
distances = defaultdict(int)
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distances[(i,j)] = distance(points[i],points[j])

# compute connected edges and create graph
graph = defaultdict(list)
c = 0
last = None
for a,b in sorted(distances, key=distances.get):
    graph[a].append(b)
    graph[b].append(a)
    c += 1
    if c >= CONNECTIONS: break

visited = set()
components = []
for node in graph:
    if node not in visited:
        # BFS o DFS per trovare tutta la componente
        queue = deque([node])
        comp = []
        visited.add(node)
        
        while queue:
            cur = queue.popleft()
            comp.append(cur)
            for nei in graph[cur]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        
        components.append(comp)

m = 1
c = 0
for comp in sorted(components, key=len, reverse=True):
    m *= len(comp)
    c += 1
    if c >= TOP_CONN: break
print(m)

#Part-2 
print("--- Part 2 ---")

# Disjoint Set Union
#
#   Tiene traccia di insieme disgiunti e fornisce operazioni quali:
#       - find
#       - union
#
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[rb] = ra
        self.components -= 1
        return True


dsu = DSU(len(points))
last_connector = None
for a, b in sorted(distances, key=distances.get):
    if dsu.union(a, b):
        # Questa unione ha ridotto il numero di componenti
        if dsu.components == 1:
            last_connector = (a, b)
            break

print(points[last_connector[0]].x * points[last_connector[1]].x)