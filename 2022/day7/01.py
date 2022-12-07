from pathlib import Path
from treelib import Node, Tree

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = file.read().splitlines()

class File(object):
        def __init__(self, size):
            self.size = size


tree = Tree()
tree.create_node("/", "/", data=File(0))
pwd = '/'

def parse_command(command):
    global pwd
    elems = command.split(' ')

    if elems[0] == '$':
        if elems [1] == 'cd':
            pwd = tree.parent(pwd).identifier if elems[2] == ".." else pwd + '/' + elems[2]

        if elems [1] == 'ls':
            return
    else:
        if elems[0] == 'dir':
            tree.create_node(elems[1], pwd + '/' + elems[1], parent=pwd, data=File(0))
        else:
            tree.create_node(elems[1], pwd + '/' + elems[1], parent=pwd, data=File(elems[0]))


def solve(data):
    for command in data:
        parse_command(command)

    tree.show(idhidden=False, data_property='size')

solve(data)

def test():
    assert solve() == 0

