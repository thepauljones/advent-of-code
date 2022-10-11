import hashlib

count = 0

found = False
while found is False:
    i = 'iwrupvqb' + str(count)

    result = hashlib.md5(i.encode())

    first_five = result.hexdigest()[0:6]

    if first_five == '000000':
        found = True
        break

    count += 1

print(count)
