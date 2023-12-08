from pathlib import Path

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

start = "AAA"
target = "ZZZ"


def unpack_node(node_string):
    parts = node_string.split(" = ")
    location = parts[0]
    dest = (parts[1].split(", ")[0][1:], parts[1].split(", ")[1][:-1])

    return location, dest


node = nodes[0]


for node in nodes:
    loc, dest = unpack_node(node)
    map[loc] = dest


# Solve
def solve(start, target):
    pos = start
    loops = 0
    i = 0
    while i < len(directions):
        pos = map[pos][directions[i]]
        loops += 1
        i += 1
        if pos == target:
            break

        if i > len(directions) - 1:
            i = 0

    return loops


ans = solve(start, target)
print(ans)
