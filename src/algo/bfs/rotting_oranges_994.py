from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    fresh = 1
    rotten = 2
    rows, cols = len(grid), len(grid[0])
    q = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == rotten:
                q.append([i, j])

    time = 0
    while len(q) > 0:
        for _ in range(len(q)):
            (row, col) = q.pop(0)
            grid[row][col] = rotten
            if row + 1 < rows and grid[row + 1][col] == fresh:
                grid[row + 1][col] = rotten
                q.append([row + 1, col])
            if row - 1 >= 0 and grid[row - 1][col] == fresh:
                grid[row - 1][col] = rotten
                q.append([row - 1, col])
            if col + 1 < cols and grid[row][col + 1] == fresh:
                grid[row][col + 1] = rotten
                q.append([row, col + 1])
            if col - 1 >= 0 and grid[row][col - 1] == fresh:
                grid[row][col - 1] = rotten
                q.append([row, col - 1])
        time += 1

    # check if there is fresh orange left
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == fresh:
                return -1
    return max(time - 1, 0)
