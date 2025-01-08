from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.readlines()

tel_paths = {
    "7": {
        "7": "A",
        "8": ">A",
        "9": ">>A",
        "4": "vA",
        "5": "v>A",
        "6": "v>>A",
        "1": "vvA",
        "2": "vv>A",
        "3": "vv>>A",
        "0": "vvv>A",
        "A": "vvv>>A",
    },
    "8": {
        "7": "<A",
        "8": "A",
        "9": ">A",
        "4": "<vA",
        "5": "vA",
        "6": "v>A",
        "1": "<vvA",
        "2": "vvA",
        "3": "vv>A",
        "0": "vvvA",
        "A": "vvv>A",
    },
    "9": {
        "7": "<<A",
        "8": "<A",
        "9": "A",
        "4": "<<vA",
        "5": "<vA",
        "6": "vA",
        "1": "<<vvA",
        "2": "<vvA",
        "3": "vvA",
        "0": "<vvvA",
        "A": "vvvA",
    },
    "4": {
        "7": "^A",
        "8": ">^A",
        "9": ">>^A",
        "4": "A",
        "5": ">A",
        "6": ">>A",
        "1": "vA",
        "2 ": "v>A",
        "3": "v>>A",
        "0": "vv>A",
        "A": "vv>>A",
    },
    "5": {
        "7": "<^A",
        "8": "^A",
        "9": ">^A",
        "4": "<A",
        "5": "A",
        "6": ">A",
        "1": "<vA",
        "2": "vA",
        "3": "v>A",
        "0": "vvA",
        "A": "vv>A",
    },
    "6": {
        "7": "<<^A",
        "8": "<^A",
        "9": "^A",
        "4": "<<A",
        "5": "<A",
        "6": "A ",
        "1": "<<vA",
        "2": "<vA",
        "3": "vA",
        "0": "<vvA",
        "A": "vvA",
    },
    "1": {
        "7": "^^A",
        "8": ">^^A",
        "9": ">>^^A",
        "4": "^A",
        "5": ">^A",
        "6": ">>^A",
        "1": "A",
        "2": ">A",
        "3": ">>A",
        "0": "v>A",
        "A": "v>>A",
    },
    "2": {
        "7": "<^^A",
        "8": "^^A",
        "9": ">^^A",
        "4": "<^ A",
        "5": "^A",
        "6": ">^A",
        "1": "<A",
        "2": "A",
        "3": ">A",
        "0": "vA",
        "A": "v>A",
    },
    "3": {
        "7": "<<^^A",
        "8": "<^^A",
        "9": "^^A",
        "4": "<<^A",
        "5": "<^A",
        "6": "^A",
        "1": "<<A",
        "2": "<A",
        "3": "A",
        "0": "<vA",
        "A": "vA",
    },
    "0": {
        "7": "<^^^A",
        "8": "^^^A",
        "9": "^^^>A",
        "4": "<^^A",
        "5": "^^A",
        "6": "^^>A",
        "1": "^<A",
        "2": "^A",
        "3": ">^A",
        "0": "A",
        "A": ">A",
    },
    "A": {
        "7": "^^^<<A",  # done
        "8": "<^^^A",
        "9": "^^^A",
        "4": "^^<<A",  # done
        "5": "<^^A",
        "6": "^^A",
        "1": "^<<A",  # done
        "2": "<^A",
        "3": "^A",
        "0": "<A",
        "A": "A",
    },
}

dir_paths = {
    "^": {"^": "A", "A": ">A", "<": "v<A", "v": "vA", ">": "v>A"},  # done
    "<": {"^": ">^A", "A": ">>^A", "<": "A", "v": ">A", ">": ">>A"},  # done
    "v": {"^": "^A", "A": "^>A", "<": "<A", "v": "A", ">": ">A"},
    ">": {"^": "<^A", "A": "^A", "<": "<<A", "v": "<A", ">": "A"},
    "A": {"^": "<A", "A": "A", "<": "<<vA", "v": "<vA", ">": "vA"},
}


def get_buttons(f, t):
    return tel_paths[f][t]


def get_buttons_for_code(code, start="A"):
    test = start + code
    res = ""
    for i in range(len(test) - 1):
        res += get_buttons(test[i], test[i + 1])

    return res


def get_dir_buttons(f, t):
    return dir_paths[f][t]


def get_dir_buttons_for_code(code, start="A"):
    code = start + code
    res = ""
    for i in range(len(code) - 1):
        res += get_dir_buttons(code[i], code[i + 1])

    return res


def get_robot2_for_code(code):
    dirs = get_buttons_for_code(code)
    robot1 = get_dir_buttons_for_code(dirs)
    robot2 = get_dir_buttons_for_code(robot1)

    print(robot2)
    print(robot1)
    print(dirs)
    print(code)

    print((len(robot2)), "*", int(code[:-1]))
    return int(code[:-1]) * (len(robot2))


ans = 0
for code in data:
    ans += get_robot2_for_code(code.strip())
print(ans)
