from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.readlines()

a = []
blocks = []
inA = True

for l in data:
    if l == "\n":
        inA = False
        continue
    if inA:
        a.append(l.strip())
    else:
        blocks.append(l.strip())

B = {}
for line in a:
    name, val = line.split(":")
    B[name] = int(val)

pos = 0
while len(blocks) > 0:
    if pos > len(blocks) - 1:
        pos = 0

    print(pos)
    line = blocks[pos]
    print("TEST", line, blocks, pos)
    logic, output = line.split(" -> ")
    a, type, b = logic.split(" ")

    if a not in B or b not in B:
        pos += 1
        continue
    else:
        blocks.remove(line)
        pos -= 1

    if type == "AND":
        res = B[a] & B[b]
        B[output] = res
    if type == "OR":
        res = B[a] | B[b]
        B[output] = res
    if type == "XOR":
        res = B[a] ^ B[b]
        B[output] = res

res = ""
for k in sorted(B.keys(), reverse=True):
    if k[0] == "z":
        res += str(B[k])

print(int(res, 2))
