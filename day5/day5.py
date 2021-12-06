from itertools import chain

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

with open('data.dat') as file:
    data = [line.strip() for line in file]

def get_lines(data):
    lines = []
    for line in data:
        current_line = line.split(' -> ')
        x1 = int(current_line[0].split(',')[0])
        y1 = int(current_line[0].split(',')[1])
                                              
        x2 = int(current_line[1].split(',')[0])
        y2 = int(current_line[1].split(',')[1])

        lines.append([Point(x1, y1), Point(x2, y2)])

    return lines[:]

def get_max_size(data):
    maxSize = 0
    for line in data:
        current_line = line.split(' -> ')
        x1 = current_line[0].split(',')[0]
        y1 = current_line[0].split(',')[1]
        
        x2 = current_line[1].split(',')[0]
        y2 = current_line[1].split(',')[1]

        candidates = map(int, [maxSize, x1, x2, y1, y2])

        maxSize = max(candidates)

    return int(maxSize)


def init_board(size):
    board = []
    for y in range(0, size + 1):
        board.append([])
        for _ in range(0, size + 1):
            board[y].append(0)

    return board

def add_line_to_board(line, board):
    start = line[0]
    end = line[1]
        
    # only horizontal and vertical lines allowed
    if not (start.x == end.x or start.y == end.y):
        print('REJECTED', start.x, start.y, end.x, end.y)
        return

    print('From ', start.x, start.y, ' to ', end.x, end.y)
    if (start.x == end.x):
        s = min(start.y, end.y)
        e = max(start.y, end.y)
        for y in range(s, e + 1):
            board[int(y)][int(start.x)] += 1
    else:
        s = min(start.x, end.x)
        e = max(start.x, end.x)
        for x in range(s, e + 1):
            board[int(start.y)][x] += 1

def print_board(board):
    for line in board:
        print(''.join(str(line)))
    
def print_points(points):
    for line in points:
        print(line[0].x, line[0].y, ' -> ', line[1].x, line[1].y)

def get_max(board):
    m = 0
    for line in board:
        for val in list(line):
            if (int(val) > m):
                m = int(val)

    return m

def count_instances(board):
    count = 0
    for line in board:
        for curr in list(line):
            if (curr > 1):
                count = count + 1

    return count


def part_one():
    max_size = get_max_size(data)
    board = init_board(max_size)
    lines = get_lines(data)

    for line in lines:
        add_line_to_board(line, board)

    return count_instances(board)

print(part_one())

