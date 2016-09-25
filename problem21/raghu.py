from copy import deepcopy
import heapq

def readfile(filename):
    try:
        with open(filename,"r") as file:
            text = file.read().replace('\n', ' ')
            file.close()
        return text
    except IOError:
        print('Enter correct filename!')
        return

def swap(start,r1,c1,r2,c2):
    term = start[r1][c1]
    start[r1][c1] = start[r2][c2]
    start[r2][c2] = term
    return start

def is_goal(goal,current):
    for r in range(4):
        for c in range(4):
            if goal[r][c] != current[r][c]:
                return False
    return True

def heuristic_cost(start):
        totalSum = 0
        for r in range(4):
            for c in range(4):
                n = start[r][c] - 1
                if n is not 0:
                    r_solved = abs(r - n / 4)
                    c_solved = abs(c - n % 4)
                    totalSum += r_solved + c_solved
        return totalSum

def heuristic_cost_1(start,goal):
        totalSum = 0
        circularSum = 0
        cost = 0
        s = 0
        '''for r in range(4):
            for c in range(4):
                if start[r][c] != goal[r][c]:
                    totalSum += 1'''
        for r in range(4):
            for c in range(4):
                n = start[r][c] - 1
                if n != -1:
                    r_solved = abs(r - n / 4)
                    c_solved = abs(c - n % 4)
                    totalSum += r_solved + c_solved
                    s = r_solved + c_solved
                    if s == 6:
                        circularSum += s/3
                    else:
                        circularSum += (s % 3) + 1

                else:
                    r_solved = abs(r - 15 / 4)
                    c_solved = abs(c - 15 % 4)
                    totalSum += r_solved + c_solved
                    s = r_solved + c_solved
                    if s == 6:
                        circularSum += s/3
                    else:
                        circularSum += (s % 3) + 1

        cost = min(totalSum,circularSum)
        return cost


def heuristic_cost_2(start,goal):
        totalSum = 0
        for r in range(4):
            for c in range(4):
                if start[r][c] != goal[r][c]:
                    totalSum += 1
        return totalSum

def neighbors(start):
        #print start
        neighbors = []
        w = 4
        h = 4
        for r in range(h):
            for c in range(w):
                if (start[r][c] == 0):
                    if (r == 0):
                        neighbor = deepcopy(start)
                        neighbor = swap(neighbor, r, c, h - 1, c)
                        neighbors.append((neighbor,'D'))
                    if (r == h - 1):
                        neighbor = deepcopy(start)
                        neighbor = swap(neighbor, r, c, 0, c)
                        neighbors.append((neighbor,'U'))
                    if (c == 0):
                        neighbor = deepcopy(start)
                        neighbor = swap(neighbor, r, c, r, w - 1)
                        neighbors.append((neighbor,'R'))
                    if (c == w - 1):
                        neighbor = deepcopy(start)
                        neighbor = swap(neighbor, r, c, r, 0)
                        neighbors.append((neighbor,'L'))
                    if (r != 0):
                        neighbor = deepcopy(start)
                        neighbor = swap(neighbor, r, c, r - 1, c)
                        neighbors.append((neighbor,'U'))
                    if (r != h - 1):
                        neighbor = deepcopy(start)
                        neighbor = swap(neighbor, r, c, r + 1, c)
                        neighbors.append((neighbor,'D'))
                    if (c != 0):
                        neighbor = deepcopy(start)
                        neighbor = swap(neighbor, r, c, r, c - 1)
                        neighbors.append((neighbor,'L'))
                    if (c != w - 1):
                        neighbor = deepcopy(start)
                        neighbor = swap(neighbor, r, c, r, c + 1)
                        neighbors.append((neighbor,'R'))
        return neighbors



def create_matrix(board,dimension):
    mat = []
    board = board.split(' ')
    for x in range(dimension):
        row = []
        for y in range(x*4, (x+1)*4):
            row.append(int(board[y]))
        mat.append(row)
    return mat



def create_goal_state(dimension):
    mat = []
    for x in range(dimension):
        row = []
        for y in range(x*4, (x+1)*4):
            if y == 15:
                row.append(0)
            else:
                row.append(y+1)
        mat.append(row)
    return mat

def solve(board,goal):
    fringe = []
    h = heuristic_cost_1(board,goal)
    heapq.heappush(fringe,(h,board))
    min = h
    sol = []
    dir = []
    d = []
    sol.append(board)

    while(len(fringe) > 0):

        best = []

        for s in neighbors(heapq.heappop(fringe)[1]):
            if is_goal(goal,s[0]):
                sol.append(s[0])
                dir.append(s[1])
                return sol,dir
            if s[0] not in fringe:
                mini = heuristic_cost_1(s[0],goal)

                if mini <= min:
                    best = s[0]
                    d = s[1]
                    min = mini
                    if (min,best) not in fringe:
                        heapq.heappush(fringe,(min,best))
        sol.append(best)
        if len(d) > 0:
            dir.append(d)
    return 0, 0

text = readfile('tile.txt')
board = create_matrix(text,4)
#print board
goal = create_goal_state(4)
x,y = solve(board,goal)

if x == 0:
    print "Unsolvable"
else:
    print "Solution:"
    for j in x:
        for m in j:
            for n in m:
                print n,
            print
        print " "

    for i in y:
        print i,