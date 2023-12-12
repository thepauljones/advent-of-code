from pathlib import Path
from collections import defaultdict

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = [
    (
        y.split(" ")[0],
        [int(z) for z in y.split(" ")[1].split(",")],
    )
    for y in [x for x in file.read().splitlines()]
]


def get_count_groups(pattern):
    isGroup = False
    result = []

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


assert get_count_groups("###.###") == [3, 3]
assert get_count_groups("##..###") == [2, 3]
assert get_count_groups("#.#.###") == [1, 1, 3]
assert get_count_groups("#...###") == [1, 3]
assert get_count_groups(".##.###") == [2, 3]
assert get_count_groups(".#..###") == [1, 3]
assert get_count_groups("..#.###") == [1, 3]
assert get_count_groups("....###") == [3]


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
    print("P", pattern, groups)

    result = 0
    for poss in replacements("".join(pattern)):
        r = get_count_groups(poss)

        if len(r) > len(groups):
            continue

        if r[: len(groups)] == groups:
            print(poss)
            result += 1

    results.append(result)

print(results)
print(sum(results))
