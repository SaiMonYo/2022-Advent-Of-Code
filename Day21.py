from utils import *

with open("Day21.txt") as f:
    lines = f.read().split("\n")

locals = {}

# hacky solution
while "root" not in locals:
    for line in lines:
        # rhs variables not defined yet
        try:
            exec(line.replace(": ", " = "), None, locals)
        except:
            pass
print(locals["root"])


def solve(eq):
    parts = monkeys[eq]
    if len(parts) == 1:
        return parts[0]

    a, op, b = parts
    return "(" + solve(a) + op + solve(b) + ")"

def evalify(eq):
    nums = floats(eq)
    if len(nums) == 1:
        return nums[0]
    op = ""
    for i, char in enumerate(eq):
        if char in "+-*/" and eq[i-1].isdigit():
            op = char
            break
    # prevent op from being - when nums[1] is negative
    if nums[1] < 0 and op == "-":
        op = "+"
    match op:
        case "*":
            return nums[0] * nums[1]
        case "/":
            return nums[0] / nums[1]
        case "+":
            return nums[0] + nums[1]
        case "-":
            return nums[0] - nums[1]
    

# (num op num) match
reducer = re.compile(r"\(([-+]?\d+(?:\+|\*|\/|\-|)-?\d+)\)")
def reduce(eq):
    # continue until no more matches
    while True:
        cont = False
        # simplify all matches
        for match in re.finditer(reducer, eq):
            eq = eq.replace(match.group(), str(int(evalify(match.group()))))
            cont = True
        if not cont:
            break
    return eq
        

monkeys = {}
for line in lines:
    a, b = line.split(": ")
    monkeys[a] = b.split(" ")

# monkeys humn should be a variable like x
# but to make it work in python we use complex numbers
# and the imaginary part is the variable
monkeys["humn"] = ["-1j"]
monkeys["root"][1] = "-("

result = eval(solve("root") + ")")
# does not need reducing but can be done
#print(reduce(solve("root") + ")"))
print(int(result.real / result.imag))