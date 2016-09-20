'''
Author: Supreeth (skeragod@indiana.edu)
Python code to solve the 16 tile puzzle problem
Input: Text file to read the randomized input
Output: Solved Puzzle and the number of steps that it took
'''
import sys
from copy import deepcopy
import heapq


def getFileName():
    return 'tile.txt'
    #return sys.argv[1]


def readContents(fn):
    file = open(fn, mode='r')
    content = [int(i) for i in file.read().replace('\n', ' ').split()]
    return content, len(content)


def addArray(index):
    goalState = []
    for i in range(index, index+4):
        goalState.append(i+1)
    return goalState


def getGoalState(size):
    return [addArray(i) if i < size/4 * 3 else [i+1, i+2, i+3, 0] for i in range(0, size, 4)]


def findZero(board):
    return [[i, j] for i, sublists in enumerate(board) for j, value in enumerate(sublists) if value == 0]


def createNewBoards(fringeList, zeroPos):
    zerothRow = zeroPos[0][0]
    zerothCol = zeroPos[0][1]
    newBoard = []
    returnBoard = []
    swapPos = []
    for i in range(0, 8):
        addFringe = deepcopy(fringeList)
        newBoard.append(addFringe)
        if zerothCol != 0 and 'L' not in swapPos:
            newBoard[i][zerothRow][zerothCol - 1], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][zerothCol], newBoard[i][zerothRow][zerothCol - 1]
            swapPos.append('L')
            returnBoard.append((newBoard[i], 'L'))
            #print 'L', newBoard[i]

        elif zerothRow != 0 and 'U' not in swapPos:
            newBoard[i][zerothRow - 1][zerothCol], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow - 1][
                                                                                           zerothCol]
            swapPos.append('U')
            returnBoard.append((newBoard[i], 'U'))
            #print 'U', newBoard[i]


        elif zerothRow != 3 and 'D' not in swapPos:
            newBoard[i][zerothRow + 1][zerothCol], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow + 1][
                                                                                           zerothCol]
            swapPos.append('D')
            returnBoard.append((newBoard[i], 'D'))
            #print 'D', newBoard[i]


        elif zerothCol != 3 and 'R' not in swapPos:
            newBoard[i][zerothRow][zerothCol + 1], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow][
                                                                                           zerothCol + 1]
            swapPos.append('R')
            returnBoard.append((newBoard[i], 'R'))
            #print 'R', newBoard[i]


        elif zerothRow == 3 and 'DT' not in swapPos:
            newBoard[i][zerothRow - 3][zerothCol], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow - 3][
                                                                                           zerothCol]
            swapPos.append('DT')
            returnBoard.append((newBoard[i], 'U'))
            #print 'DT', newBoard[i]

        elif zerothRow == 0 and 'TD' not in swapPos:
            newBoard[i][zerothRow + 3][zerothCol], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow + 3][
                                                                                           zerothCol]
            swapPos.append('TD')
            returnBoard.append((newBoard[i], 'D'))
            #print 'TD', newBoard[i]

        elif zerothCol == 0 and 'RL' not in swapPos:
            newBoard[i][zerothRow][zerothCol + 3], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow][
                                                                                           zerothCol + 3]
            swapPos.append('RL')
            returnBoard.append((newBoard[i], 'L'))
            #print 'RL', newBoard[i]

        #elif zerothCol == 3 and 'LR' not in swapPos:
            newBoard[i][zerothRow][zerothCol - 3], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow][
                                                                                           zerothCol - 3]
            swapPos.append('LR')
            returnBoard.append((newBoard[i], 'R'))
            #print 'LR', newBoard[i]

    return returnBoard


def getOriginalBoard():
    contents = readContents(getFileName())
    return [contents[0][i:i + 4] for i in range(0, len(contents[0]), 4)]


def isGoal(lst):
    goalState = getGoalState(16)
    if len([x for x in goalState if x not in lst] + [x for x in lst if x not in goalState]) == 0:
        return True
    else:
        return False


def heuristicCost(start):
    totalSum = 0
    circularSum = 0
    cost = 0
    s = 0

    for r in range(4):
        for c in range(4):
            n = start[r][c] - 1
            if n != -1:
                r_solved = abs(r - n / 4)
                c_solved = abs(c - n % 4)
                totalSum += r_solved + c_solved
                s = r_solved + c_solved
                if s == 6:
                    circularSum += s / 3
                else:
                    circularSum += (s % 3) + 1

            else:
                r_solved = abs(r - 15 / 4)
                c_solved = abs(c - 15 % 4)
                totalSum += r_solved + c_solved
                s = r_solved + c_solved
                if s == 6:
                    circularSum += s / 3
                else:
                    circularSum += (s % 3) + 1

    cost = min(totalSum, circularSum)
    return cost


def swapTiles(board):
    fringe = []
    heurCost = heuristicCost(board)
    minimum = heurCost
    heapq.heappush(fringe, (heurCost, board))
    solution = [ ]
    direction = [ ]
    dir = [ ]
    solution.append(board)
    zerothPos = findZero(board)
    while( len(fringe) > 0 ):
        for s in createNewBoards(heapq.heappop(fringe)[1], zerothPos):
            if isGoal(s[0]):
                solution.append(s[0])
                direction.append(s[1])

                return solution, direction

            if s[0] not in fringe:
                min = heuristicCost(board)
                if min <= minimum:
                    bestSolution, dir = s[0], s[1]
                    minimum = min
                    if (minimum, bestSolution) not in fringe:
                        heapq.heappush(fringe, (minimum, bestSolution))
        solution.append(bestSolution)
        if len(dir) > 0:
            direction.append(dir)
        return 0, 0


#Main Function
if __name__ == '__main__':
    print 'Read the file from command terminal\n'
    misplacedTiles = getOriginalBoard()
    sol, dir = swapTiles(misplacedTiles)

    if sol == 0:
        print "Unsolvable"
    else:
        print "Solution:"
        for i in sol:
            for j in i:
                for k in j:
                    print k,
                print
            print " "

        for i in dir:
            print i,
