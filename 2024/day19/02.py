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
    # If you've popped off things that start with a towel design
    # such that only one letter is left, then that is one design that is possible
    if len(design) == 0:
        return 1

    else:
        # count the number of possibilities with ALL the towels it _could_ start with
        # and add them all up, then send what ever is left back into this washing machine
        # by chopping off everything after the length of the thing that matched
        res = 0
        for a in towels:
            if design.startswith(a):
                res += test_design(design[len(a) :])

    return res


ans = 0
for d in designs:
    print(d, test_design(d))
    ans += test_design(d)

print(ans)
