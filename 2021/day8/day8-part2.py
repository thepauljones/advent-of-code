with open('data.dat') as file:
    data = [line.strip() for line in file]

def get_signal(line):
    return line.split(' | ')[0]

def get_code(line):
    return line.split(' | ')[1]

def get_overlap(code, test):
    return [x for x in code if x in test]

def get_topbar(key):
    return list(set(key[7]) - set(key[1]))[0]

def get_top_right(key):
    intersection_five_six = set(list(key[5]) + list(key[6]))
    return list(set(key[8]) - intersection_five_six)


def build_key(signal, key):
    for cypher in signal:
        cypher = ''.join(sorted(cypher))

        if len(cypher) == 2:
            key[1] = cypher
        if len(cypher) == 3:
            key[7] = cypher
        if len(cypher) == 4:
            key[4] = cypher
        if len(cypher) == 7:
            key[8] = cypher

    
    floaters = []
    for i in [2, 3, 5]:
        basis = ''.join(set(signal[3]).intersection(set(signal[4])).intersection(set(signal[5])))
        union = ''.join(set(signal[3]).union(set(signal[4])).union(set(signal[5])))
        floaters = ''.join(set(union).symmetric_difference(basis))

        four_and_seven = set(key[4]).union(set(key[7]))

        bottom_bar = ''.join(set(basis).difference(four_and_seven))
        top_bar = ''.join(set(key[7]).symmetric_difference(set(key[1])))
        cross_bar = ''.join(set(basis).difference(set([bottom_bar, top_bar])))

        bottom_left = ''.join(set(key[8]) - four_and_seven.union([bottom_bar]))
        top_left = ''.join(set(key[8]) - set(basis).union(set(key[1])).union([bottom_left]))

        key[i] = basis
        
    top_right = ''
    for i in [3, 4, 5]:
        if (bottom_left in signal[i]):
            top_right = ''.join(set(signal[i]) - set(basis).union([bottom_left]))

    bottom_right = ''.join(set(key[1]) - set([top_right]))

    # set awkwards
    key[0] = ''.join(set(key[8]) - set([cross_bar]))
    key[2] += bottom_left + top_right
    key[3] += top_right + bottom_right
    key[5] += top_left + bottom_right
    key[6] = key[5] + bottom_left
    key[9] = ''.join(set(key[8]) - set([bottom_left]))

codes = []
for line in data:
    key = []
    while len(key) < 10:
        key.append('')

    signal = line.split(' | ')[0].split()
    code = line.split(' | ')[1].split()

    build_key(sorted(signal, key=len), key)

    current_code = []
    for num in code:
        for i in range(0, len(key)):
            snum = ''.join(sorted(num))
            skey = ''.join(sorted(key[i]))
            if snum == skey:
                current_code.append(i)

    codes.append(''.join(map(str, current_code)))

total = 0
for code in codes:
    total += int(code)

print(total)
