from pathlib import Path
from collections import defaultdict

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.read()

lensMap = defaultdict(list)


def hash(input):
    result = 0
    for char in input:
        result += ord(char)
        result *= 17
        result %= 256

    return result


def process_box(input):
    if "-" in input:
        label = input.split("-")[0]
        box_location = str(hash(label))
        lenses = lensMap[box_location]

        updated_lenses = []
        for lens in lenses:
            if lens[0] != label:
                updated_lenses.append(lens)

        lensMap[box_location] = updated_lenses

    elif "=" in input:
        label, (lens_strength) = input.split("=")
        box_location = str(hash(label))

        lenses = lensMap[box_location]

        updated_lenses = []

        updated = False
        for lens in lenses:
            currLabel, _ = lens
            if currLabel == label:
                updated_lenses.append((label, lens_strength))
                updated = True
            else:
                updated_lenses.append(lens)

        if not updated:
            updated_lenses.append((label, lens_strength))

        lensMap[box_location] = updated_lenses


for ins in data.strip().split(","):
    process_box(ins)


def calculate_focus_power(lensMap):
    ans = 0
    for box in lensMap:
        box_power = 0
        lenses = lensMap[box]

        for i, lens in enumerate(lenses):
            slot = i + 1
            box_power = int(box) + 1

            lens_strength = int(lens[1])

            ans += box_power * slot * lens_strength

    return ans


answer = calculate_focus_power(lensMap)

print(answer)


def solve():
    return 0


def test():
    assert solve() == 0
