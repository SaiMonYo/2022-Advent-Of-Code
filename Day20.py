from utils import *

with open("Day20.txt") as file:
    raw = file.read()
    nums = ints(raw)

def solve(data, part = 1):
    # use indexes instead of data to account for duplicates
    indexes = list(range(len(data)))
    # multiply by encoding number for p2
    data = [x * 811589153 if part == 2 else x for x in data]
    # do 10 times for p2, 1 time for p1
    for _ in range(10 if part == 2 else 1):
        for i,x in enumerate(data):
            ind = indexes.index(i)
            # remove and reinsert
            indexes.pop(ind)
            indexes.insert((ind+x)%len(indexes), i)

    # zero index
    z = indexes.index(data.index(0))
    a = data[indexes[(z+1000)%len(indexes)]]
    b = data[indexes[(z+2000)%len(indexes)]]
    c = data[indexes[(z+3000)%len(indexes)]]
    print(a+b+c)

solve(nums[:], 1)
solve(nums[:], 2)