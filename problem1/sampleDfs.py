graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F', 'M'],
         'F': ['C', 'E', 'M'],
         'M': ['F', 'E'],
         'G': ['K']}

def dfs_paths(graph, start, goal):
    paths = []
    stack = [(start, [start])]

    while stack:
        (vertex, path) = stack.pop(0)
        vertices = graph[vertex]

        for next_vertex in (set(vertices) - set(path)):
            new_path = path + [next_vertex]

            if next_vertex == goal:
                paths.append(new_path)
            else:
                stack.insert(0, (next_vertex, new_path))

    return paths

print dfs_paths(graph, 'A', 'D')
#[['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
'''
def dfs_paths_rec(graph, start, goal, path=[]):
    if start == goal:
        path.append(start)
        return path

    paths = []
    for next in set(graph[start]) - set(path):
        new_path = dfs_paths_rec(graph, next, goal, path + [next])
        paths.append(new_path)

    return paths

print dfs_paths_rec(graph, 'A', 'F')
'''