from pathlib import Path
from treelib import Node, Tree

total_drive_size = 70000000

required = 30000000

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = file.read().splitlines()

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
            size = getSize(child, size)
        else:
            size += int(child.data.size)

    return size


def getUsedSpace():
    used = 0

    for node in tree.all_nodes():
        used += int(node.data.size)

    return used

def solve(data):
    for command in data:
        parse_command(command)

    used = getUsedSpace()
    print('USED', used)
    unused = total_drive_size - used

    print('UNUSED', unused)

    min_delete = required - unused

    print('MIN ', unused + min_delete)

    sizes = []
    for node in tree.all_nodes():
        size = getSize(node)

        if size >= min_delete:
            sizes.append(size)

    sizes.sort()
    print(sizes[0])

solve(data)
