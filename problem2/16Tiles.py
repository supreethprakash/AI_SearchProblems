'''
Author: Supreeth (skeragod@indiana.edu)
Python code to solve the 16 tile puzzle problem
Input: Text file to read the randomized input
Output: Solved Puzzle and the number of steps that it took
'''
import sys


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

def createNewBoards(zeroPos):
    zerothRow = zeroPos[0][0]
    zerothCol = zeroPos[0][1]
    newBoard = []
    swapPos = []
    print(getOriginalBoard())
    for i in range(0, 8):
        newBoard.append(getOriginalBoard())
        if zerothCol != 0 and 'L' not in swapPos:
            newBoard[i][zerothRow][zerothCol - 1], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow][
                                                                                           zerothCol - 1]
            swapPos.append('L')
            print 'L', newBoard[i]

        elif zerothRow != 0 and 'U' not in swapPos:
            newBoard[i][zerothRow - 1][zerothCol], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow - 1][
                                                                                           zerothCol]
            swapPos.append('U')
            print 'U', newBoard[i]


        elif zerothRow != 3 and 'D' not in swapPos:
            newBoard[i][zerothRow + 1][zerothCol], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow + 1][
                                                                                           zerothCol]
            swapPos.append('D')
            print 'D', newBoard[i]


        elif zerothCol != 3 and 'R' not in swapPos:
            newBoard[i][zerothRow][zerothCol + 1], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow][
                                                                                           zerothCol + 1]
            swapPos.append('R')
            print 'R', newBoard[i]


        elif zerothRow == 3 and 'DT' not in swapPos:
            newBoard[i][zerothRow - 3][zerothCol], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow - 3][
                                                                                           zerothCol]
            swapPos.append('DT')
            print 'DT', newBoard[i]

        elif zerothRow == 0 and 'TD' not in swapPos:
            newBoard[i][zerothRow + 3][zerothCol], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow + 3][
                                                                                           zerothCol]
            swapPos.append('TD')
            print 'TD', newBoard[i]

        elif zerothCol == 0 and 'RL' not in swapPos:
            newBoard[i][zerothRow][zerothCol + 3], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow][
                                                                                           zerothCol + 3]
            swapPos.append('RL')
            print 'RL', newBoard[i]

        elif zerothCol == 3 and 'LR' not in swapPos:
            newBoard[i][zerothRow][zerothCol - 3], newBoard[i][zerothRow][zerothCol] = newBoard[i][zerothRow][
                                                                                           zerothCol], \
                                                                                       newBoard[i][zerothRow][
                                                                                           zerothCol - 3]
            swapPos.append('LR')
            print 'LR', newBoard[i]


def getOriginalBoard():
    contents = readContents(getFileName())
    return [contents[0][i:i + 4] for i in range(0, len(contents[0]), 4)]


def swapTiles(board):
    zerothPos = findZero(board)
    createNewBoards(zerothPos)


#Main Function
if __name__ == '__main__':
    print 'Read the file from command terminal\n'
    misplacedTiles = getOriginalBoard()
    swapTiles(misplacedTiles)
    #print getGoalState(contents[1])