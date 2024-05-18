from typing import List


def getMaximumGold(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def _dfs(grid: List[List[int]], row: int, col: int, visited: List[List[bool]]) -> int:
        if visited[row][col]:
            return 0
        if grid[row][col] == 0:
            return 0
        gold = grid[row][col]
        max_gold = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited[row][col] = True
        for direct in directions:
            m, n = row + direct[0], col + direct[1]
            if 0 <= m < rows and 0 <= n < cols:
                max_gold = max(max_gold, _dfs(grid, m, n, visited))

        visited[row][col] = False
        return gold + max_gold

    max_g = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                max_g = max(max_g, _dfs(grid, i, j, [[False for _ in range(cols)] for _ in range(rows)]))
    return max_g


if __name__ == '__main__':
    print(getMaximumGold([[1,0,7,0,0,0],
                          [2,0,6,0,1,0],
                          [3,5,6,7,4,2],
                          [4,3,1,0,2,0],
                          [3,0,5,0,20,0]]))
