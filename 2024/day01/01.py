from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.readlines()

left = []
right = []

sums = []

for line in data:
    one, two = map(int, line.split())
    left.append(one)
    right.append(two)

maxLeft = max(left)
maxRight = max(right)

minLeft = min(left)
minRight = min(right)

while (maxLeft != minLeft):
    minLeft = min(left)
    left.pop(left.index(minLeft))
    minRight = min(right)
    right.pop(right.index(minRight))

    sums.append(abs(minLeft - minRight))



def solve():
    print(sums)
    print(sum(sums))

    print('test')


solve()
