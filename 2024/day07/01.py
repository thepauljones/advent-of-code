from pathlib import Path
import re
import math
from itertools import product

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.read().splitlines()

items = []

for line in data:
    result, parts = line.split(":")
    items.append((int(result), list(map(int, parts.strip().split(" ")))))

def check_sum(value, eq, orig):
    things = eq.split(",")
    if len(things) <= 1:
        if int(things.pop(0)) == value:
            print("Found", value, "with", orig.split(","))
            return True, value
        else:
            return False, value

    a = things.pop(0)
    o = things.pop(0)
    b = things.pop(0)

    if o == "*":
        sum = int(a) * int(b)

        things.insert(0, str(sum))
        return check_sum(value, ",".join(things), orig)

    if o == "+":
        sum = int(a) + int(b)
        if sum == value:
            print("Found", value, "with", orig.split(","))
            return True, value

        things.insert(0, str(sum))
        return check_sum(value, ",".join(things), orig)

    return False, value
        

def test(value, parts, operators):
    eq = []
    if len(parts) == 1:
        if parts[0] == value:
            return True, value
        else:
            return False, value

    for i in range(len(parts)):
        eq.append(str(parts[i]))
        if i != len(parts) - 1:
            eq.append(operators[i])

    return check_sum(value, ",".join(eq), ",".join(eq))

def get_permutations(n):
    chars = ['*', '+']
    permutations = [''.join(p) for p in product(chars, repeat=n)]
    result = list(set(list(sorted(permutations))))
    return result

def test_parts_for_value(value, parts):
    perms = get_permutations(len(parts))
    for perm in perms:
        res, value = test(value, parts, perm)
        if res == True:
            return True, value
            break

    return False, value


good = []
bad = []
for t in items:
    res, val = test_parts_for_value(t[0], t[1])
    if res != False:
        good.append(val)
    else:
        bad.append(val)


answer = 0
for g in good:
    answer += g
print(answer)

print(sum(good))
print(good)
