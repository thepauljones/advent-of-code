from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = []

for line in file:
    line = line.strip()
    if line.startswith("Button A:"):
        a = list(map(int, re.findall(r"\d+", line)))
    elif line.startswith("Button B:"):
        b = list(map(int, re.findall(r"\d+", line)))
    elif line.startswith("Prize:"):
        prize = list(map(int, re.findall(r"\d+", line)))
        data.append([a, b, prize])


DUD = 99999999


def solve(a, b, target):
    fewest_button_presses = DUD
    for j in range(101):
        for i in range(101):
            if j * a[0] + i * b[0] == target[0] and j * a[1] + i * b[1] == target[1]:
                fewest_button_presses = min(fewest_button_presses, i + 3 * j)

    return fewest_button_presses


ans = 0
for machine in data:
    a, b, target = machine
    result = solve(a, b, target)
    if result != DUD:
        ans += result


print(ans)
