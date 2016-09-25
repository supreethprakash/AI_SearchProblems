from heuristics import *
from generateAdjoints import *


def toString(obj):
    return '\n'.join([''.join([str(col) + ' ' for col in row]) for row in obj])


def getMinimumElement(openset, fScore):
    minScore = 2 ** 30
    minElem = None
    for elem in openset:
        if elem in fScore.keys() and fScore[elem] < minScore:
            minElem = elem
            minScore = fScore[elem]
    return minElem


def createMatrix(board, dimension):
    mat = []
    board = board.split(' ')
    for i in range(dimension):
        row = []
        for j in range(i * 4, (i + 1) * 4):
            if '\n' in board[j]:
                board[j] = board[j].strip('\n')
            row.append(int(board[j]))
        mat.append(row)
    return mat


def solve(board, goal, option):
    noOfStates = 0
    startState = toString(board)
    goalState = toString(goal)
    closedSet = []
    openset = [startState]
    previousStates = {}

    gS = {startState: 0}
    if option == 1:
        fS = {startState: gS[startState] + misplacedTiles(board, goal)}
    else:
        fS = {startState: manhattan(board)}

    while len(openset) != 0:
        curState = getMinimumElement(openset, fS)
        if curState == goalState: return previousStates, curState, noOfStates
        currentMatrix = createMatrix(curState, 4)
        openset.remove(curState)
        closedSet.append(curState)
        adjoints = genAdjoints(currentMatrix)

        for eachNeighbor in adjoints:
            tentativeGs = gS[curState] + 1
            if option == 1:
                tentativeFs = tentativeGs + misplacedTiles(eachNeighbor, goal)
            else:
                tentativeFs = manhattan(eachNeighbor)

            neighborString = toString(eachNeighbor)

            if neighborString in closedSet and neighborString in fS and tentativeFs >= fS[neighborString]:
                continue

            if neighborString not in openset or (neighborString in fS and tentativeFs < fS[neighborString]):
                noOfStates += 1
                previousStates[neighborString] = curState
                gS[neighborString] = tentativeGs
                fS[neighborString] = tentativeFs

                if neighborString not in openset:
                    openset.append(neighborString)

    return 0, 0, 0
