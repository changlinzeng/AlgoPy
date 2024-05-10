import math
from typing import List


def coinChange(coins: List[int], amount: int) -> int:

    def _backtrack(coins: List[int], amount: int, memo: List[int]) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if memo[amount] != 0:
            return memo[amount]
        min_count = math.inf
        for coin in coins:
            next_count = _backtrack(coins, amount - coin, memo)
            if next_count != -1:
                min_count = min(min_count, next_count + 1)
        memo[amount] = min_count if min_count != math.inf else -1
        return memo[amount]

    if amount == 0:
        return 0
    return _backtrack(coins, amount, [0] * (amount + 1))


if __name__ == '__main__':
    print(coinChange([1, 2, 5], 11))
    print(coinChange([2], 3))
    print(coinChange([186,419,83,408], 6249))
