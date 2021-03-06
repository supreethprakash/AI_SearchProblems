from copy import deepcopy
from math import sqrt
import sys
# This is the graph of all cities.

def cityGPS(fileName):
    dict = {}
    f = open(fileName,'r')
    temp = [line.split(' ',) for line in [line.rstrip('\n') for line in f ]]
    for i in temp:
        if i[0] not in dict:
            dict[i[0]] = i[1:]
    f.close()
    #print dict
    return dict

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
        tup = tup + ((int(i[2])/(int(i[3])* 1.0)) * 60.0,)
        if int(i[3]) >= 55:
            tup = tup + (0,)
        else:
            tup = tup + (1,)
        graph[i[0]].append(tup)

        if i[1] not in graph:
            graph[i[1]] = []
        if i[3] == '':
            i[3] = '10'

        if int(i[3]) >= 55:
            a = 0
        else:
            a = 1
        graph[i[1]].append((i[0], int(i[2]), int(i[3]), i[4], (int(i[2]) / (int(i[3])* 1.0)) * 60.0, a))

    #for key, val in graph.iteritems():
        #print key , ':', val
    return graph

def isgoal(start, destination, i):
    return i[0] == start and i[-1] == destination

#For min distance, segment, time
def heuristic(graph,node,end,ch):
    if node not in graph or end not in graph:
        return 0
    if ch == 2:
        return sqrt((float(graph[end][0]) - float(graph[node][0]))**2 +\
                    (float(graph[end][1]) - float(graph[node][1]))**2)/25
    return sqrt((float(graph[end][0]) - float(graph[node][0])) ** 2 + \
                (float(graph[end][1]) - float(graph[node][1])) ** 2)

# A*
def solve3(graph, start, destination,gps,ch):
    visited = {start:0}
    stack = [[[start],[0,heuristic(gps,start,destination,ch)]]]
    result = [[],99999]
    while stack:
        #print "stack = ", stack
        index = 0
        for i in stack:
            if i[1][1] < stack[index][1][1]:
                index = stack.index(i)
        v = stack.pop(index)
        if result[1] > v[1][1]:
            if isgoal(start, destination, v[0]):
                result[0]=v[0]
                result[1]=v[1][0]
                if ch == 0:
                    return result
            else:
                for i in successor3(v, graph,visited,gps,destination,ch**2):
                    stack.append(i)
    return result

def successor3(node, graph,visited,gps,destination,ch):
    if ch == 0: c = 1
    else: c = ch
    temp = graph[node[0][-1]]
    s = []
    for i in temp:
        if i[0] not in visited:
            visited[i[0]] = 99999
        elif node[1][0]+i[c] >= visited[i[0]]:
            continue
        k = deepcopy(node)
        k[0].append(i[0])
        k[1][0] += i[c]
        visited[i[0]] = k[1][0]
        k[1][1] = k[1][0]+heuristic(gps,i[0],destination,ch)
        s.append(k)
    #print s
    return s


#for time and distance routing option
def solve2(graph, start, destination, choice,ch, depth):
    visited = {start:0}
    stack = [[[start], 0]]
    result = [[],99999]
    while stack:
        #print "stack = ", stack
        if choice == 0:
            v = stack.pop(0)
        else:
            v = stack.pop()
            if choice == 2:
                if len(v[0]) == depth:
                    continue
        for i in successor2(v, graph,visited,ch**2):
            if result[1] > i[1]:
                if isgoal(start, destination, i[0]):
                    result = i
                else:
                    stack.append(i)
    #print visited
    return result

def successor2(node, graph,visited,ch):
    temp = graph[node[0][-1]]
    s = []
    for i in temp:
        if i[0] not in visited:
            visited[i[0]] = 99999
        elif node[1]+i[ch] >= visited[i[0]]:
            continue
        k = deepcopy(node)
        k[0].append(i[0])
        k[1] += i[ch]
        visited[i[0]] = k[1]
        s.append(k)
    #print s
    return s

#for segment routing option
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
    fileName2 = "city-gps.txt"
    fileName = "road-segments.txt"
    graph = createGraph(fileName)
    gps = cityGPS(fileName2)
    routing_option = int(sys.argv[3])
    routing_algo = int(sys.argv[4])
    starting = sys.argv[1]
    destination = sys.argv[2]
    d = 10
    if routing_algo == 3:
        a = solve3(graph,starting,destination,gps,routing_option)
        print a[1], " ", a[0]
    else:
        if routing_option == 1 or routing_option == 2:
            a = solve2(graph, starting, destination, routing_algo, routing_option, d)
            if routing_algo == 2:
                while len(a[0]) == 0:
                    d += 1
                    a = solve2(graph, starting, destination, routing_algo,routing_option, d)
            print a[1], " ", a[0]
        else:
            a = solve(graph, starting, destination, routing_algo, d)
            if routing_algo == 2:
                while len(a) == 0:
                    d += 1
                    a = solve(graph, starting, destination, routing_algo, d)
            print a

    '''
    #following code finds minimum distance from Bloomington,_Indiana to the farthest city using A*
    farthest = 0.0
    city1 = "Bloomington,_Indiana"
    city2 = ""
    for i in gps:
        d = heuristic(gps,city1,i,1)
        if d > farthest:
            farthest = d
            city2 = i
    print solve3(graph, city1, city2, gps, 1)
    '''
