from networkx import DiGraph, shortest_path
from utils import *

raw = open("Day12.txt").read()
# find start and end
S = raw.find("S")
E = raw.find("E")
raw = raw.replace("S", "a").replace("E", "z")

# convert to grid with numbers
g = [[ord(c)-97 for c in line] for line in raw.split("\n")]

# account for "\n"
sx, sy = S % (len(g[0]) + 1), S // (len(g[0])+1)
tx, ty = E % (len(g[0]) + 1), E // (len(g[0])+1)

dij = DiGraph()

for y in range(len(g)):
    for x in range(len(g[0])):
        for dir in cardinals:
            nx = x + dir[0]
            ny = y + dir[1]
            # valid position
            if nx in range(len(g[0])) and ny in range(len(g)):
                a = g[y][x]
                b = g[ny][nx]
                # edge in the graph
                if a+1 >= b:
                    dij.add_edge((x, y), (nx, ny))

p = shortest_path(dij, (sx, sy), (tx, ty))
# assuming we already went from the minimum "a" to the end
for i, (x, y) in enumerate(p):
    if g[y][x] == 0:
        d = i
print(len(p) - 1)
print(len(p) - 1 - d)

mm = 9999e100
# try all starts with "a"
for y in range(len(g)):
    for x in range(len(g[0])):
        if g[y][x] == 0:
            # might not be possible
            try:
                mm = min(mm, len(shortest_path(dij, (x, y), (tx, ty))) - 1)
            except:
                pass
            
print(mm)
