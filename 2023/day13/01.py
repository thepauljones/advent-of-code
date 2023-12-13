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


def is_vertically_symmetrical_at(mirror, i):
    if i > len(mirror[0]) - 1:
        return False

    left, right = split_mirror_vertically_at(mirror, i)

    is_symmetrical = True
    for j in range(len(left)):
        if left[j] != right[j]:
            is_symmetrical = False
            break

    return is_symmetrical


def is_horizontally_symmetrical_at(mirror, i):
    if i > len(mirror) - 1:
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
        print("".join(line))
    print()


def print_mirror_with_horizontal_reflector(m, i):
    print("found horizontal")
    for j, line in enumerate(m):
        if j == i:
            print("-" * len(line))
        print("".join(line))
    print()
    print()
    print()
    print()


def print_mirror_with_vertical_reflector(m, i):
    print("found vertical")
    for line in m:
        line.insert(i, "|")
        print("".join(line))

    print()
    print()
    print()


def solve():
    vert = 0
    hor = 0
    for m in mirrors:
        loop = max(len(m), len(m[0]))

        for j in range(loop):
            if is_vertically_symmetrical_at(m, j):
                print_mirror_with_vertical_reflector(m, j)
                vert += j

            if is_horizontally_symmetrical_at(m, j):
                print_mirror_with_horizontal_reflector(m, j)
                hor += j

    print(vert)
    print(hor)
    return vert + (hor * 100)


print(solve())
