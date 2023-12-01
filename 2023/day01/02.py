from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.read().splitlines()


def solve():
    words = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    nums = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]

    total = 0
    for line in data:
        first = 1000000000
        last = -1

        for item in nums + words:
            if item in line and line.find(item) < first:
                first = line.find(item)
                numone = item
            if item in line and line.rfind(item) > last:
                last = line.rfind(item)
                numtwo = item

        firstValue = numone
        secondValue = numtwo

        piss = []
        if numone in words:
            firstValue = str(words.index(numone) + 1)

        if numtwo in words:
            secondValue = str(words.index(numtwo) + 1)

        piss.append(str(firstValue))
        piss.append(str(secondValue))
        total += int("".join(piss))

        first = len(line) + 1
        last = -1

    print(total)


solve()
