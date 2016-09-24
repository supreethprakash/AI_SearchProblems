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

    #for key, val in graph.iteritems():
        #print key, ':', val

    return graph

def isgoal(start,destination,i):
    return i[0] == start and i[-1] == destination


def solve(graph, start, destination,choice, depth):
    path = []
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
        for i in successor(v, graph):
            if isgoal(start, destination, i):
                return i
            else:
                visited.append(i[-1])
                stack.append(i)
        #print stack
    return []


def successor(node, graph):
    temp = graph[node[-1]]
    s = []
    for i in temp:
        k = list(node)
        k.append(i[0])
        s.append(k)

    return s

if __name__ == '__main__':
    fileName = "road-segments.txt"
    graph = createGraph(fileName)
    starting = "Chicago,_Illinois"
    destination = "Bloomington,_Indiana"
    d = 10
    ch = 2
    a = solve(graph, starting, destination, ch, d)
    if ch == 2:
        while a == []:
            #print a
            d+=1
            a = solve(graph, starting, destination, ch, d)
    print a
