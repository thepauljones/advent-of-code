from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.read()
t, d = data.split("\n\n")

towels = list(reversed(sorted(list(map(str.strip, t.split(","))), key=len)))
designs = d.strip().split("\n")

print(towels)

print(designs)


def test_design(design):
    if len(design) == 0:
        return True

    for a in towels:
        if design.startswith(a):
            return test_design(design[len(a) :])

    return False


ans = 0
for d in designs:
    print(d, test_design(d))
    if test_design(d):
        ans += 1

print(ans)
