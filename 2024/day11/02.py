from pathlib import Path
from functools import lru_cache

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = str.strip(file.read())

stones = data.split(" ")

NUM_BLINKS = 25

# I had a lookup {} dict but it's handier to just slap a cache decorator on here
# The point is to handle each stone completely separately from the last blink downwards
# So start at 75 in this case, blink down to 74, then 73, etc. until 0
#
# The cache decorator will store the results of each call to process() so that we don't have to recompute them


@lru_cache(maxsize=None)
def process(s, blinks):
    res = 0

    # No blinks left, return 1
    # This is the part that fries my brain a bit
    if blinks == 0:
        return 1

    # this makes sense, blink from whatever value, downwards
    # and set the result to the next blink and the next and the next
    # until one.
    if s == "0":
        res = process(1, blinks - 1)
    elif len(str(s)) % 2 == 0:
        temp = []
        temp.append(str(int(s[: int(len(s) / 2)])))
        temp.append(str(int(s[int(len(s) / 2) :])))

        res = process(temp[0], blinks - 1) + process(temp[1], blinks - 1)
    else:
        res = process(str(int(s) * 2024), blinks - 1)

    return res


ans = 0
for y in stones:
    ans += process(y, NUM_BLINKS)

print(ans)
