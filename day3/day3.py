with open('data.dat') as file:
    data = [ line.strip() for line in file ]

counter = []
for i in range(0, len(data[0])):
    counter.append(0)

def get_readings(data):
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

    return [gam, epi]

readings = get_readings(data)

def multiply_readings(readings):
    return int(''.join(str(b) for b in  readings[0]), 2) * int(''.join(str(b) for b in readings[1]), 2)

def part_one(readings):
    return multiply_readings(readings)

def strip(passed_data, mode):
    for i in range(0, len(list(passed_data[0]))):
        count = 0
        ones = 0
        zeroes = 0
        for line in passed_data:
            if (int(line[i]) == 1):
                count = count + 1
                ones = ones + 1
            else:
                zeroes = zeroes + 1

        if (mode == 'most'):
            if (ones > zeroes):
                mask = 1
            elif (ones == zeroes):
                mask = 1
            else:
                mask = 0

        elif (mode == 'fewest'):
            if (ones > zeroes):
                mask = 0
            elif (zeroes == ones):
                mask = 0
            else:
                mask = 1

        new_data = []

        for line in passed_data:
            if (int(line[i]) == mask):
                new_data.append(line)

        passed_data = new_data[:]

        if (len(passed_data) == 1):
            return passed_data
    return passed_data

o2_reading = strip(data[:], 'most')
Co2_reading = strip(data[:], 'fewest')

print(multiply_readings([o2_reading, Co2_reading]))

exit()
