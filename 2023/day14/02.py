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


def evaluate(grid):
    map = []
    for line in grid:
        map_line = []
        segments = "".join(line).split("#")

        pos = 0
        for seg in segments:
            if seg.count("O") > 0:
                map_line.append((len(line) - pos, seg.count("O")))
            pos += len(seg) + 1

        map.append(map_line)

    ans = 0
    for line in map:
        for seg in line:
            ans += calc_seg(seg)

    print("Answer:", ans)


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
def rotation(grid):
    slid = slide_north(grid)
    slid = slide_west(slid)
    slid = slide_south(slid)
    slid = slide_east(slid)

    return slid[:]


e = []
for i in tqdm(range(100000)):
    data = rotation(data[:])
    e.append(evaluate(data))

print(min(e))


def solve():
    return 0


def test():
    assert solve() == 0
