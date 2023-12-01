from pathlib import Path
import re
import sys
from termcolor import colored, cprint
from threading import Timer

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

    def printThing(one, two, middle):
        one = colored(one, "green")
        two = colored(two, "red")
        print(one + middle + two)

    total = 0
    count = 1
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

        count += 1
        t = Timer(
            0.1 * count, printThing, [numone, numtwo, line[len(numone) : -len(numtwo)]]
        )
        t.start()

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
