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


# Slides rocks to north of grid
def slide(grid):
    # zip  basically gives you a matrix transform of 90 degrees and list then makes it an array again
    # essentially rotating it to the left to allow easier calcualtions
    cols = list(zip(*grid))

    map = []
    # for each line, split around rocks, then the count of the rocks
    # is the same as moving them to the left (which is the "Top, or north" in this case)
    # then make a list of tuples where the left value is the "power of the line"
    # i.e. the length, minus the index, so the left most, (north-most line is the length of the array - it's index, (0))
    # and then you multiply that number by the number of rocks, removing 1 each time, for subsequent rows
    #
    # add these up for the whole grid and Robert's your mothers brother
    for line in cols:
        map_line = []
        segments = "".join(line).split("#")

        pos = 0
        for seg in segments:
            if seg.count("O") > 0:
                map_line.append((len(line) - pos, seg.count("O")))
            pos += len(seg) + 1

        map.append(map_line)

    print(evaluate(map))


slide(data)


def solve():
    return 0


def test():
    assert solve() == 0
