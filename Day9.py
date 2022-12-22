from utils import *

with open("Day9.txt", "r") as file:
    raw = file.read()
    data = ints(raw)
    lines = raw.split("\n")


# head x, y coords
xh = 0
yh = 0

# tail x, y coords
yt = 0
xt = 0

offset = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

visited = set()
for i, line in enumerate(lines):
    d, n = line.split(" ")
    off = offset[d]
    for _ in range(int(n)):
        xh += off[0]
        yh += off[1]
        # moved to far left or right
        if (abs(xh-xt) > 1):
            xt = xh - 1 if xh > xt else xh + 1
            yt = yh
        # moved to far up or down
        if (abs(yh-yt) > 1):
            yt = yh - 1 if yh > yt else yh + 1
            xt = xh
        visited.add((xt, yt))
print(len(visited))


visited = set()

rope = [(0,0) for _ in range(10)]
for line in lines:
    d, n = line.split(" ")
    off = offset[d]
    for _ in range(int(n)):
        xh, yh = rope[0]
        rope[0] = (xh + off[0], yh + off[1])
        # same as p1 but i-1 is head and i is tail
        for i in range(1, 10):
            xc, yc = rope[i-1]
            xi, yi = rope[i]
            if abs(xi-xc) > 1:
                xi = xc - 1 if xc > xi else xc + 1
                yi = yc
            if abs(yi-yc) > 1:
                yi = yc - 1 if yc > yi else yc + 1
                xi = xc
            rope[i] = (xi, yi)
        visited.add(rope[-1])
print(len(visited))