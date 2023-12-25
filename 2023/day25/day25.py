from pathlib import Path
import queue
import networkx as nx

p = Path(__file__).with_name("input.txt")

G = nx.Graph()

graph = {}
for line in open(p).read().splitlines():
    [elem, rest] = line.split(": ")
    connections = rest.split(" ")
    for connection in connections:
        G.add_edge(elem, connection)

cut_value, partition = nx.stoer_wagner(G)
print("Part 1", len(partition[0]) * len(partition[1]))
