with open("Day3.txt") as file:
    lines = file.read().split("\n")


p1 = 0
p2 = 0



for i, line in enumerate(lines):
    a, b =  line[len(line)//2:], line[:len(line)//2]
    # find the intersection of a and b
    # -96) % 58 gets priority
    p1 += (ord(list(set(a) & (set(b)))[0])-96)%58

for x, y, z in zip(lines[::3], lines[1::3], lines[2::3]):
    # find the intersection of the 3 lines
    # -96) % 58 gets priority
    p2 += (ord(list((set(x) & (set(y))) & (set(z)))[0])-96)%58


print(p1)
print(p2)

ls = open("Day3.txt").read().split("\n")
print(sum(map(lambda t: (ord(list(set(t[0])&(set(t[1])))[0])-96)%58,[(l[:len(l)//2],l[len(l)//2:]) for l in ls])))
print(sum(map(lambda t: (ord(list((set(t[0])&(set(t[1])))&(set(t[2])))[0])-96)%58, [p for p in zip(ls[::3],ls[1::3], ls[2::3])])))
