from pathlib import Path
from tqdm import tqdm

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

rows = file.read().splitlines()
sky = []
cols = []
for line in rows:
    sky.append([x for x in line])


def get_col(i):
    result = []
    for j in range(len(sky)):
        result.append(sky[j][i])

    return result


for i in range(len(rows[0])):
    cols.append(get_col(i))


def is_empty(t):
    return list(set(t)) == ["."]


rows_to_insert = []
cols_to_insert = []

for j in range(len(sky)):
    if is_empty(sky[j]):
        rows_to_insert.append(j)
for i in range(len(sky[0])):
    if is_empty(get_col(i)):
        cols_to_insert.append(i)

rows_to_insert.reverse()
cols_to_insert.reverse()


def print_sky(galaxy_positions):
    count = 1

    maxX = 0
    maxY = 0
    for g in galaxy_positions:
        y, x = g
        maxX = max(maxX, x)
        maxY = max(maxY, y)

    for j in range(maxY + 1):
        for i in range(maxX + 1):
            if (j, i) in galaxy_positions:
                print(count, end="")
                count += 1
            else:
                print(".", end="")

        print()


def get_distance(p):
    x, y = p

    x1, y1 = x
    x2, y2 = y

    return abs(y2 - y1) + abs(x2 - x1)


galaxy_positions = []
for j in range(len(sky)):
    for i in range(len(sky[0])):
        if sky[j][i] == "#":
            galaxy_positions.append((j, i))


# expand universe!
def expand(g):
    step = 1
    y, x = g

    for r in rows_to_insert:
        if r < y:
            y += step

    for c in cols_to_insert:
        if c < x:
            x += step

    return (y, x)


expanded = []
for g in galaxy_positions:
    expanded.append(expand(g))
# print_sky(galaxy_positions[:])
print_sky(expanded[:])

# expand universe!

pairs = []
for g in expanded:
    for p in [x for x in expanded if x != g]:
        if [g, p] not in pairs and [p, g] not in pairs:
            pairs.append([g, p])

print("len pairs", len(pairs))

assert get_distance([(6, 1), (11, 5)]) == 9, "Manhattan distance not working"
assert get_distance([(1, 1), (-1, -1)]) == 4, "Manhattan distance not working"
assert get_distance([(0, 2), (0, 4)]) == 2, "Manhattan distance not working"

ans = 0
for p in pairs:
    ans += get_distance(p)

print("Answer: ", ans)
