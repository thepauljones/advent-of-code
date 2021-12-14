from collections import OrderedDict

with open('data.dat') as file:
    raw_data = [line.strip() for line in file]

starting_pattern = raw_data[0]

Code = {}
for i in range (2, len(raw_data)):
    pattern, insertion = raw_data[i].split(' -> ')
    Code[pattern] = insertion

def perform_insertion_on_pair(pair, insertion):
    chars = list(pair)
    return ''.join([chars[0], insertion])


def apply_pattern(pattern):
    updated_pattern = ''
    for i in range(0, len(list(pattern)) - 1):
        pair = ''.join([pattern[i], pattern[i + 1]])
        updated_pattern += perform_insertion_on_pair(pair, Code[pair])

    updated_pattern += list(pattern)[len(list(pattern)) - 1]

    return updated_pattern

def get_count(pattern, count_type = 'Most'):
    chars = list(pattern)
    Count = {}
    for char in pattern:
        if Count.get(char):
            Count[char] += 1
        else:
            Count[char] = 1

    ordered = OrderedDict(sorted(Count.items())).items()

    most = (' ', 0)
    fewest = (' ', 9999999)

    for pair in Count.items():
        letter = pair[0]
        count = pair[1]
        print(letter, count)
        if count > most[1]:
            most = (letter, count)
        if count < fewest[1]:
            fewest = (letter, count)

    print(most)
    print(count)

    return most[1] if count_type == 'Most' else fewest[1]


def part_one():
    result = starting_pattern
    count = 0
    while count < 10:
        result = apply_pattern(result)
        print(count + 1, 'times', len(result))
        count = count + 1

    count_most = get_count(result)
    count_fewest = get_count(result, 'Fewest')

    print(count_most - count_fewest)

part_one()

