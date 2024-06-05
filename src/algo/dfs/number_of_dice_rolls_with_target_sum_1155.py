def numRollsToTarget(n: int, k: int, target: int) -> int:

    def _dfs(n: int, k: int, target: int, memo: dict[str, int]) -> int:
        key = f'{n}_{target}'
        if key in memo:
            return memo[key]
        if n == 0 and target == 0:
            return 1
        if n == 0 or target == 0:
            return 0
        for i in range(1, k + 1):
            if i <= target:
                count = _dfs(n - 1, k, target - i, memo)
                if key not in memo:
                    memo[key] = 0
                if count > 0:
                    memo[key] = (memo[key] + count) % 1_000_000_007
        return memo[key]

    return _dfs(n, k, target, {})


if __name__ == '__main__':
    print(numRollsToTarget(1, 6, 3))
    print(numRollsToTarget(2, 6, 7))
    print(numRollsToTarget(30, 30, 500))
