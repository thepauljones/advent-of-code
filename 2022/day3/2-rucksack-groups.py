from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = file.read().splitlines()

codes = ['DUMMY', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


group = []
all_groups = []
for line in data:
    group.append(line)

    if len(group) == 3:
        all_groups.append(group)
        group = []


def get_common(group):
    dupes = []
    rucksack = group[0]
    for item in list(rucksack):
        if item in list(group[1]) and item in list(group[2]):
            dupes.append(codes.index(item))

    result =  list(set(dupes))
    result =[int(x) for x in result] 
    return result[0]

badges = []
for group in all_groups:
    badges.append(get_common(group))

print(sum(badges))

