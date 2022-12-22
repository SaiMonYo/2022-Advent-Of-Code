from utils import *

# accumulate the list
def acc(a):
    for i in range(1, len(a)):
        a[i] += a[i-1]
        yield a[i-1]

with open("Day10.txt") as f:
    values = []
    for line in f.read().split("\n"):
        # 0s added for cycles
        if line != "noop":
            values += [0, int(line[5:])]
        else:
            values.append(0)
    #values = [[0, int(line[5:])] if line != "noop" else [0] for line in f.read().split("\n")]
    #values = [c for val in values for c in val]

part1, part2 = 0, ''
for i, x in enumerate(acc([1]+values), 1):
    if i%40==20:
        part1 += i*x
    part2 += '██' if (i-1)%40-x in [-1,0,1] else '  '
    part2 += '\n' if i%40==0 else ''

print(part2, part1)

