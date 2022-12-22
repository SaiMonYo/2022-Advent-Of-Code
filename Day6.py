with open("Day6.txt") as file:
    lines = file.read().split("\n")

def solve(n):
    p = 0
    for line in lines:
        for i in range(len(line)-n):
            # find first n unique letters
            if len(set(line[i:i+n])) == n:
                p += i+n
                break
    return p

print(solve(4))
print(solve(14))
