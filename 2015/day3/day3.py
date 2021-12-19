with open('data.dat') as file:
    data = [line.strip() for line in file]

GiftMap = {}

x1 = 0
y1 = 0

x2 = 0
y2 = 0
counter = 1
for char in list(data[0]):
    if counter % 2 == 0:
        if char == '^': 
            y2 -=1
        if char == 'v': 
            y2 +=1
        if char == '<': 
            x2 -=1
        if char == '>':
            x2 +=1
        if GiftMap.get((x2, y2)):
            GiftMap[(x2, y2)] += 1
        else:
            GiftMap[(x2, y2)] = 1

    else:
        if char == '^': 
            y1 -=1
        if char == 'v': 
            y1 +=1
        if char == '<': 
            x1 -=1
        if char == '>':
            x1 +=1
        if GiftMap.get((x1, y1)):
            GiftMap[(x1, y1)] += 1
        else:
            GiftMap[(x1, y1)] = 1

    counter += 1

sorted(GiftMap)
print(len(GiftMap))
