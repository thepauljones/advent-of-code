from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.readlines()

dirs = {}
dirs["^"] = (-1, 0)
dirs["v"] = (1, 0)
dirs[">"] = (0, 1)
dirs["<"] = (0, -1)

grid = []
for i in range(data.index("\n")):
    grid.append(list(data[i].strip()))

ins = list(data[-1].strip())

vex = []
for d in ins:
    if d == " ":
        break
    vex.append(dirs[d])

print(vex)
print(grid)
