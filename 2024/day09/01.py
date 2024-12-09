from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.read().strip()

disk = {}

for i, ins in enumerate(data):
    if i % 2 == 0:
        disk[i] = (str(int(i / 2)) * int(ins)).split()
    else:
        disk[i] = ("." * int(ins)).split()
    print(disk)

