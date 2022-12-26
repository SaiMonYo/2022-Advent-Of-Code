from utils import *

with open("Day23.txt") as f:
    lines = f.read().split("\n")


# parse input into set
elves = set()
for y, row in enumerate(lines):
    for x, char in enumerate(row):
        if char == "#":
            elves.add((x, y))

# starting directions to check
# with the moving direction in the middle
dirs = [[NE, N, NW], [SE, S,  SW], [NW, W, SW], [NE, E, SE]]
round = 1
while True:
    # tuple: tuple -> startpos to endpos
    moves = {}
    # tuple: int -> how many elves will move to that position
    movecount = {}
    for x, y in elves:
        # check if all of the 8 directions are free
        if all((x + dx, y + dy) not in elves for dx, dy in [N, NE, NW, S, SE, SW, W, E]):
            # keep elf where it is
            continue
        for d in dirs:
            # check if all three in d direction are free
            if all((x + dx, y + dy) not in elves for dx, dy in d):
                # move
                endup = (x+d[1][0], y+d[1][1])
                # update dicts
                moves[(x, y)] = endup
                if endup in movecount:
                    movecount[endup] += 1
                else:
                    movecount[endup] = 1
                break
    # p2
    if len(moves) == 0:
        print(round)
        break       
    for move in moves:
        if movecount[moves[move]] == 1:
            elves ^= {moves[move], move}
    # move first direction to end
    dirs = dirs[1:] + [dirs[0]] 
    # p1 done
    if round == 10:
        # calulate area
        minx = min([x for x, y in elves])
        maxx = max([x for x, y in elves])
        miny = min([y for x, y in elves])
        maxy = max([y for x, y in elves])

        area = (maxx - minx + 1) * (maxy - miny  + 1)
        # there will be len(elves) occupying space
        area -= len(elves)
        print(area)
    round += 1