import sys
from getBoard import getBoardPlacements
from permInversion import findPermuatationInv
from solve import solve
from traverse import discoverDir


def getFileName():
    #return 'tile.txt'
    return sys.argv[1]

def addArray(index):
    goalState = []
    for i in range(index, index+4):
        goalState.append(i+1)
    return goalState


def getGoalState(size):
    return [addArray(i) if i < size/4 * 3 else [i+1, i+2, i+3, 0] for i in range(0, size, 4)]


if __name__ == '__main__':
    print 'Read the file from command terminal\n'
    heuristicOption = input('Please Enter 1 for Heuristic 1(Misplaced Tiles) and 2 for Heuristic 2(Manhattan)\n')
    misplacedTiles = getBoardPlacements()
    if findPermuatationInv(misplacedTiles) == 1:
        print 'Not able to solve. Try a different Board'
    else:
        previousStates, curState, noOfStates = solve(misplacedTiles, getGoalState(16), int(heuristicOption))
    if previousStates == 0 or curState == 0 or noOfStates == 0:
        print 'Something is Wrong. Please Run again\n'
    else:
        path = discoverDir(previousStates, curState)
        print 'The moves are, \n'
        for i in range(len(path)):
            print path[i],
        print '\n\nTotal Number of states generated', noOfStates