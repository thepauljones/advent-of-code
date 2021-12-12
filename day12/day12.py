with open('test-data.dat') as file:
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

def get_all_paths(graph):
    paths = []

    paths.append(get_path_from(graph, 'start', 'end', []))

    return paths

def part_one(graph):
    result = get_all_paths(graph)
    for line in result:
        print(line)

    print(len(result[0]))

part_one(G)
