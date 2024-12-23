A = 59590048
B = 0
C = 9
output = []

p = "2,4,1,5,7,5,0,3,1,6,4,3,5,5,3,0"
program = [int(x) for x in p.split(",")]


def combo(n):
    if n < 4:
        return n

    if n == 4:
        return A

    if n == 5:
        return B

    if n == 6:
        return C

    return n


def run_program(program):
    global A, B, C, output
    pointer = 0

    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]

        pointer = operate(opcode, operand, pointer)

    print("A:", A, "B:", B, "C:", C)
    print("Output:", ",".join(output))


def operate(opcode, operand, pointer):
    global A, B, C, output
    if opcode == 0:
        A = A // 2 ** combo(operand)

    if opcode == 1:
        B = B ^ operand

    if opcode == 2:
        B = combo(operand) % 8

    if opcode == 3:
        if A != 0:
            return operand

    if opcode == 4:
        B = B ^ C

    if opcode == 5:
        output.append(str(combo(operand) % 8))

    if opcode == 6:
        B = A // 2 ** combo(operand)

    if opcode == 7:
        C = A // 2 ** combo(operand)

    return pointer + 2


run_program(program)
