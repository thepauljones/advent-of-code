from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.readlines()

left = []
right = []


answer = 0

for line in data:
    one, two = map(int, line.split())
    left.append(one)
    right.append(two)


for item in left:
    increment = item * right.count(item)
    answer += increment



def solve():

    print(answer)


solve()
