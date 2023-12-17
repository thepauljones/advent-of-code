from pathlib import Path
import sys

sys.setrecursionlimit(99500)
script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = [list(x) for x in file.read().splitlines()]


ALL_RUNS = {}


def show_energized(hitMap):
    count = 0
    for j, line in enumerate(data):
        for i, char in enumerate(line):
            if (j, i) in hitMap:
                count += 1
            else:
                pass

    return count


def project_beam(pos, vector, hitmap, activated):
    pj, pi = pos
    vj, vi = vector

    hitmap[(pj, pi)] = True

    if pi > len(data[0]) - 1 or pi < 0:
        return

    if pj > len(data) - 1 or pj < 0:
        return

    hitmap[(pj, pi)] = True

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
            if (pj, pi) in activated:
                return
            # continue in one direction, and call project_beam again for the other
            newVI = 1
            newVJ = 0
            activated[(pj, pi)] = True

            project_beam(
                (pj, pi - 1), (0, -1), hitmap, activated
            )  # recursively call project beam for split direction

    if data[pj][pi] == "|":
        if vi != 0:
            if (pj, pi) in activated:
                return
            # continue in one direction, and call project_beam again for the other
            newVJ = -1
            newVI = 0

            activated[(pj, pi)] = True

            project_beam(
                (pj, pi), (1, 0), hitmap, activated
            )  # recursively call project beam for split direction

    project_beam((pj + newVJ, pi + newVI), (newVJ, newVI), hitmap, activated)


# Ladies and Gentlemen, Welcome Welcome Welcome to the FUCK EVERY POSSIBLITY AT THE PROBLEM
# approach. Below the keen eyed among you will observe me just battering all the possiblities at my
# cringing CPU and screeching "Fuck you asshole" as hot pokers are slipped into its most
# sensitive orifices
#
# For the sake of completeness "I'm _not_ sorry"
all_answers = []
# from the left down
for j in range(len(data)):
    hitmap = {}
    activated = {}
    project_beam((j, 0), (j, 1), hitmap, activated)
    ALL_RUNS[(j, 1)] = hitmap

# from the top down
for i in range(len(data[0])):
    hitmap = {}
    activated = {}
    project_beam((0, i), (1, 0), hitmap, activated)
    ALL_RUNS[(0, i)] = hitmap

# from the bottom up
for i in range(len(data[0])):
    hitmap = {}
    activated = {}
    project_beam((len(data) - 1, i), (-1, 0), hitmap, activated)
    ALL_RUNS[(len(data) - 1 - i, i)] = hitmap

# from the right in
for j in range(len(data)):
    hitmap = {}
    activated = {}
    project_beam((j, len(data[0]) - 1), (j, -1), hitmap, activated)
    ALL_RUNS[(j, len(data[0]) - 1)] = hitmap

for run in ALL_RUNS:
    all_answers.append(show_energized(ALL_RUNS[run]))

print(all_answers)
print(max(all_answers))


def solve():
    return 0


def test():
    assert solve() == 0
