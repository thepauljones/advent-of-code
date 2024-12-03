from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

regex = re.compile(r"mul\(\d+,\d+\)")


all = regex.findall(data)

answer = 0
for sum in all:
    one, two = sum.split(",")
    numOne = one.split("mul(")[1]
    numTwo = two.split(")")[0]

    print(int(numOne),  int(numTwo))

    answer += int(numOne) * int(numTwo)


print(answer)
