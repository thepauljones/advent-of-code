with open('data.dat') as file:
    raw_data = [line.strip() for line in file]

# Alright, let's see if I can handle Graphs
G = {}

# Fill up a Dictionary with each node
# and all the nodes to which is can travel
# ihavenoideawhatimdoing.jpg
for line in raw_data:
    start, end = line.split('-')
    if isinstance(G.get(start), list):
        G[start].append(end)
    else:
        G[start] = [end]


    # FORGOT TO add the reverse relationship
    # for too long here, this was the major FUCK UP
    if isinstance(G.get(end), list):
        G[end].append(start)
    else:
        G[end] = [start]

# Graph algorithm to get all paths in a graph
# augmented to disallow multiple traversals of lower
# case nodes
def get_path_from(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return [path]

    if not graph.has_key(start):
        return []

    paths = []

    for node in graph[start]:
        if node not in path or not node.islower():
            newpaths = get_path_from(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths

def may_join_path(node, path):
    if node.islower() and not node == 'start' and not node == 'end':
        already_contains_two_of_a_lowercase_node = False
        for internal_node in path:
            if path.count(internal_node) > 1 and internal_node.islower():
                already_contains_two_of_a_lowercase_node = True

        if not already_contains_two_of_a_lowercase_node:
            return True

    return node not in path or not node.islower()

# print(may_join_path('b', ['start', 'b', 'A', 'd', 'c', 'e', 'D', 'D']))

# Like the above graph path finder
# but uses the custom checker function may_join_path
# which allows lowercase caves twice a SINGLE time
def get_path_from_with_twist(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return [path]

    if not graph.has_key(start):
        return []

    paths = []

    for node in graph[start]:
        if may_join_path(node, path):
            newpaths = get_path_from_with_twist(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths

def part_one(graph):
    paths = []
    paths.append(get_path_from(graph, 'start', 'end', []))
    print(len(paths[0]))

def part_two(graph):
    paths = []
    paths.append(get_path_from_with_twist(graph, 'start', 'end', []))
    print(len(paths[0]))

part_one(G)
part_two(G)
