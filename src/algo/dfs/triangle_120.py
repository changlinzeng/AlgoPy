from typing import List


def minimumTotal(triangle: List[List[int]]) -> int:
    INF = 1_000_000

    def _dfs(tri: List[List[int]], row: int, col: int, memo: List[List[int]]) -> int:
        sum = tri[row][col]
        if row == len(tri) - 1:
            return sum
        if memo[row][col] != INF:
            return memo[row][col]
        min_sum = _dfs(tri, row + 1, col, memo)
        min_sum = min(min_sum, _dfs(tri, row + 1, col + 1, memo))
        memo[row][col] = sum + min_sum
        return memo[row][col]

    size = len(triangle)
    return _dfs(triangle, 0, 0, [[INF for _ in range(size)] for _ in range(size)])


if __name__ == '__main__':
    print(minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
