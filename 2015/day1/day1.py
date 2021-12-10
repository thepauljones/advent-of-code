with open('data.dat') as file:
    data = [line.strip() for line in file]

def part_one():
    floor = 0
    for i in range(0, len(data[0])):
        if data[0][i] == '(':
            floor += 1
        elif data[0][i] == ')':
            floor -= 1

    return floor

def part_two():
    floor = 0
    for i in range(0, len(data[0])):
        if data[0][i] == '(':
            floor += 1
        elif data[0][i] == ')':
            floor -= 1

        if floor == -1:
            return i + 1

    return False

print(part_one())
print(part_two())
