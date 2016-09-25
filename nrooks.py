# nrooks.py : Solve the N-Rooks problem!
# D. Crandall, August 2016
#
# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.

# This is N, the size of the board.
N = 0
initial_board = [[0] * N] * N
indexList = []

# Count # of pieces in given row
def count_on_row(board, row):
    return sum(board[row])

#returns 1 or 0 based on the queens present in the right to left diagonal
def leftRightDiagonal(board, row, col):
    diffSum = row if row <= col else col
    r = row - diffSum
    c = col - diffSum

    while r < N and c < N:
        if board[r][c] == 1:
            return 0
        else:
            r = increment(r)
            c = increment(c)
    return 1

#returns 1 or 0 based on the queens present in the left to right diagonal
def rightLeftDiagonal(board, row, col):
    r = row
    c = col

    while r < N and c >=0:
        if board[r][c] is 1:
            return 0
        else:
            r = increment(r)
            c = decrement(c)

    while row >= 0 and col < N:
        if board[row][col] == 1:
            return 0
        else:
            row = decrement(row)
            col = increment(col)
    return 1

# Count # of pieces in given column
def count_on_col(board, col):
    return sum([row[col] for row in board])

#count diagonal elements in chess board
def countDiagonal(board):
    print sum([board[i][i] for i in range(len(board))])

# Count total # of pieces on board
def count_pieces(board):
    return sum([sum(row) for row in board])

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([" ".join(["R" if col else "_" for col in row]) for row in board])

def printable_boardqueen(board):
    return "\n".join([" ".join(["Q" if col else "_" for col in row]) for row in board])

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    addedPiece = board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]
    return addedPiece

def increment(i):
    return i+1

def decrement(i):
    return i-1

def addPieceMod(board, row):
    c = 0
    while(c < N):
        if(count_on_col(board, c) is 0):return add_piece(board, row, c)
        else:
            c = increment(c)

# Get list of successors of given board state
def successors(board):
    succFuncs = [add_piece(board, r, c) for r in range(0, N) for c in range(0,N)]
    return succFuncs

#Successor function that doesn't add N+1 rooks or if there's an already added moves.
def successors2(board):
    return [add_piece(board, r, c) for r in range(0, N) for c in range(0, N) if board[r][c] != 1 and count_pieces(board) <= N]

def checkValidity(board, row, col):
    if sum(board[row]) >= 1:
        return True
    else:
        return False

#successor3 function checks if there is a pawn either in the row or the column.
def successors3(board):
    return [add_piece(board, r, c) for r in range(0, N) for c in range(0, N) if board[r][c]!=1 and count_pieces(board) <= N and not checkValidity(board, r, c)]
    '''
    for r in range(0, N):
        for c in range(0, N):
            state = checkValidity(board, r, c)
            if not state:
                if board[r][c] != 1:
                    A = [add_piece(board, r, c)]
                    return [A]
                else:
                    return []
            else:
                return []
    #return [add_piece(board, r, c) if board[r][c] != 1 and count_pieces(board) <= N else removeRowCols(board, r, c) for r in range(0, N) for c in range(0, N)]
    '''

def successors4(board):
    return [add_piece(board, i, i) for i in range(len(board)) if 1 not in board[i]]

def successors5(board):
    return [addPieceMod(board, r) for r in range(0, N) if 1 not in board[r]]

def successorQueen(board):
    return [add_piece(board, r, c) for r in range(0, N) for c in range(0, N) if 1 not in board[r] and count_pieces(board) <= N and leftRightDiagonal(board, r, c) and rightLeftDiagonal(board, r, c)]

# check if board is a goal state
def is_goal(board):
    return count_pieces(board) == N and \
        all([count_on_row(board, r) <= 1 for r in range(0, N)]) and \
        all([count_on_col(board, c) <= 1 for c in range(0, N)])

#Adds an element to the list
def enqueue(fringe, s):
    fringe.append(s)

#removes from the first inserted element
def dequeue(fringe):
    return fringe.pop(0)

# Solve n-rooks!
def solve(initial_board, suc, rq):
    fringe = [initial_board]
    while len(fringe) > 0:
        if rq == 1:
            if suc == 1:
                for s in successors(dequeue(fringe)):
                    if is_goal(s):
                        return(s)
                    enqueue(fringe, s)
            elif suc == 2:
                for s in successors2(dequeue(fringe)):
                    if is_goal(s):
                        return(s)
                    enqueue(fringe, s)
            elif suc == 3:
                for s in successors4(dequeue(fringe)):
                    if is_goal(s):
                        return(s)
                    enqueue(fringe, s)
            else:
                for s in successors5(dequeue(fringe)):
                    if is_goal(s):
                        return(s)
                    enqueue(fringe, s)
        elif rq == 2:
            for s in successorQueen(dequeue(fringe)):
                if is_goal(s):
                    return (s)
                enqueue(fringe, s)
    return False

def solvedfs(initial_board, suc, rq):
    fringe = [initial_board]
    while len(fringe) > 0:
        if rq == 1:
            if suc == 1:
                for s in successors(fringe.pop()):
                    if is_goal(s):
                        return(s)
                    fringe.append(s)
            elif suc == 2:
                for s in successors2(fringe.pop()):
                    if is_goal(s):
                        return(s)
                    fringe.append(s)
            elif suc == 3:
                for s in successors4(fringe.pop()):
                    if is_goal(s):
                        return(s)
                    fringe.append(s)
            else:
                for s in successors5(fringe.pop()):
                    if is_goal(s):
                        return(s)
                    fringe.append(s)
        elif rq == 2:
            for s in successorQueen(fringe.pop()):
                if is_goal(s):
                    return (s)
                fringe.append(s)
    return False


# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
if __name__ == '__main__':
    N = int(input('Please Enter the number of N\n'))
    initial_board = [[0] * N] * N
    selection = int(input('Please enter 1 to check for BFS and 2 to check for DFS\n'))
    rookOrQueen= int(input('Press 1 for Rook and 2 for Queens\n'))

    if rookOrQueen == 1:
        successor = int(input('Please enter the successor function\n 1. Successor - Professors Function\n 2. Successors2 - Function for 2nd Question \n 3. Successors4 - Diagonal placement(for question 4)\n 4. Successors5 - For Question 4 (Main Approach)\n'))
    elif rookOrQueen == 2:
        successor = 5

    print "Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n"

    if selection == 1:
        solution = solve(initial_board, successor, rookOrQueen)
    else:
        solution = solvedfs(initial_board, successor, rookOrQueen)

    if rookOrQueen == 1:
        print printable_board(solution) if solution else "Sorry, no solution found. :("
    elif rookOrQueen == 2:
        print printable_boardqueen(solution) if solution else "Sorry, no solution found. :("


