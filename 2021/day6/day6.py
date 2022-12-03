from collections import deque

with open('data.dat') as file:
    raw_data = file.read().split(',')

fish_data = list(map(int, map(str.strip, raw_data)))

def get_fish_count_after_days(days, data, debug = False):
    day = 0
    total_days = days

    while (day < total_days):
        if debug:
            print('Day: ', day + 1, ' : ', len(data))
        for i in range(0, len(data)):
            if (data[i] == 0):
                data.append(8)
                data[i] = 6
            else:
                data[i]-=1

        day += 1

    return len(data)


def get_efishent_count_after_days(days, data, debug = False):
    day = 0
    total_days = days

    age_bracket = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for age in data:
        age_bracket[age] += 1
       
    while (day < total_days):
        spawn = age_bracket.pop(0)
        age_bracket[6] += spawn
        age_bracket.append(spawn)

        if debug:
            print('Day: ', day + 1, ' : ', age_bracket, sum(age_bracket))

        day += 1

    return sum(age_bracket)

def part_one():
    print(get_fish_count_after_days(80, fish_data[:]))

def part_two():
    print(get_efishent_count_after_days(256, fish_data[:], True))

part_one()
part_two()
