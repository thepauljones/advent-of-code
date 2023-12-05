from pathlib import Path
from collections import defaultdict

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.read().splitlines()

seeds = [int(x) for x in data[0].split(": ")[1].split(" ")]

seedPairs = []

p = 0

while p < len(seeds) - 1:
    seedPairs.append([seeds[p], seeds[p + 1]])
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
        continue

    sourceDestinationRange = [int(x) for x in line.split(" ")]
    maps[">".join(currentMap)].append(sourceDestinationRange)


def getMapped(f, to, seeds):
    result = []
    for seed in seeds:
        current = maps[f + ">" + to]
        mappedValue = seed
        for m in current:
            dest, source, r = m
            sourceRange = range(source, source + r)
            destRange = range(dest, dest + r)

            if seed in sourceRange:
                t = sourceRange.index(seed)
                mappedValue = destRange[t]

        result.append(mappedValue)

    return result


hugeSeedList = []
for pair in seedPairs:
    hugeSeedList.extend(list(range(pair[0], pair[0] + pair[1])))


print(len(hugeSeedList))

for i in range(len(allTypes) - 1):
    hugeSeedList = getMapped(allTypes[i], allTypes[i + 1], hugeSeedList[:])

print(min(hugeSeedList))
