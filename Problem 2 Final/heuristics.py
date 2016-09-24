def manhattan(board):
    totalSum = 0
    for row in range(4):
        for col in range(4):
            n = board[row][col] - 1
            if n == -1:
                n = 15
            totalSum += abs(row - n / 4) + abs(col - n % 4)
    return totalSum


def misplacedTiles(start, goal):
    totalSum = 0
    for r in range(4):
        for c in range(4):
            if start[r][c] != goal[r][c]:
                totalSum += 1
    return totalSum