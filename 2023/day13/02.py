from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"

file = file_location.open()

all_input = file.read().splitlines()

mirrors = []
current_mirror = []
for line in all_input:
    if line == "":
        mirrors.append(current_mirror)
        current_mirror = []
        continue

    current_mirror.append(list(line))

mirrors.append(current_mirror)


def split_mirror_vertically_at(mirror, i):
    left = []
    right = []

    currL = []
    currR = []

    for row in mirror:
        for x in range(len(row)):
            if x < i:
                currL.append(row[x])
            else:
                currR.append(row[x])

        currL.reverse()

        left.append("".join(currL))
        right.append("".join(currR))

        currL = []
        currR = []

    min_width = min(len(left[0]), len(right[0]))

    trimmed_left = []
    for line in left:
        trimmed_left.append(line[:min_width])

    trimmed_right = []
    for line in right:
        trimmed_right.append(line[:min_width])

    return trimmed_left, trimmed_right


def split_mirror_horizontally_at(mirror, i):
    top = []
    bottom = []

    for y in range(len(mirror)):
        if y >= i:
            bottom.append(mirror[y])
        else:
            top.append(mirror[y])

    top.reverse()

    min_length = min(len(top), len(bottom))

    top = top[:min_length]
    bottom = bottom[:min_length]

    return top, bottom


def try_is_vertically_symmetrical_at(mirror, P):
    cop = mirror[:]

    for j in range(len(cop)):
        for i in range(len(cop[0])):
            old = cop[j][i]

            if cop[j][i] == "#":
                cop[j][i] = "."
            elif cop[j][i] == ".":
                cop[j][i] = "#"

            for x in range(len(cop[0])):
                if x == P:
                    continue

                if is_vertically_symmetrical_at(cop[:], x):
                    return x

            cop[j][i] = old


def try_is_horizontally_symmetrical_at(mirror, P):
    cop = mirror[:]

    for j in range(len(cop)):
        for i in range(len(cop[0])):
            old = cop[j][i]

            if cop[j][i] == "#":
                cop[j][i] = "."
            elif cop[j][i] == ".":
                cop[j][i] = "#"

            for y in range(len(cop)):
                if y == P:
                    continue

                if is_horizontally_symmetrical_at(cop[:], y):
                    return y

            cop[j][i] = old


def is_vertically_symmetrical_at(mirror, i):
    if i > len(mirror[0]):
        return False

    if i == 0:
        return False

    left, right = split_mirror_vertically_at(mirror, i)

    is_symmetrical = True
    for j in range(len(left)):
        if left[j] != right[j]:
            is_symmetrical = False
            break

    return is_symmetrical


def is_horizontally_symmetrical_at(mirror, i):
    if i > len(mirror):
        return False

    if i == 0:
        return False

    top, bottom = split_mirror_horizontally_at(mirror, i)

    is_symmetrical = True
    for j in range(len(top)):
        if top[j] != bottom[j]:
            is_symmetrical = False
            break

    if len(top) == 0 or len(bottom) == 0:
        is_symmetrical = False

    return is_symmetrical


def print_mirror(m):
    for line in m:
        print("LINE>: ", end="")
        print("".join(line))

    print("\n")


def print_mirror_with_horizontal_reflector(m, i):
    mo = m[:]
    for j, line in enumerate(mo):
        if j == i:
            print("-" * len(line))
        print("".join(line))

    print("\n")


def print_mirror_with_vertical_reflector(m, i):
    mo = m[:]
    for line in mo:
        line.insert(i, "|")
        print("".join(line))

    print("\n")


def solve():
    vert = 0
    hor = 0
    count = 0
    map = {}
    for m in mirrors:
        for width in range(len(m[0])):
            if is_vertically_symmetrical_at(m[:], width):
                vert += width

                map[str(count)] = ("V", width)

        for height in range(len(m)):
            if is_horizontally_symmetrical_at(m[:], height):
                hor += height
                map[str(count)] = ("H", height)

        count += 1

    count = 0
    vert = 0
    hor = 0
    for m in mirrors:
        t, v = map[str(count)]

        val = try_is_vertically_symmetrical_at(m[:], v if t == "V" else -1)
        if val is not None:
            vert += val

        hVal = try_is_horizontally_symmetrical_at(m[:], v if t == "H" else -1)
        if hVal is not None:
            hor += hVal

        count += 1

    print(vert)
    print(hor)
    return vert + (hor * 100)


print(solve())

# 384230 too high
# 384128 too high
#
# 22947 too low
# 40192 not right
# 38439 not right
