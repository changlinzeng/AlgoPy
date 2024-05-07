from typing import List


def numIslands(grid: List[List[str]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def dfs(grid:  List[List[str]], row: int, col: int, visited: List[List[bool]]):
        if grid[row][col] != '1' or visited[row][col]:
            return
        visited[row][col] = True
        if row + 1 < rows:
            dfs(grid, row + 1, col, visited)
        if row - 1 >= 0:
            dfs(grid, row - 1, col, visited)
        if col + 1 < cols:
            dfs(grid, row, col + 1, visited)
        if col - 1 >= 0:
            dfs(grid, row, col - 1, visited)

    num = 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and not visited[i][j]:
                num += 1
                dfs(grid, i, j, visited)
    return num


if __name__ == '__main__':
    print(numIslands([['0', '1', '0'], ['1', '0', '1'], ['0', '1', '0']]))
