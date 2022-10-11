import hashlib

count = 0

found = False
while found is False:
    i = 'iwrupvqb' + str(count)

    print(i)
    result = hashlib.md5(i.encode())

    first_five = result.hexdigest()[0:5]

    if first_five == '00000':
        found = True
        break

    count += 1

print(count)
