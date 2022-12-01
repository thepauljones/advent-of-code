from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = [[]]
count = 0

for x in file.readlines():
    if (x == '\n'):
        count += 1
        data.append([])
    else:
        data[count].append(int(x))

maxElf = 0

for elf in data:
    maxElf = max(sum(elf), maxElf)

print(maxElf)

