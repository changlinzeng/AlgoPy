from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def _search(board: List[List[str]], word: str, row: int, col: int, index: int, visited: List[List[bool]]) -> bool:
        if index >= len(word):
            return True
        if board[row][col] != word[index] or visited[row][col]:
            return False

        visited[row][col] = True
        if index == len(word) - 1:
            return True

        found = False
        if row + 1 < rows:
            if _search(board, word, row + 1, col, index + 1, visited):
                found = True
        if not found and row - 1 >= 0:
            if _search(board, word, row - 1, col, index + 1, visited):
                found = True
        if not found and col + 1 < cols:
            if _search(board, word, row, col + 1, index + 1, visited):
                found = True
        if not found and col - 1 >= 0:
            if _search(board, word, row, col - 1, index + 1, visited):
                found = True
        # revert visited as the same cell may be used more than once
        if not found:
            visited[row][col] = False
        return found

    for i in range(rows):
        for j in range(cols):
            if _search(board, word, i, j, 0, [[False for _ in range(cols)] for _ in range(rows)]):
                return True
    return False


if __name__ == '__main__':
    print(exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED'))
    print(exist([['a']], 'a'))
