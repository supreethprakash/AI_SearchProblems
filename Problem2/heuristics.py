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