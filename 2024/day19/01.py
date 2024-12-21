from pathlib import Path
from functools import cache

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.read()
t, d = data.split("\n\n")

towels = list(reversed(sorted(list(map(str.strip, t.split(","))), key=len)))
designs = d.strip().split("\n")


@cache
def test_design(design):
    res = 0
    if len(design) == 0:
        return 1

    else:
        res = 0
        for a in towels:
            if design.startswith(a):
                res += test_design(design[len(a) :])

    return res


ans = 0
for d in designs:
    print(d, test_design(d))
    if test_design(d):
        ans += 1

print(ans)
