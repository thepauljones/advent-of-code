from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = file.read().splitlines()

snapshots = []
for i in range(20, 221, 40):
    snapshots.append(i)

X = 1
time = 0
buffer = 0
sleep = 0
line = []
 
def tick(instruction = ''):
    global X
    global time
    global buffer
    global sleep
    global snapshots
    global line


    ins = [x for x in instruction.split(' ')]

    if ins[0] == 'noop':
        piss = 'wet'
    elif ins[0] == 'addx':
        buffer = int(ins[1])
        sleep = 2
    
    if sleep == 0:
        X += buffer
        buffer = 0

    time += 1
    sleep -= 1

    magic = time % 40
    if magic + 1 == X or magic - 1 == X or magic == X:
        line.append('#')
    else:
        line.append('.')

    if magic == 0:
        print(''.join(line))
        line = []
            

    return

def run_program(instructions):
    global sleep

    while len(instructions) > 0:
        if sleep > 0:
            sleep -= 1
            tick()
        tick(instructions.pop())


data.reverse()
run_program(data)


def test():
    assert solve() == 0
