from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()


def solve():
    print("test")


solve()
