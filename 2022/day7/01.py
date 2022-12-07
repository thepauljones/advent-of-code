from pathlib import Path
from treelib import Node, Tree

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = file.read().splitlines()

script_location = Path(__file__).absolute().parent
file_location = script_location / 'test-data.dat'
file = file_location.open()

test_data = file.read().splitlines()

class File(object):
        def __init__(self, size, element_type):
            self.size = size
            self.element_type = element_type


tree = Tree()
tree.create_node("/", "/", data=File(0, 'dir'))
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
            tree.create_node(elems[1], pwd + '/' + elems[1], parent=pwd, data=File(0, 'dir'))
        else:
            tree.create_node(elems[1], pwd + '/' + elems[1], parent=pwd, data=File(elems[0], 'file'))

def getSize(dirNode, size = 0):
    for child in tree.children(dirNode.identifier):
        if child.data.element_type == 'dir':
            size += getSize(child, size)
        else:
            size += int(child.data.size)

    return size


def solve(data):
    for command in data:
        parse_command(command)

    tree.show()

    sizes = []
    for directory in tree.filter_nodes(lambda x: x.data.element_type == 'dir'):
        size = getSize(directory)

        if size <= 100000:
            sizes.append(size)
        
    print(sum(sizes))
    
solve(data)
