from pathlib import Path
import re
import sys
from termcolor import colored, cprint
from threading import Timer

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.read().splitlines()


def solve():

solve()
