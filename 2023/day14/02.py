from pathlib import Path
from tqdm import tqdm
import functools

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = [x for x in file.read().splitlines()]


def p(grid):
    for line in grid:
        print("".join(line))

    print("\n")


def calc_seg(seg):
    result = 0
    for i in range(seg[1]):
        result += seg[0] - i

    return result


def evaluate(g):
    ans = 0
    i = 0
    for line in g:
        score = max(0, line.count("O") * abs(len(g) - i))
        ans += score
        i += 1

    return ans


@functools.cache
def s(line):
    n = "".join(line)
    while ".O" in n:
        n = n.replace(".O", "O.")

    return n


# Slides rocks to north of grid
def slide_north(grid):
    # zip  basically gives you a matrix transform of 90 degrees and list then makes it an array again
    # essentially rotating it to the left to allow easier calcualtions
    cols = list(zip(*grid))

    slid = []

    for line in cols:
        slid.append(s(line))

    slid = list(zip(*slid))

    return slid


def slide_west(grid):
    slid = []

    for line in grid:
        slid.append(s(line))

    return slid


def slide_south(grid):
    return list(reversed(slide_north(reversed(grid))))


def slide_east(grid):
    slid = []
    for line in grid:
        slid.append(list(reversed(s(reversed(line)))))

    return slid


# slide north -> west - > south - > east
def rotation(grid, shouldPrint):
    slid = slide_north(grid)
    if shouldPrint:
        print("North")
        p(slid)
    slid = slide_west(slid)
    if shouldPrint:
        print("West")
        p(slid)
    slid = slide_south(slid)
    if shouldPrint:
        print("South")
        p(slid)
    slid = slide_east(slid)
    if shouldPrint:
        print("East")
        p(slid)

    return slid[:]


scores = []
repeats = []
loop_size = 0
first = 1

for i in tqdm(range(1000)):
    data = rotation(data[:], False)
    score = evaluate(data)

    if score in scores:
        print("repeat:", i)
        scores.append(score)
        first = i + 1

    scores.append(score)


print(scores)


def solve():
    return 0


def test():
    assert solve() == 0


# too low 100354
#
#
#
#
#  also not right
#
#  not right
#  also not right
#
#  tried
#
#  tried down to 104450 :/
