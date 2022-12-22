from utils import *

# pints splits the line into a list of positive ints width 4
ranges = pints(open("Day4.txt").read(), 4)

p1 = 0
p2 = 0

for a, b, c, d in ranges:
    ab = set(range(a, b + 1))
    cd = set(range(c, d + 1))
    # any number in the other range
    p1 += ab <= cd or cd <= ab
    # entire range is in the other range
    if ab & cd:
        p2 += 1
print(p1, p2)


print(sum((a<=c<=d<=b or c<=a<=b<=d)+1j*(a<=d>=c<=b)
for a,b,c,d in[map(int, l.replace("-", ",").split(","))for l in open('Day4.txt')]))


