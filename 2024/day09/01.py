from pathlib import Path
from functools import cache
from itertools import chain
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.read().strip()

things = []
for i, ins in enumerate(data):
    items = []
    if ins == "0":
        continue
    if i % 2 == 0:
        while len(items) < int(ins):
            items.append(str(int(i / 2)))
        things.append(items)
    else:
        while len(items) < int(ins):
            items.append(".")
        things.append(items)

# flatten 2d array
output = list(chain.from_iterable(things))


without = []
for char in output:
    if char != ".":
        without.append(char)


assert(len(output) - len(without) == output.count("."))

string = []
for i, char in enumerate(output):
    if not "." in output[i + 1:]:
        break

    if char == ".":
        string.append(without.pop())
    else:
        string.append(char)

    if len(string) == len(output) - output.count("."):
        break

assert(len(string) == len(output) - output.count("."))

print(output)
print(string)

ans = 0
for i, part in enumerate(string):
    ans += i * int(part)

print(ans)

