from itertools import permutations

def get_perms(length):
    a = "+" * (length - 1) + "*"
    return list(set(["".join(p) for p in permutations(a)]))

print("".join(get_perms(6)))
