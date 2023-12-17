from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.read()


def hash(input):
    result = 0
    for char in input:
        result += ord(char)
        result *= 17
        result %= 256

    return result


ans = 0
for ins in data.strip().split(","):
    ans += hash(ins)

print(ans)


def solve():
    return 0


def test():
    assert solve() == 0
