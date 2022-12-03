with open('data.dat') as file:
    raw_data = [line.strip() for line in file]

starting_pattern = raw_data[0]

# Create Polymer from starting polymer
Polymer = {}
for i in range(0, len(list(starting_pattern)) - 1):
    pair = ''.join([starting_pattern[i], starting_pattern[i+1]])
    if Polymer.get(pair):
        Polymer[pair] += 1
    else:
        Polymer[pair] = 1

# Parse rules of polymer proliferation
Code = {}
for i in range (2, len(raw_data)):
    pattern, insertion = raw_data[i].split(' -> ')
    Code[pattern] = insertion

def polymerize(Polymer):
    Result = {}
    for pair in Polymer:
        pair_count = Polymer[pair]

        first = pair[0] + Code[pair]
        second = Code[pair] + pair[1]

        if Result.get(first):
            Result[first] += pair_count
        else:
            Result[first] = pair_count

        if Result.get(second):
            Result[second] += pair_count
        else:
            Result[second] = pair_count

    return Result

def get_count_most_min_count_fewest(Result):
    CountChars = {}
    unique_chars = set(''.join(Result.keys()))

    for char in unique_chars:
        local_count = 0
        for pair in Result:
            if char == pair[1]:
                local_count += Result[pair]

        CountChars[char] = local_count

    sorted_chars = sorted(CountChars.items(), key=lambda x: x[1], reverse=True)

    return sorted_chars[0][1] - sorted_chars[len(sorted_chars) - 1][1]

def part_one(Polymer):
    Result = Polymer
    count = 0
    while count < 40:
        Result = polymerize(Result)
        count += 1

    total = 1
    for pair in Result:
        total += Result[pair]

    print(get_count_most_min_count_fewest(Result))

part_one(Polymer)

