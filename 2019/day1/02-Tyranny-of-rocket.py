from pathlib import Path
import math

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()


def calculate(mass):
    result = math.floor(mass / 3 - 2)
    return result


masses = [int(x) for x in file.readlines()]

total = 0
for mass in masses:
    fuel = calculate(mass)
    extra = fuel
    extras = []
    while extra > 0:
        extra = calculate(extra)

        if extra > 0:
            extras.append(extra)

    total += fuel + sum(extras)

print(total)
