from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

RULES = {}
ACCEPTED = []

rule_input, input = file.read().split("\n\n")


def process_rule(rule):
    name, cinput = rule.split("{")
    cinput = cinput[:-1]

    conditions = cinput.split(",")

    RULES[name] = conditions


def unpack_part(p):
    result = {}
    bits = p[1:-1].split(",")
    for bit in bits:
        var, val = bit.split("=")
        result[var] = int(val)

    return result


def setup():
    for rule in rule_input.split("\n"):
        process_rule(rule)


def evaluate(condition, part):
    if "<" in condition:
        var, valI = condition.split("<")
        val = int(valI)
        if var in part:
            if part[var] < val:
                return True

    if ">" in condition:
        var, valI = condition.split(">")
        val = int(valI)
        if var in part:
            if part[var] > val:
                return True

    return False


def apply_rule(ruleKey, part):
    if ruleKey == "A":
        if part not in ACCEPTED:
            ACCEPTED.append(part)
        return
    if ruleKey == "R":
        return

    conditions = RULES[ruleKey][:]

    while len(conditions) > 0:
        condition = conditions.pop(0)
        if ":" in condition:
            cond, branch = condition.split(":")
            if evaluate(cond, part):
                apply_rule(branch, part)
                return
            else:
                continue

        else:
            apply_rule(condition, part)

    return


def process_part(p):
    part = unpack_part(p)
    apply_rule("in", part)


def solve():
    setup()

    for line in input.split("\n")[:-1]:
        process_part(line)

    answer = 0
    for i in ACCEPTED:
        for k in i.keys():
            answer += i[k]

    print()
    print(ACCEPTED)
    print("Answer: ", answer)


solve()
