with open('data.dat') as file:
    data = [line.strip() for line in file]

def get_digits(line):
    return line.split(' | ')[1]

valid = map(get_digits, data)

valid_digits = [2, 4, 3, 7]

count = 0
for digits in [line.split() for line in valid]:
    for digit in digits:
        if (len(digit) in valid_digits):
            count += 1

print(count)
