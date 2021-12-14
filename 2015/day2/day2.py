with open('data.dat') as file:
    data = [line.strip() for line in file]

total = 0
for line in data:
    l, w, h = [int(x) for x in line.split('x')]
    sides = [l * w, w * h, h * l]
    total += 2*sum(sides) + min(sides)

print(total)

