from pathlib import Path
from collections import defaultdict

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.read().splitlines()

seeds = [int(x) for x in data[0].split(": ")[1].split(" ")]

rawMaps = data[2:]

maps = defaultdict(list)

digits = "0123456789"
currentMap = ""

allTypes = ["seed"]

for line in rawMaps:
    rawName = line.split(" ")[0]

    if len(line) == 0:
        currentMap = ""
        continue

    # get the name of the map
    if line[0] not in digits:
        currentMap = rawName.split("-to-")
        allTypes.append(currentMap[1])
        continue

    sourceDestinationRange = [int(x) for x in line.split(" ")]
    maps[">".join(currentMap)].append(sourceDestinationRange)

for seed in seeds:
    current = maps["seed" + ">soil"]
    for m in current:
        source, dest, r = m

        count = 1
        mappedValue = seed
        if seed in range(source, source + r):
            count += 1
            mappedValue = seed + count

    print("seed: ", seed, mappedValue)


def solve():
    print(seeds)


solve()
