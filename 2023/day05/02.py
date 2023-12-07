from pathlib import Path
from collections import defaultdict

script_location = Path(__file__).absolute().parent
file_location = script_location / "input.txt"
file = file_location.open()

data = file.read().splitlines()

seeds = [int(x) for x in data[0].split(": ")[1].split(" ")]

seedPairs = []

p = 0

startingBrute = float("inf")

while p < len(seeds) - 1:
    if seeds[p] < startingBrute:
        startingBrute = int(seeds[p])
    seedPairs.append(range(seeds[p], seeds[p] + seeds[p + 1]))
    p += 2

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
        maps[">".join(currentMap)] = []
        continue

    destinationSourceRange = [int(x) for x in line.split(" ")]
    d, s, r = destinationSourceRange
    maps[">".join(currentMap)].append([range(d, d + r), range(s, s + r)])


def getMapped(f, to, seeds):
    result = []

    for seed in seeds:
        ranges = maps[f + ">" + to]
        mappedValue = seed
        for sourceRange, destRange in ranges:
            if seed in sourceRange:
                t = sourceRange.index(seed)
                mappedValue = destRange[t]
                break

        result.append(mappedValue)

    return result


tried = startingBrute - 100
result = [tried]
allTypes.reverse()

while True:
    for i in range(len(allTypes) - 1):
        result = getMapped(allTypes[i + 1], allTypes[i], result[:])

    for r in seedPairs:
        if result[0] in r:
            print(tried)
            exit()

    tried += 1
    result = [tried]
