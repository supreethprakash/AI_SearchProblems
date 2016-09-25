from copy import deepcopy
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
                i[3] = '25'
            if j.isdigit():
                tup = tup + (int(j),)
            else:
                tup = tup + (j,)
        if int(i[3]) == 0:
            i[3] = 25
        tup = tup + ((int(i[2])/(int(i[3])* 1.0)),)
        graph[i[0]].append(tup)

        if i[1] not in graph:
            graph[i[1]] = []
        if i[3] == '':
            i[3] = '10'
        graph[i[1]].append((i[0], int(i[2]), int(i[3]), i[4], (int(i[2]) / (int(i[3])* 1.0))))

    return graph


def isgoal(start, destination, i):
    return i[0] == start and i[-1] == destination


def solve2(graph, start, destination,choice,depth):
    visited = {start:0}
    stack = [[[start], 0]]
    max = 99999
    result = [[],99999]
    while stack:
        #print "stack = ", stack
        if choice == 0:
            v = stack.pop(0)
        else:
            v = stack.pop()
            if choice == 2:
                if len(v) == depth:
                    continue
        for i in successor2(v, graph,visited):
            if isgoal(start, destination, i[0]):
                if result[1] > i[1]:
                    result = i
            elif max > i[1] and result[1] > i[1]:
                stack.append(i)

    return result

def successor2(node, graph,visited):
    temp = graph[node[0][-1]]
    s = []
    for i in temp:
        if i[0] not in visited or node[1]+i[1] < visited[i[0]]:
            k = deepcopy(node)
            #print k
            k[0].append(i[0])
            #print k
            #print "k1= ",k[1],"node1=",node[1],"i1=",i[1]
            k[1] += i[1]
            #print k[1]
            s.append(k)
    #print s
    return s



def solve(graph, start, destination, choice, depth):
    visited = [start]
    stack = [[start]]
    while stack:
        if choice == 0:
            v = stack.pop(0)
        else:
            v = stack.pop()
            if choice == 2:
                if len(v) == depth:
                    continue
        for i in successor(v, graph, visited):
            if isgoal(start, destination, i):
                return i
            else:
                visited.append(i[-1])
                stack.append(i)
    return []


def successor(node, graph, visited):
    temp = graph[node[-1]]
    s = []
    for i in temp:
        if i[0] not in visited:
            k = list(node)
            k.append(i[0])
            s.append(k)

    return s

if __name__ == '__main__':
    fileName = "road-segments.txt"
    graph = createGraph(fileName)
    starting = "Indianapolis,_Indiana"
    destination = "Bloomington,_Indiana"
    #print solve2(graph, starting, destination)
    d = 10
    ch = 1
    a = solve2(graph, starting, destination, ch, d)
    if ch == 2:
        while len(a) == 0:
            d += 1
            a = solve(graph, starting, destination, ch, d)
    print a
