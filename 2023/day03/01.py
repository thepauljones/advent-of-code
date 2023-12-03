from pathlib import Path
import re
import numpy as np

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

engine = [list(x.strip()) for x in file.readlines()]


def get_adjacent(j, i, data):
    adjs = []
    if j < len(data) - 1:
        adjs.append(data[j + 1][i])  # South
        if i >= 1:
            adjs.append(data[j + 1][i - 1])  # South-West
        if i < len(data[0]) - 1:
            adjs.append(data[j + 1][i + 1])  # South-East

    if j >= 1:
        adjs.append(data[j - 1][i])  # North
        if i >= 1:
            adjs.append(data[j - 1][i - 1])  # North-West
        if i < len(data[0]) - 1:
            adjs.append(data[j - 1][i + 1])  # North-East

    if i < len(data[j]) - 1:  # East
        adjs.append(data[j][i + 1])

    if i >= 1:
        adjs.append(data[j][i - 1])  # West

    return adjs


digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

non_symbols = digits + ["."]


def solve():
    allDigits = []
    for j in range(0, len(engine)):
        currentDigit = []
        currentDigitAdjacents = []
        for i in range(0, len(engine[0])):
            if engine[j][i] in digits:
                currentDigit.append(engine[j][i])
                currentDigitAdjacents.extend(get_adjacent(j, i, engine))
            else:
                if len(currentDigit) > 0:
                    print(currentDigit)
                    print(currentDigitAdjacents)
                    adjacentSymbols = list(
                        set(currentDigitAdjacents).difference(non_symbols)
                    )
                    if len(adjacentSymbols) > 0:
                        allDigits.append(int("".join(currentDigit)))
                        print(
                            "adding "
                            + str(allDigits[-1])
                            + " because of "
                            + ",".join(adjacentSymbols)
                        )
                    currentDigit = []
                    currentDigitAdjacents = []

    print(sum(allDigits))


solve()
