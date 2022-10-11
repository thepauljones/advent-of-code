with open('data.dat') as file:
    data = [line.strip() for line in file]


def check(i):
    one = False
    two = False

    c = 0
    for x in i:
        if c + 2 < len(i) and x == i[c + 2]:
            two = True

        if c + 1 < len(i):
            test = x + i[c + 1]

            if i.find(test, c + 2) != -1:
                one = True

        c += 1

    return one and two

nice = 0
naughty = 0

for string in data:
    if check(string):
        nice += 1
    else:
        naughty += 1

print('Count nice:', nice, 'naughty:', naughty, 'of total', len(data))

# test = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']
# for x in test:
#     print(x, 'is', 'nice' if check(x) else 'naughty')
# 
