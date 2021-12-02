with open('data.dat') as file:
    data = [ line.strip() for line in file ]

def part_one(data):
    depth = 0
    x = 0

    for line in data:
        ins = line.split(' ')
        instruction = ins[0]
        value = int(ins[1])

        if instruction == 'down':
            depth = depth + value
        elif instruction == 'up':
            depth = depth - value
        elif instruction == 'forward':
            x = x + value

    return depth * x


def part_two(data):
    depth = 0
    x = 0
    aim = 0

    for line in data:
        ins = line.split(' ')
        instruction = ins[0]
        value = int(ins[1])

        if instruction == 'down':
            aim = aim + value
        elif instruction == 'up':
            aim = aim - value
        elif instruction == 'forward':
            x = x + value
            depth += aim * value

    return  depth * x

print(part_one(data))
print(part_two(data))

exit()
