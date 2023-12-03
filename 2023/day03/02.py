from pathlib import Path
import re
import numpy as np

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

engine = [list(x.strip()) for x in file.readlines()]


def get_adjacent_stars(j, i, data):
    adjs = []
    if j < len(data) - 1:
        if data[j + 1][i] == "*":
            adjs.append([j + 1, i])
        if i >= 1:
            if data[j + 1][i - 1] == "*":  # South-West
                adjs.append([j + 1, i - 1])
        if i < len(data[0]) - 1:
            if data[j + 1][i + 1] == "*":  # South-East
                adjs.append([j + 1, i + 1])  # South-East

    if j >= 1:
        if data[j - 1][i] == "*":  # North
            adjs.append([j - 1, i])  # North
        if i >= 1:
            if data[j - 1][i - 1] == "*":  # North-West
                adjs.append([j - 1, i - 1])  # North-West
        if i < len(data[0]) - 1:
            if data[j - 1][i + 1] == "*":  # North-East
                adjs.append([j - 1, i + 1])  # North-East

    if i < len(data[j]) - 1:  # East
        if data[j][i + 1] == "*":
            adjs.append([j, i + 1])

    if i >= 1:
        if data[j][i - 1] == "*":  # West
            adjs.append([j, i - 1])  # West

    return adjs


digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

non_symbols = digits + ["."]


def solve():
    answer = 0
    gearMap = {}
    for j in range(0, len(engine)):
        currentDigit = []
        currentAdjacentStars = []
        for i in range(0, len(engine[0])):
            if engine[j][i] in digits:
                currentDigit.append(engine[j][i])
                currentAdjacentStars.extend(get_adjacent_stars(j, i, engine))

            else:
                if len(currentDigit) > 0 and len(currentAdjacentStars) > 0:
                    for x in currentAdjacentStars:
                        starMap = ",".join(map(str, x))
                        if starMap not in gearMap:
                            gearMap[starMap] = []
                    gearMap[starMap].append(int("".join(currentDigit)))

                currentDigit = []
                currentAdjacentStars = []

    for stars in gearMap:
        if len(gearMap[stars]) == 2:
            answer += gearMap[stars][0] * gearMap[stars][1]

    print(answer)

    print(gearMap)


solve()
