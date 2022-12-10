from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = file.read().splitlines()

snapshots = []
for i in range(20, 221, 40):
    snapshots.append(i)

X = 1
time = 1
buffer = 0
sleep = 0
 
add_line = []

answer = 0

def tick(instruction = ''):
    global X
    global time
    global buffer
    global sleep
    global snapshots
    global answer

    if time == 20:
        print(','.join(add_line))

    ins = [x for x in instruction.split(' ')]

    if ins[0] == 'noop':
        piss = 'wet'
    elif ins[0] == 'addx':
        buffer = int(ins[1])
        add_line.append(str(buffer))
        sleep = 2
    
    if sleep == 0:
        X += buffer
        buffer = 0


    time += 1
    sleep -= 1

    if time in snapshots:
        answer += time * X
        print('Clock:', time, ':', X)

    return

def run_program(instructions):
    global sleep
    global answer
    while len(instructions) > 0:
        if sleep > 0:
            sleep -= 1
            tick()
        tick(instructions.pop())

    print(answer)

data.reverse()
run_program(data)



def test():
    assert solve() == 0
