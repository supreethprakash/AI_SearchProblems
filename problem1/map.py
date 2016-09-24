
# This dictionary contains all the cities and it's connections
def createDict(fileName):
    dict = {}
    f = open(fileName,'r')
    temp = [line.split(' ',) for line in [line.rstrip('\n') for line in f ]]
    for i in temp:
        str = ''
        if i[0] not in dict:
            dict[i[0]] = []
        for j in i[1:]:
            str += ', ' + j
        dict[i[0]].append(str[2:])

    return dict

    #for key, val in dict.iteritems():
        #print key, ':', val

# This is the graph of all cities.
def createGraph(fileName):
    graph = {}

    f = open(fileName, 'r')
    temp = [line.split(' ', ) for line in [line.rstrip('\n') for line in f]]
    for i in temp:
        tup = tuple()
        if i[0] not in graph:
            graph[i[0]] = []
        for j in i[1:5]:
            if not j:
                j = '25'
            if j.isdigit():
                tup = tup + (int(j),)
            else:
                tup = tup + (j,)
        graph[i[0]].append(tup)

        if i[1] not in graph:
            graph[i[1]] = []
        if i[3] == '':
            i[3] = '0'
        graph[i[1]].append((i[0], int(i[2]), int(i[3]), i[4]))

    for key, val in graph.iteritems():
        print key, ':', val

    return graph


#sample path from Src A - Dst B
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node[0] not in path:
            newpath = find_path(graph, node[0], end, path)
            if newpath: return newpath
    return None


#Finds the first found route between src and dest, need to tweak it a bit
def dfs(graph, start, destination, path=[]):
    allPaths = []
    start = (start, 0)
    stack = [graph[start]]
    while stack:
        v = stack.pop(0)
        if v[0] not in path:
            path = path + [v[0]]
            stack = graph[v[0]] + stack
        if destination in path:
            allPaths.append(path)
    return allPaths

def successor(node,graph):
    return graph[node]

def bfs(graph, start, destination, path=[]):
    allPath = []
    visited = [start]
    stack = []
    for i in successor(start,graph):
        if i not in stack:
            stack.append(i)
    while stack:
        v = stack.pop(0)
        visited.append(v)
        for i in successor(v, graph):
            if i not in stack and i is not in visited:
                stack.append(i)

        if destination in visited:
            allPath.append(visited)
    return allPath


fileName = "test1.txt"
graph = createGraph(fileName)
sourceConnections = createDict(fileName)
starting = "A"
destination = "E"
#a = dfs(graph, starting, destination)
#print(bfs(graph, starting, destination))
a = bfs(graph, starting, destination)
f = open('output.txt','a')
min_len = len(a[0])
min_path = a[0]
for item in a:
    if len(item) < min_len:
        min_path = item
        min_len = len(item)

print "min_len = ", min_len, ", path = ", min_path
f.close()
#print(find_path(graph, starting,[]))
