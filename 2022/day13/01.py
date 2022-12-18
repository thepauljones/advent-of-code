from pathlib import Path
import ast

script_location = Path(__file__).absolute().parent
file_location = script_location / 'test-data.dat'
file = file_location.open()

rawData = file.read().splitlines()

pair = []
pairs = []
for line in rawData:
    if line == '':
        pairs.append(pair)
        pair = []
    else:
        pair.append(ast.literal_eval(line))

pairs.append(pair)

def evaluatePair(couple):
    for left, right in couple:
        if type(left) is int and type(right) is int:
            return left < right

        if type(left) is list and type(right) is int:
            right = list(right)

        if type(left) is int and type(right) is list:
            left = list(left)

        return evaluatePair((left, right))


def evaluatePairs(testData):
    results = []
    for left, right in testData:

        if type(left) is int and type(right) is int:
            results.append(left < right)

        if type(left) is list and type(right) is int:
            right = list(right)

        if type(left) is int and type(right) is list:
            left = list(left)
        
        if type(left) is list and type(right) is list:
            for i in range(len(left)):
                results.append(evaluatePair((left, right)))

        results.append(True)

    print(results)


evaluatePairs(pairs)

def solve():
    return 0


def test():
    assert solve() == 0
