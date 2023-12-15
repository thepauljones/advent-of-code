from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = [list(x) for x in file.read().splitlines()]


def p(grid):
    for line in grid:
        print("".join(line))

    print("\n")


p(data[:])


def calc_seg(seg):
    result = 0
    for i in range(seg[1]):
        result += seg[0] - i

    return result


def evaluate(map):
    ans = 0
    for line in map:
        for seg in line:
            ans += calc_seg(seg)

    print(ans)


def slide(grid):
    cols = list(zip(*grid))

    map = []
    for line in cols:
        map_line = []
        segments = "".join(line).split("#")

        pos = 0
        for seg in segments:
            if seg.count("O") > 0:
                map_line.append((len(line) - pos, seg.count("O")))
            pos += len(seg) + 1

        map.append(map_line)

    print(map)
    print(evaluate(map))


slide(data)


def solve():
    return 0


def test():
    assert solve() == 0
