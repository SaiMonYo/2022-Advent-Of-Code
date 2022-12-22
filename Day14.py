from utils import *

with open("day14.txt") as f:
    inpt = [[list(map(int, j.split(","))) for j in i.split(" -> ")] for i in f.read().split("\n")]

walls = set()

for w in inpt:
    for i in range(len(w) - 1):
        start = w[i]
        end = w[i + 1]
        if start[0] == end[0]:
            for y in wacky_range_inc(start[1], end[1]):
                walls.add((start[0], y))
        else:
            for x in wacky_range_inc(start[0], end[0]):
                walls.add((x, start[1]))

max_depth = max(map(lambda a: a[1], walls))

# Part 1
sand_location = (500, 0)
sands = set()

# keep track of where sands been
# the next piece of sand will fall to atleast the last touched
touched = []
# gone past all walls
while sand_location[1] <= max_depth:
    # try adding in this order
    for x, y in ((0, 1), (-1, 1), (1, 1)):
        temp = sand_location[0] + x, sand_location[1] + y
        if temp not in walls and temp not in sands:
            # add to touched
            touched += [temp]
            sand_location = temp
            break
    else:
        # hit a wall or sand
        sands.add(sand_location)
        sand_location = touched.pop()
print(len(sands))


# Part 2
sands = set()
sand_location = (500, 0)
touched = [(500, 0)]
while (500, 0) not in sands:
    for x, y in ((0, 1), (-1, 1), (1, 1)):
        temp = sand_location[0] + x, sand_location[1] + y
        # not in walls or sand and not gone below the floor
        if temp not in walls and temp not in sands and temp[1] < max_depth + 2:
            touched += [temp]
            sand_location = temp
            break
    else:
        sands.add(sand_location)
        # multiple can reach back to start
        if len(touched) != 0:
            sand_location = touched.pop()
        else:
            sand_location = (500, 0)
print(len(sands))