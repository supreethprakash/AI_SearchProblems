
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
        else:
            if i[3] == '':
                i[3] = '0'
            graph[i[1]].append((i[0], int(i[2]), int(i[3]), i[4]))

    #for key, val in graph.iteritems():
        #print key, ':', val

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
    stack = [start]
    while stack:
        v = stack.pop(0)
        if v[0] not in path:
            path = path + [v[0]]
            stack = graph[v[0]] + stack
        if destination in path:
            return path

#This won't work
def BFS(graph, start, end):
    start = (start, 0)
    temp_path = [start]
    queue = []
    queue.append(temp_path)

    while len(queue) > 0:
        tmp_path = queue.pop(0)
        temp_path = tmp_path[0]
        last_node = temp_path[len(temp_path) - 1]
        #print 'temp path', tmp_path
        if last_node == end:
            print "VALID_PATH : ", temp_path
        for link_node in graph[last_node]:
            if link_node not in temp_path:
                new_path = []
                new_path = temp_path + [link_node]
                queue.append(new_path)

    print queue


fileName = "road-segments.txt"
graph = createGraph(fileName)
sourceConnections = createDict(fileName)
starting = "Bloomington,_Indiana"
destination = "Indianapolis,_Indiana"
print(dfs(graph, starting, destination))
#BFS(graph, starting, destination)
#print(find_path(graph, starting,[]))
