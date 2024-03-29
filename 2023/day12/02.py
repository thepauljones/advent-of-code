from pathlib import Path
from tqdm import tqdm
from functools import cache

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = [
    (
        y.split(" ")[0],
        tuple([int(z) for z in y.split(" ")[1].split(",")]),
    )
    for y in [x for x in file.read().splitlines()]
]


def expand_input(line):
    m, groups = line
    result = [(m + "?" + m + "?" + m + "?" + m + "?" + m), groups * 5]
    return result


# data = list(map(expand_input, data))


def fits(pattern, groups, i, groupI, currentBlockLength):
    ans = 0
    if pattern[i] == "?":
        for char in ".#":
            ans += fits(
                char + "".join(pattern[1:]), groups, i + 1, groupI, currentBlockLength
            )

    if pattern[i] == "#":
        if currentBlockLength == groups[groupI]:
            print("ANUS")
            print("ANAsL", currentBlockLength, groups, groupI, groups[groupI])
            return fits(pattern, groups, i + 1, groupI + 1, 0)
        else:
            print("ANAL", currentBlockLength, groups, groupI, groups[groupI])
            return fits(pattern, groups, i + 1, groupI, currentBlockLength + 1)

    if pattern[i] == ".":
        print("oh my hemel")
        return fits(pattern, groups, i + 1, groupI, 0)

    return ans


ans = 0
for i in tqdm(range(len(data))):
    line = data[i]
    (
        p,
        g,
    ) = line
    ans += fits(p, g, 0, 0, 0)

print(ans)
