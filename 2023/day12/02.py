from pathlib import Path
from collections import defaultdict

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = [
    (
        y.split(" ")[0],
        [int(z) for z in y.split(" ")[1].split(",")],
    )
    for y in [x for x in file.read().splitlines()]
]

expanded = []


def map_springs(line):
    m, groups = line
    result = [(m + "?") * 5, groups * 5]
    print(result)
    return result


data = list(map(map_springs, data))

print(data)

map = {}


def get_count_groups(pattern):
    isGroup = False
    result = []

    if pattern in map:
        return map[pattern]

    groupStart = 0
    for i, char in enumerate(pattern):
        if isGroup is not True and char == "#":
            isGroup = True
            groupStart = i

        if isGroup and char != "#":
            result.append(i - groupStart)
            isGroup = False

        if i == len(pattern) - 1 and isGroup:
            result.append(i - groupStart + 1)

    return result


def replacements(pattern):
    if pattern == "":
        return [""]

    return [
        x + y
        for x in ("#." if pattern[0] == "?" else pattern[0])
        for y in replacements(pattern[1:])
    ]


def default_value():
    return 0


results = []
for springs in data:
    pattern, groups = springs

    result = 0
    for poss in replacements("".join(pattern)):
        r = get_count_groups(poss)

        if len(r) > len(groups):
            continue

        if r[: len(groups)] == groups:
            result += 1

    results.append(result)

print(results)
print(sum(results))
