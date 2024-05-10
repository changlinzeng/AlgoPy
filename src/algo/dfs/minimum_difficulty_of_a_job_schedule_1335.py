import math
from typing import List


def minDifficulty(jobDifficulty: List[int], d: int) -> int:
    def _dfs(difficulty: List[int], start: int, day: int, memo: List[List[int]]) -> int:
        current_max_difficulty = 0
        min_difficulty = math.inf

        if memo[start][day] != -1:
            return memo[start][day]

        if day == 1:
            for i in range(start, len(difficulty)):
                current_max_difficulty = max(current_max_difficulty, difficulty[i])
            return current_max_difficulty

        for i in range(start, len(difficulty) - day + 1):
            current_max_difficulty = max(current_max_difficulty, difficulty[i])
            next_min = _dfs(difficulty, i + 1, day - 1, memo)
            min_difficulty = min(min_difficulty, current_max_difficulty + next_min)
        memo[start][day] = min_difficulty
        return min_difficulty

    if len(jobDifficulty) < d:
        return -1
    if len(jobDifficulty) == d:
        return sum(jobDifficulty)
    return _dfs(jobDifficulty, 0, d, [[-1 for _ in range(d + 1)] for _ in range(len(jobDifficulty))])


if __name__ == '__main__':
    print(minDifficulty([6, 5, 4, 3, 2, 1], 2))
