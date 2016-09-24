def swap(board, row1, col1, row2, col2):
    temp = board[row1][col1]
    board[row1][col1] = board[row2][col2]
    board[row2][col2] = temp
    return board


def copy(board):
    from copy import deepcopy
    return deepcopy(board)


def genAdjoints(board):
    adjointList = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                if row == 0:
                    adjoint = copy(board)
                    adjoint = swap(adjoint, row, col, 3, col)
                    adjointList.append(adjoint)
                if row == 3:
                    adjoint = copy(board)
                    adjoint = swap(adjoint, row, col, 0, col)
                    adjointList.append(adjoint)
                if row != 0:
                    adjoint = copy(board)
                    adjoint = swap(adjoint, row, col, row - 1, col)
                    adjointList.append(adjoint)
                if row != 3:
                    adjoint = copy(board)
                    adjoint = swap(adjoint, row, col, row + 1, col)
                    adjointList.append(adjoint)
                if col == 0:
                    adjoint = copy(board)
                    adjoint = swap(adjoint, row, col, row, 3)
                    adjointList.append(adjoint)
                if col == 3:
                    adjoint = copy(board)
                    adjoint = swap(adjoint, row, col, row, 0)
                    adjointList.append(adjoint)
                if col != 0:
                    adjoint = copy(board)
                    adjoint = swap(adjoint, row, col, row, col - 1)
                    adjointList.append(adjoint)
                if col != 3:
                    adjoint = copy(board)
                    adjoint = swap(adjoint, row, col, row, col + 1)
                    adjointList.append(adjoint)

    return adjointList