with open("Day7.txt") as file:
    lines = file.read().split("\n")

# parsing
d, x, y = ['/'], {}, []
# start 1: as already got '/'
for i in lines[1:]:
    if i[0] == '$':
        if y:
            # convert to tuple as hashable
            x[tuple(d)] = y
            y=[]
        if i[2:4]=='cd':
            # move up dir
            if i[5:] == '..':
                d.pop()
            # move down dir
            else:
                d.append(i[5:])
        else:
            y=[]
    else:
        y.append(tuple(i.split()))
# might still have y
if y:
    x[tuple(d)] = y

# flatten the dir tree
def flatten(start):
    ret = 0
    for i in x[start]:
        if i[0] == "dir":
            ret += flatten(start + (i[1],))
        else:
            ret += int(i[0])
    return ret

# sum of all dirs
s = {p:flatten(p) for p in x}
# print number of dirs < 100,000
print(sum(s[v] for v in s if s[v] < 100_000))
# print min of all dirs greater than required
required = flatten(('/',)) - 40_000_000
print(min(min(s[i] for i in x if s[i] >= required), 70_000_000))


ls=[*open("Day7.txt")]
d,x,y=['/'],{},[]
for i in ls[1:]:
    i=i.strip()
    if i[0]=='$':
        if y:x[tuple(d)]=y;y=[]
        if i[2:4]=='cd':d.pop()if i[5:]=='..'else d.append(i[5:])
        else:y=[]
    else:y.append(tuple(i.split()))
x[tuple(d)]=y if y else[]
m=lambda start:sum(m(start+(i[1],))if i[0]=="dir"else int(i[0])for i in x[start])
s={p:m(p)for p in x}
print(sum(s[v]for v in s if s[v]<1e5))
print(min(min(s[i]for i in x if s[i]>=-4e7+m(('/',))),7e6))