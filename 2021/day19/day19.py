with open('data.dat') as file:
    data = [line.strip() for line in file]

scanners = {}
current_scanner = ''
for line in data:
    if line.find('scanner') > -1:
        current_scanner = line
        scanners[current_scanner] = []
        continue

    if line == '':
        continue

    scanners[current_scanner].append(map(int, line.split(',')))

print(scanners['--- scanner 0 ---'])
