with open("Day13.txt") as f:
    chunks = f.read().split("\n\n")

p1 = 0
p2 = 1

class T:
    def __init__(self, x):
        self.x = x
    
    def __lt__(self, other):
        return compare(self.x, other.x) == -1
    
    def __repr__(self):
        return str(self.x)

def compare(a,b):
    at = type(a)
    bt = type(b)
    if at == int and bt == int:
        return (a > b) - (a < b)
    elif at == list and bt == list:
        i = 0
        # compare each element
        while i < len(a) and i < len(b):
            c = compare(a[i], b[i])
            # if they are not equal, return the result
            if c:
                return c
            i += 1
        # if one list is longer than the other, return the result
        if i == len(a) and i < len(b):
            return -1
        elif i==len(b) and i<len(a):
            return 1
        # if they are equal, return 0
        else:
            return 0
    # if one is a list and the other is an int, convert the int to a list
    elif at == int and bt == list:
        return compare([a], b)
    else:
        return compare(a, [b])

data = []
for i, chunk in enumerate(chunks):
    # convert the string list to python list
    a, b = eval(chunk.replace("\n", ","))
    # a < b
    if compare(a, b) == -1:
        p1 += 1 + i
    data += [a, b]

# add the two divider packets
packets = data + [[[2]]] + [[[6]]]
# convert to custom class to allow comparison
packets = [T(p) for p in packets]
for i, p in enumerate(sorted(packets)):
    # if the packet is a divider packet, multiply the result by the index
    if p.x == [[2]] or p.x == [[6]]:
        p2 *= i + 1


print(p1, p2)