from collections import defaultdict
import math
from pathlib import Path
import queue
from networkx.utils import UnionFind

p = Path(__file__).with_name("input.txt")
file = open(p)

lines = [line for line in file.readlines() if line.strip()]

positions = []
distances = []

for line in lines:
    x, y, z = map(int, line.split(","))
    positions.append((x, y, z))

for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
        x1, y1, z1 = positions[i]
        x2, y2, z2 = positions[j]
        distance =  math.dist((x1, y1, z1), (x2, y2, z2))
        distances.append((distance, i, j))
        
distances = sorted(distances, key = lambda item: item[0])

parents = [None for x in range(len(positions))]

ITERS = 1000
edges = defaultdict(lambda: [])
for iter in range(ITERS):
    dist, i, j = distances[iter]
    edges[i].append(j)
    edges[j].append(i)
    

visited = set()

comp_zises = []

for i in range(len(positions)):
    if i not in visited and len(edges[i]) > 0:        
        q = queue.Queue()
        q.put(i)
        
        comp_size = 0
        visited.add(i)
        
        while not q.empty():
            item = q.get()
            comp_size += 1
            
            for edge in edges[item]:
                if edge not in visited:
                    q.put(edge)
                    visited.add(edge)
                    
            q.task_done()
            
        comp_zises.append(comp_size)
    
comp_zises = sorted(comp_zises, reverse=True)

print("Part 1", comp_zises[0] * comp_zises[1] * comp_zises[2])
            
uf = UnionFind(range(len(positions)))

for _, i, j in distances:
    uf.union(i, j)
    num_components = len({uf[x] for x in range(len(positions))})
    if num_components == 1:
        print("Part 2", positions[i][0] * positions[j][0])
        break