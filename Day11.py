from utils import *
from copy import deepcopy


def solve(monkeys, part):
    # the worry levels grow too big without // 3
    # but we only need to keep track of the worry in regard to modulo
    modmod = 1
    for monkey in monkeys:
        modmod = modmod * monkey.mod

    for _ in range(20 if part == 1 else 10_000):
        for monkey in monkeys:
            rem = []
            # map the operation to the items
            monkey.items = list(map(monkey.op, monkey.items))
            for i in range(len(monkey.items)):
                # reduce by // 3 if part 1 or % modmod if part 2
                monkey.items[i] = monkey.items[i] // 3 if part == 1 else monkey.items[i] % modmod
                # send item to correct monkey
                if monkey.items[i] % monkey.mod == 0:
                    monkeys[monkey.true].items.append(monkey.items[i])
                    rem += [i]
                else:
                    monkeys[monkey.false].items.append(monkey.items[i])
                    rem += [i]
                monkey.count += 1
            # remove items that were sent to other monkeys
            monkey.items = [monkey.items[i] for i in range(len(monkey.items)) if i not in rem]
    # return the max of the counts of the monkeys
    cs = [monkey.count for monkey in monkeys]
    cs = sorted(cs, reverse = True)

    return cs[0] * cs[1]

class Monkey:
    def __init__(self, block):
        ls = block.split("\n")
        self.items = ints(ls[1])
        # old count, only had old * old not old + old
        oldc = ls[2].count("old")
        if oldc == 2:
            self.op = lambda x: x*x
        elif oldc == 1:
            m = ls[2].count("*")
            i = ints(ls[2])[0]
            # multiply or add
            if m == 1:
                self.op = lambda x: x*i
            else:
                self.op = lambda x: x+i
        self.mod = ints(ls[3])[0]
        self.true = ints(ls[4])[0]
        self.false = ints(ls[5])[0]
        self.count = 0


with open("Day11.txt") as f:
    raw = f.read()
    lines = raw.split("\n")
    data = ints(raw)

ms = []
for ch in raw.split("\n\n"):
    ms.append(Monkey(ch))

# copy the monkeys
print(solve(deepcopy(ms), 1))
print(solve(ms, 2))