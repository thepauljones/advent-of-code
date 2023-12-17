from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = [list(x) for x in file.read().splitlines()]


lit = {}


def project_beam(pos, vector):
    pj, pi = pos
    vj, vi = vector

    if pi > len(data[0]) - 1 or pi < 0:
        return

    if pj > len(data) - 1 or pj < 0:
        return

    lit[(pj, pi)] = True

    # handle mirrors and splitters
    if data[pj][pi] == "":
        if vi == 1:
            vi = 0
            vj = -1
        if vi == -1:
            vi = 0
            vj = 1
        if vj == 1:
            vj = 0
            vi = -1
        if vj == -1:
            vi = 1
            vj = 0

    if data[pj][pi] == "\\":
        if vi == 1:
            vi = 0
            vj = 1
        if vi == -1:
            vi = 0
            vj = -1
        if vj == -1:
            vi = -1
            vj = 0
        if vj == 1:
            vi = 1
            vj = 0

    if data[pj][pi] == "-":
        if vi != 0:  # going horizontally
            print("do nothing")
        else:
            # continue in one direction, and call project_beam again for the other
            vi = -1
            vj = 0
            print("split horizonal")
            project_beam(
                (pj, pi), (0, 1)
            )  # recrusively call project beam for split direction

    if data[pj][pi] == "|":
        if vj != 0:  # going vertically
            print("do nothing")
        else:
            # continue in one direction, and call project_beam again for the other
            vj = -1
            vi = 0
            print("split vertical")
            print("vi", vi, vj)
            project_beam(
                (pj, pi), (1, 0)
            )  # recrusively call project beam for split direction

    project_beam((pj + vj, pi + vi), (vj, vi))


project_beam((0, 0), (0, 1))
print(len(lit))


def show_energized():
    for j, line in enumerate(data):
        for i, char in enumerate(line):
            if (j, i) in lit:
                print("#", end="")
            else:
                print(char, end="")
        print("\n")


print(lit)
show_energized()


def solve():
    return 0


def test():
    assert solve() == 0
