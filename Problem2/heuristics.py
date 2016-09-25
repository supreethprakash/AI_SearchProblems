def manhattan(board):
    totalSum = 0
    for row in range(len(board)):
        for col in range(len(board)):
            n = board[row][col] - 1
            if n == -1:
                n = 15
            totalSum += abs(row - n / 4) + abs(col - n % 4)

    return totalSum


def misplacedTiles(board, goal):
    totalSum = 0
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] != goal[r][c]:
                totalSum += 1

    return totalSum


def manhattanMod(board):
    totalSum = 0
    circularSum = 0

    for r in range(4):
        for c in range(4):
            n = board[r][c] - 1
            if n != -1:
                r_solved = abs(r - n / 4)
                c_solved = abs(c - n % 4)
                totalSum += r_solved + c_solved
                if r_solved + c_solved == 6:
                    circularSum += (r_solved + c_solved) / 3
                else:
                    circularSum += ((r_solved + c_solved) % 3) + 1

            else:
                r_solved = abs(r - 15 / 4)
                c_solved = abs(c - 15 % 4)
                totalSum += r_solved + c_solved
                if r_solved + c_solved == 6:
                    circularSum += (r_solved + c_solved) / 3
                else:
                    circularSum += ((r_solved + c_solved) % 3) + 1

    return min(totalSum, circularSum)
