def knightProbability(n: int, k: int, row: int, column: int) -> float:
    def _dfs(n: int, k: int, row: int, col: int, memo: dict[str, float]) -> float:
        if k == 0:
            return 1
        key = f'{k}_{row}_{col}'
        if key in memo:
            return memo[key]
        directions = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
        prob = 0
        for direct in directions:
            next_row, next_col = row + direct[0], col + direct[1]
            if 0 <= next_row < n and 0 <= next_col < n:
                prob = prob + 1 / 8 * _dfs(n, k - 1, next_row, next_col, memo)
        memo[key] = prob
        return prob
    return _dfs(n, k, row, column, {})


if __name__ == '__main__':
    print(knightProbability(3, 2, 0, 0))
