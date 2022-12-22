from utils import *

with open("Day5.txt") as file:
    # input parsing
    raw = file.read()
    parts = raw.split("\n\n")
    lines = ints(parts[1], 3)
    blocks = [[] for _ in range(9)]
    for line in parts[0].split("\n")[:-1]:
        for i in range(9):
            # go through each letter block
            if i * 4 + 1 < len(line) and line[i * 4 + 1] != ' ':
                blocks[i].append(line[i * 4 + 1])
    # make a copy of the blocks
    blocks = [list(reversed(s)) for s in blocks]
    blocks2 = [s.copy() for s in blocks]


for n,start,stop  in lines:
    # reversed as takes 1 by 1
    blocks[stop-1] += blocks[start-1][-n:][::-1]
    blocks[start-1] = blocks[start-1][0:-n]
    # normal as takes all at once
    blocks2[stop-1] += blocks2[start-1][-n:]
    blocks2[start-1] = blocks2[start-1][0:-n]

print("".join(c[-1] for c in blocks if len(c)))
print("".join(c[-1] for c in blocks2 if len(c)))