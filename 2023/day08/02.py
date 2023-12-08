from pathlib import Path
from tqdm import tqdm

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

# Prep
data = file.read().splitlines()

directions = list(data[0])
directions = list(map(lambda x: 0 if x == "L" else 1, directions))

nodes = data[2:]
pos = 0
rev = 0
map = {}

starts = []
destinations = []


def unpack_node(node_string):
    parts = node_string.split(" = ")
    location = parts[0]
    dest = (parts[1].split(", ")[0][1:], parts[1].split(", ")[1][:-1])

    if location[2] == "A":
        starts.append(location)

    if location[2] == "Z":
        destinations.append(location)

    return location, dest


node = nodes[0]


for node in nodes:
    loc, dest = unpack_node(node)
    map[loc] = dest


# Solve
pos = starts
loops = 0
i = 0


# Solve
def solve(start, targets):
    pos = start
    loops = 0
    i = 0
    while i < len(directions):
        pos = map[pos][directions[i]]
        loops += 1
        i += 1
        if pos in targets:
            break

        if i > len(directions) - 1:
            i = 0

        if loops > 1000000:
            return loops

    return loops


lowestLoops = float("inf")

loops = []

for s in starts:
    loops.append(solve(s, destinations))


print(loops)
ans = 1
for i in range(len(loops) - 1):
    ans += loops[i] * loops[i + 1]

print(ans - 1)
