with open('data.dat') as file:
    data = [ line.strip() for line in file ]

counter = []
for i in range(0, len(data[0])):
    counter.append(0)

def part_one(data):
    for line in data:
        i = 0
        for value in [value for value in line]:
            counter[i] += int(value)
            i+=1

    gam = []
    epi = []
    for i in range(0, len(data[0])):
        gam.append(0)
        epi.append(0)

    for i in range(0, len(counter)):
        gam[i] = 0 if counter[i] > len(data) / 2 else 1
        epi[i] = 1 if counter[i] > len(data) / 2 else 0

    binary_result_gam = ''.join(str(b) for b in gam)
    binary_result_epi = ''.join(str(b) for b in epi)

    return int(binary_result_gam, 2) * int(binary_result_epi, 2)

print(part_one(data))
exit()
