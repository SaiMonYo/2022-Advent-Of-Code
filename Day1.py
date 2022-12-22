from utils import *


with open("Day1.txt") as file:
    raw = file.read()
    # ints gets all integers in a string
    data = [sum(ints(n)) for n in raw.split("\n\n")]

data = sorted(data, reverse=True)
# p1 and p2
print(data[0])
print(sum(n for n in data[:3]))