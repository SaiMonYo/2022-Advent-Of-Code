from utils import *

with open("Day22.txt") as f:
    chunks = f.read().split("\n\n")

lines = chunks[0].split("\n")

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
conv = {"R": 1, "L": -1}
facing = 0

instructions = chunks[1]
pd = []
nums = ints(instructions)
ind = 0
for c in instructions:
    # add number
    if ind % 2 == 0:
        pd.append(nums[ind // 2])
        ind += 1
    # add direction
    if c in "RL":
        pd.append(c)
        ind += 1

# parse the grid
grid = {(i,j): c for j, line in enumerate(lines) for i, c in enumerate(line) if c in ".#"}


x = 0
y = 0
# find starting position
for i in range(10000):
    if (i, y) in grid:
        if grid[(i, y)] == ".":
            x = i
            break


for d in pd:
    if type(d) == int:
        dx = directions[facing][0]
        dy = directions[facing][1]
        for i in range(d):
            newx = x + dx
            newy = y + dy
            # not wrapping
            if (newx, newy) in grid:
                # empty space continue
                if grid[(newx, newy)] == ".":
                    x = newx
                    y = newy
                # hit a wall, stop moving
                elif grid[(newx, newy)] == "#":
                    break
            # wrapping
            else:
                tx = x
                ty = y
                # keep moving backwards until edge of grid
                while (tx-dx, ty-dy) in grid:
                    tx -= dx
                    ty -= dy
                # if empty space, move there
                # otherwise stay where we are
                if grid[(tx, ty)] == ".":
                    x = tx
                    y = ty
    # turn
    else:
        facing = (facing + conv[d]) % 4

print(1000 * (y+1) + 4 * (x+1) + facing)

facing = 0
y = 0

# find starting position
for i in range(10000):
    if (i, y) in grid:
        if grid[(i, y)] == ".":
            x = i
            break

def square_in(x, y):
    '''
      1100
      1100
      22
      22
    4433
    4433
    55
    55
    '''
    if 0 <= y < 50:
        if 50 <= x < 100:
            return 1
        return 0
    elif 50 <= y < 100:
        return 2
    elif 100 <= y < 150:
        if 0 <= x < 50:
            return 4
        return 3
    print(x, y)
    return 5



for d in pd:
    if type(d) == int:
        for j in range(d):
            oldx, oldy, oldf = x, y, facing
            x += directions[facing][0]
            y += directions[facing][1]
            # need to wrap
            # (hardcoded for this problem)
            if (x, y) not in grid:
                match facing:
                    # right 
                    case 0:
                        match y // 50:
                            # 0 -> 3
                            case 0:
                                x = 99
                                y = 149 - y
                                facing = 2
                            # 2 -> 0
                            case 1:
                                x = y + 50
                                y = 49
                                facing = 3
                            # 3 -> 0
                            case 2:
                                x = 149
                                y = 149 - y
                                facing = 2
                            # 5 -> 3
                            case 3:
                                x = y - 100
                                y = 149
                                facing = 3
                    # down
                    case 1:
                        match x // 50:
                            # 5 -> 0
                            case 0:
                                x = x + 100
                                y = 0
                                facing = 1
                            # 3 -> 5
                            case 1:
                                y = x + 100
                                x = 49
                                facing = 2
                            # 0 -> 2
                            case 2:
                                y = x - 50
                                x = 99
                                facing = 2
                    # left
                    case 2:
                        match y // 50:
                            # 1 -> 4
                            case 0:
                                x = 0
                                y = 149 - y
                                facing = 0
                            # 2 -> 4
                            case 1:
                                x = y - 50
                                y = 100
                                facing = 1
                            # 4 -> 1
                            case 2:
                                x = 50
                                y = 149 - y
                                facing = 0
                            # 5 -> 1
                            case 3:
                                x = y - 100
                                y = 0
                                facing = 1
                    # up
                    case 3:
                        match x // 50:
                            # 4 -> 2
                            case 0:
                                y = x + 50
                                x = 50
                                facing = 0
                            # 1 -> 5
                            case 1:
                                y = x + 100
                                x = 0
                                facing = 0
                            # 0 ->  5
                            case 2:
                                x = x - 100
                                y = 199
                                facing = 3
            # found a wall resest to old position
            # stop moving in this direction
            if grid[(x,y)] == '#':
                x = oldx
                y = oldy
                facing = oldf 
                break
    else:
        # update facing
        facing = (facing + conv[d]) % 4

print(1000 * (y+1) + 4 * (x+1) + facing)