from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = file.read().splitlines()

codes = ['DUMMY', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

all_dupes = []
for line in data:
    halfway = len(line) // 2
    dupes = []
    first =list(line[0:halfway])
    second=list(line[halfway:])

    dupes = []
    for  x in first:
        if x in second:
            code = codes.index(x)
            if not code in dupes:
                dupes.append(code)

    for code in dupes:
        all_dupes.append(code)

print(sum(all_dupes))

