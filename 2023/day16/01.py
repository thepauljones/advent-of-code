from pathlib import Path
import time

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = [list(x) for x in file.read().splitlines()]


lit = {}


def show_energized():
    for j, line in enumerate(data):
        for i, char in enumerate(line):
            if (j, i) in lit:
                print("#", end="")
            else:
                print(char, end="")
        print("\n")

    print("\n")
    print("\n")
    print("\n")


def project_beam(pos, vector, prevVec):
    time.sleep(0.1)
    show_energized()
    pj, pi = pos
    vj, vi = vector

    pvj, pvi = prevVec

    if pi > len(data[0]) - 1 or pi < 0:
        return

    if pj > len(data) - 1 or pj < 0:
        return

    lit[(pj, pi)] = True

    # handle mirrors and splitters
    if data[pj][pi] == "/":
        if pvi == 1:
            vi = 0
            vj = -1
        if pvi == -1:
            vi = 0
            vj = 1
        if pvj == 1:
            vj = 0
            vi = -1
        if pvj == -1:
            vi = 1
            vj = 0

        print("Hit up mirror with prevVec", prevVec)

    if data[pj][pi] == "\\":
        if pvi == 1:
            vi = 0
            vj = 1
        if pvi == -1:
            vi = 0
            vj = -1
        if pvj == -1:
            vi = -1
            vj = 0
        if pvj == 1:
            vi = 1
            vj = 0

    if data[pj][pi] == "-":
        if vi != 0:  # going horizontally
            pass
        else:
            # continue in one direction, and call project_beam again for the other
            vi = -1
            vj = 0
            project_beam(
                (pj, pi + 1), (0, 1), vector
            )  # recrusively call project beam for split direction

    if data[pj][pi] == "|":
        if vj != 0:  # going vertically
            pass
        else:
            # continue in one direction, and call project_beam again for the other
            vj = -1
            vi = 0
            project_beam(
                (pj + 1, pi), (1, 0), vector
            )  # recrusively call project beam for split direction

    project_beam((pj + vj, pi + vi), (vj, vi), (vj, vi))


# Start beam
project_beam((0, 0), (0, 1), (0, 1))


show_energized()
print(len(lit))


def solve():
    return 0


def test():
    assert solve() == 0
