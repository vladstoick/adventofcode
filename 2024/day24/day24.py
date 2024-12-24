from pathlib import Path
import regex as re
import networkx as nx
from networkx import *
import matplotlib.pyplot as plt

file = open(Path(__file__).with_name("input.txt"))
values = dict([])
operations = dict([])

graph = nx.DiGraph()
op = 0

for line in file.readlines():
    line = line.strip()
    if line.count(":"):
        l, r = line.split(": ")
        values[l] = int(r)
        graph.add_node(l)
    elif line.count("->"):
        matches = re.findall(r"(...) (AND|XOR|OR) (...) -> (...)", line)
        oper = matches[0][1] + str(op)
        operations[oper] = line
        op += 1

        graph.add_node(oper)
        graph.add_edge(matches[0][0], oper)
        graph.add_edge(matches[0][2], oper)
        graph.add_edge(oper, matches[0][3])

topo = list(nx.topological_sort(graph))
positions = {node: (i, 0) for i, node in enumerate(topo)}

for op in topo:
    if not (op.count("AND") or op.count("OR")):
        continue

    operation = re.findall(
        r"(...) (AND|XOR|OR) (...) -> (...)", operations[op])[0]
    val1 = values[operation[0]]
    val2 = values[operation[2]]
    new_val = 0
    if operation[1] == 'AND':
        new_val = val1 & val2
    elif operation[1] == 'XOR':
        new_val = val1 ^ val2
    elif operation[1] == 'OR':
        new_val = val1 | val2
    values[operation[3]] = new_val

z_values = ""

sorted_keys = sorted(list(values.keys()))
for key in sorted_keys:
    if key.startswith('z'):
        z_values += "1" if values[key] else "0"

z_values = z_values[::-1]

print("Part 1", z_values, int(z_values, 2))
