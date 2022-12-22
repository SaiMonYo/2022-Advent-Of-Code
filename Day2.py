with open("Day2.txt") as file:
    raw = file.read()
    lines = raw.split("\n")



ap = {"A": 0, "B": 1, "C": 2}
bp = {"X": 0, "Y": 1, "Z": 2}

#   bm    add % 3     add
#    0     am -1       1
#    1     am          4
#    2     am + 1      7

score1, score2 = 0, 0
for line in lines:
    a, b = line.split(" ")
    am, bm = ap[a], bp[b]
    score1 += bm + 1 + ((bm-am + 1) % 3) * 3
    score2 += 1 + 3 * bm + (am + bm - 1) % 3

print(score1)
print(score2)


print(sum(map(lambda t:t[1]+1+((t[1]-t[0]+1)%3)*3,
d:=[[(ord(b)-65)%23 for b in l.strip().split(" ")] for l in open("Day2.txt")])),
sum(map(lambda t:1+3*t[1]+(t[0]+t[1]-1)%3,d)))

