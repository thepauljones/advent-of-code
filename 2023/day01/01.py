from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.read().splitlines()


def solve():
    total = 0
    for line in data:
        f = re.sub("[^\\d]+", "", line)
        nums = []
        nums.append(f[0])
        nums.append(f[-1])
        print(nums)
        total += int("".join(nums))

    print(total)


solve()
