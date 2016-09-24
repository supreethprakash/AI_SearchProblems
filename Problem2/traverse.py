def findPath(prev, cur):
    if cur in prev:
        p = findPath(prev, prev[cur])
        return p + [cur]
    else:
        return [cur]


def findZero(board):
    from solve import createMatrix
    boardMatrix = createMatrix(board, 4)
    return [[i, j] for i, sublists in enumerate(boardMatrix) for j, value in enumerate(sublists) if value == 0]


def getDirection(solution):
    solutionLength = len(solution)
    direction = []
    for i in range(1, solutionLength):
        rowCol = findZero(solution[i - 1])
        row1,col1 = rowCol[0][0], rowCol[0][1]
        rowCol = findZero(solution[i])
        row2,col2 = rowCol[0][0], rowCol[0][1]
        if row1 == row2:
            if col1 - col2 > 0:
                direction.append('L')
            else:
                direction.append('R')
        else:
            if row1 - row2 > 0:
                direction.append('U')
            else:
                direction.append('D')

    return direction


def discoverDir(prev, cur):
    return getDirection(findPath(prev, cur))
