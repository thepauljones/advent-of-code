from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'test-data.dat'
file = file_location.open()
test_data = file.read().splitlines()

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()
data = file.read().splitlines()


def parse(signal):
    numCols = len(signal[0])
    cols = []
    col = []

    for i in range(0, numCols):
        count = 0
        while count < len(signal):
            col.append(signal[count][i])
            count += 1

        cols.append(col)
        col = []

    count = 0
    max_count = 0

    result = [None] * numCols
    max_count = 0
    for col in cols:
        options = list(set(col))
        for opt in options:
            if col.count(opt) > max_count:
                max_count = col.count(opt)
                result[count] = opt

        count += 1
        max_count = 0

    return ''.join(result)


print(parse(data))


def test():
    result = parse(test_data)
    assert result == 'easter'


def test1():
    result = parse(data)
    assert result == 'afwlyyyq'
