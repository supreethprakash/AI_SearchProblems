import sys

def create_graph(fileName):
    graph = {}
    f = open(fileName,"r")
    temp = [line.split(' ',) for line in [line.rstrip('\n') for line in f ]]
    for i in temp:
        if i[0] not in graph:
            graph[i[0]]=[]
        for j in i[1:]:
            if j not in graph:
                graph[j] = []
            if j not in graph[i[0]]:
                graph[i[0]].append(j)
            if i[0] not in graph[j]:
                graph[j].append(i[0])
    f.close()
    del temp
    return graph

def successor(graph,node,table):
    flag = False
    for i in table:
        if len(table[i]) < N:
            for j in table[i]:
                if j in graph[node]:
                    flag = True
                    break
            if flag == False:
                table[i].append(node)
                return graph[node]
        flag = False
    table[len(table)+1] = [node]
    return graph[node]

def solve(graph):
    table = {}
    Aux = graph.keys()  # list of people not seated yet
    fringe = [Aux[0]]
    while len(fringe) > 0:
        node = fringe.pop(0)
        for s in successor(graph,node,table):
            if s not in fringe and s in Aux:
                fringe.append(s)
        Aux.remove(node)
    return table

fileName = sys.argv[1]
N = int(sys.argv[2])
graph = create_graph(fileName)
solution = solve(graph)
print solution
