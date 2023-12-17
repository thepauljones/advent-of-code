from pathlib import Path
import sys
import time

sys.setrecursionlimit(2500)
script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = [list(x) for x in file.read().splitlines()]


lit = {}


split = {}


def show_energized():
    count = 0
    for j, line in enumerate(data):
        for i, char in enumerate(line):
            if (j, i) in lit:
                count += 1
                print("#", end="")
            else:
                print(char, end="")
        print("\n")

    print("\n")
    print("\n")
    print("\n")

    return count


def project_beam(pos, vector):
    pj, pi = pos
    vj, vi = vector

    lit[(pj, pi)] = True

    if pi > len(data[0]) - 1 or pi < 0:
        print("ENDED RUN horizontal")
        return

    if pj > len(data) - 1 or pj < 0:
        print("ENDED RUN vert")
        return

    lit[(pj, pi)] = True

    newVI = vi
    newVJ = vj

    # handle mirrors and splitters
    if data[pj][pi] == "/":
        if vi == 1:  # came from the left
            newVJ = -1  # go up
            newVI = 0
        if vi == -1:  # came from the right
            newVJ = 1  # go down
            newVI = 0
        if vj == 1:  # came from above
            newVI = -1  # go left
            newVJ = 0
        if vj == -1:  # came from below
            newVJ = 0  # go right
            newVI = 1

    if data[pj][pi] == "\\":
        if vi == 1:  # came from the left
            newVJ = 1  # go down
            newVI = 0
        if vi == -1:  # came from the right
            newVJ = -1  # go up
            newVI = 0
        if vj == 1:  # came from above
            newVJ = 0  # go right
            newVI = 1
        if vj == -1:  # came from below
            newVI = -1  # go left
            newVJ = 0

    if data[pj][pi] == "-":
        if vj != 0:
            if (pj, pi) in split:
                return
            # continue in one direction, and call project_beam again for the other
            newVI = 1
            newVJ = 0
            split[(pj, pi)] = True

            print("split left")
            project_beam(
                (pj, pi - 1), (0, -1)
            )  # recursively call project beam for split direction

    if data[pj][pi] == "|":
        if vi != 0:
            if (pj, pi) in split:
                return
            # continue in one direction, and call project_beam again for the other
            newVJ = -1
            newVI = 0

            split[(pj, pi)] = True

            print("split down")
            project_beam(
                (pj, pi), (1, 0)
            )  # recursively call project beam for split direction

    project_beam((pj + newVJ, pi + newVI), (newVJ, newVI))


# Start beam
project_beam((0, 0), (0, 1))


answer = show_energized()

print(answer)


def solve():
    return 0


def test():
    assert solve() == 0
