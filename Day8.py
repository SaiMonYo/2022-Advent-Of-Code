from utils import *


raw = open("Day8.txt").read()

g = [[int(c) for c in line] for line in raw.split("\n")]

# functions to get row and column
getrow = lambda i: g[i]
getcol = lambda i: [r[i] for r in g]

# visible trees
vis = set()

# visible left to right
for j in range(len(g)):
    # biggest left and right tree seen so far
    bl = -1
    br = -1
    r = getrow(j)
    for i in range(len(r)):
        # current left and right tree
        nl, nr = r[i], r[len(r)-i-1]
        # if bigger than biggest seen so far, add to visible
        # and update biggest seen so far
        if nl > bl:
            vis.add((i, j))
            bl = nl
        if nr > br:
            vis.add((len(r)-i-1, j))
            br = nr

# visible top to bottom
for j in range(len(g[0])):
    bt = -1
    bb = -1
    c = getcol(j)
    for i in range(len(c)):
        # same as above
        nt, nb = c[i], c[len(r)-i-1]
        if nt > bt:
            vis.add((j, i))
            bt = nt
        if nb > bb:
            vis.add((j, len(c)-i-1))
            bb = nb
print(len(vis))

mscore = 0
# for each tree, find the number of trees visible from it
for j in range(len(g)):
    for i in range(len(g[0])):
        row = getrow(j)
        col = getcol(i)
        score = 1
        dist = 0
        # left
        for k in range(i-1, -1, -1):
            dist += 1
            if row[k] >= row[i]:
                break
        score *= dist
        dist = 0
        # right
        for k in range(i+1, len(row)):
            dist += 1
            if row[k] >= row[i]:
                break
        score *= dist
        dist = 0
        # up
        for k in range(j-1, -1, -1):
            dist += 1
            if col[k] >= col[j]:
                break
        score *= dist
        dist = 0
        # down
        for k in range(j+1, len(col)):
            dist += 1
            if col[k] >= col[j]:
                break
        score *= dist
        mscore = max(mscore, score)
print(mscore)

