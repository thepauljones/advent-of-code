with open('data.dat') as file:
    data = [line.strip() for line in file]

def get_adjacent(j, i, data):
    adjs = []
    if (j < len(data) - 1):
        adjs.append(data[j+1][i])

    if (j >= 1):
        adjs.append(data[j-1][i])

    if (i < len(data[j]) - 1):
        adjs.append(data[j][i+1])

    if (i >= 1):
        adjs.append(data[j][i-1])
    
    return adjs

def get_non_9_adjacent_points(j, i, data):
    points = []
    if (j < len(data) - 1):
        if data[j+1][i] != '9':
            points.append((j+1, i))

    if (j >= 1):
        if data[j-1][i] != '9':
            points.append((j - 1, i))

    if (i < len(data[j]) - 1):
        if data[j][i+1] != '9':
            points.append((j, i + 1))

    if (i >= 1):
        if data[j][i-1] != '9':
            points.append((j, i - 1))
    
    return points

def contains_point(points, point):
    if points == None:
        return False

    for p in points:
        if p == point:
            return True

    return False

def fill_basin(basin, data):
    all_new_points = []
    for point in basin:
        new_points = get_non_9_adjacent_points(point[0], point[1], data)
        for point in new_points:
            if not contains_point(basin, point):
                basin.append(point)
                all_new_points.append(point)
    
    if len(all_new_points) == 0:
        return basin
    else:
        return fill_basin(basin, data)
            
def part_two():
    basins = []
    current_basin = []
    for j in range(0, len(data)):
        for i in range(0, len(data[0])):
            if (data[j][i] == '9'):
                continue

            point_safe = True
            for basin in basins:
                if contains_point(basin, (j, i)):
                    point_safe = False
                    break

            if point_safe:
                current_basin = fill_basin([(j, i)], data)
                basins.append(current_basin)


    sorted_basins = sorted(basins, key=len, reverse=True)
    return len(sorted_basins[0]) * len(sorted_basins[1] * len(sorted_basins[2]))

def part_one():
    low_points = []
    for j in range(0, len(data)):
        for i in range(0, len(data[0])):
            if data[j][i] < min(get_adjacent(j, i, data)):
                low_points.append(data[j][i])

    return sum(map(int, low_points))+len(low_points)

print(part_one())
print(part_two())
