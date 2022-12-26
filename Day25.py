with open("Day25.txt") as f:
    raw = f.read()
    lines = raw.splitlines()

p1 = 0

def rev(n):
    ret = ''
    while n:
        match n % 5:
            case 0:
                ret += '0'
                n //= 5
            case 1:
                ret += '1'
                n //= 5
            case 2:
                ret += '2'
                n //= 5
            case 3:
                ret += '='
                # need to add 2 to get to next multiple of 5
                n = (n+2) // 5
            case 4:
                ret += '-'
                # need to add 1 to get to next multiple of 5
                n = (n+1) // 5
    # reverse the number
    return ret[::-1]

conv = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}

for line in lines:
    # convert from snafu
    parts = [conv[c] for c in line]
    ss = 0
    # want to do units part first
    # ss = sum(c * 5 ** i for i, c in enumerate(reversed(parts)))
    for i, c in enumerate(reversed(parts)):
        ss += c * 5 ** i
    p1 += ss

print(rev(p1))