'''
Author: Supreeth (skeragod@indiana.edu)
Python code to solve the 16 tile puzzle problem
Input: Text file to read the randomized input
Output: Solved Puzzle and the number of steps that it took
'''
import sys
from copy import deepcopy


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
    swapPos = []
    for i in range(0, 8):
        addFringe = deepcopy(fringeList)
        newBoard.append(addFringe)
        if zerothCol != 0 and 'L' not in swapPos:
            newBoard[i][zerothRow][zerothCol - 1], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow][
                                                                                           zerothCol - 1]
            swapPos.append('L')
            #print 'L', newBoard[i]

        elif zerothRow != 0 and 'U' not in swapPos:
            newBoard[i][zerothRow - 1][zerothCol], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow - 1][
                                                                                           zerothCol]
            swapPos.append('U')
            #print 'U', newBoard[i]


        elif zerothRow != 3 and 'D' not in swapPos:
            newBoard[i][zerothRow + 1][zerothCol], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow + 1][
                                                                                           zerothCol]
            swapPos.append('D')
            #print 'D', newBoard[i]


        elif zerothCol != 3 and 'R' not in swapPos:
            newBoard[i][zerothRow][zerothCol + 1], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow][
                                                                                           zerothCol + 1]
            swapPos.append('R')
            #print 'R', newBoard[i]


        elif zerothRow == 3 and 'DT' not in swapPos:
            newBoard[i][zerothRow - 3][zerothCol], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow - 3][
                                                                                           zerothCol]
            swapPos.append('DT')
            #print 'DT', newBoard[i]

        elif zerothRow == 0 and 'TD' not in swapPos:
            newBoard[i][zerothRow + 3][zerothCol], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow + 3][
                                                                                           zerothCol]
            swapPos.append('TD')
            #print 'TD', newBoard[i]

        elif zerothCol == 0 and 'RL' not in swapPos:
            newBoard[i][zerothRow][zerothCol + 3], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow][
                                                                                           zerothCol + 3]
            swapPos.append('RL')
            #print 'RL', newBoard[i]

        elif zerothCol == 3 and 'LR' not in swapPos:
            newBoard[i][zerothRow][zerothCol - 3], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow][
                                                                                           zerothCol - 3]
            swapPos.append('LR')
            #print 'LR', newBoard[i]
    return newBoard


def getOriginalBoard():
    contents = readContents(getFileName())
    return [contents[0][i:i + 4] for i in range(0, len(contents[0]), 4)]


def isGoal(lst):
    goalState = getGoalState(16)
    if len([x for x in goalState if x not in lst] + [x for x in lst if x not in goalState]) == 0:
        return True
    else:
        return False

def heuristicCost(lst):
    totalSum = 0
    for r in range(4):
        for c in range(4):
            n = lst[r][c] - 1
            if (n == -1):
                n = 15
            r_solved = n / 4
            c_solved = n % 4
            totalSum += abs(r - r_solved)
            totalSum += abs(c - c_solved)
    return totalSum


def swapTiles(board):
    fringe = [board]
    zerothPos = findZero(board)
    minimum = 9999
    bestOptions = []
    while(len(fringe) > 0):
        for s in createNewBoards(fringe.pop(), zerothPos):
            if isGoal(s):
                return s
            if s not in fringe:
                heurCost = heuristicCost(s)
                if heurCost < minimum:
                    minimum = heurCost
                    bestOptions = s
            fringe.append(bestOptions)
    return False


#Main Function
if __name__ == '__main__':
    print 'Read the file from command terminal\n'
    misplacedTiles = getOriginalBoard()
    print(swapTiles(misplacedTiles))
