with open('data.dat') as file:
    data = [line.strip() for line in file]

vow = 'aeiou'
unwanted = ['ab', 'cd', 'pq', 'xy']

def check(i):
    global vow, unwanted
    v = 0
    c = 0
    n = 0
    d = False
    for x in i:
        n += 1
        if x in vow:
            v += 1

        if n < len(i) and x == i[n]:
            d = True

        c += 1

    u = False

    for x in unwanted:
        if x in i:
            u = True

    nice = v > 2 and d and not u

    print(i, 'is', 'nice' if nice else 'naughty')

    return nice


nice = 0
naughty = 0

for string in data:
    if check(string):
        nice += 1
    else:
        naughty += 1

print('Count nice:', nice, naughty)
print('count', len(data))

# Test strings
