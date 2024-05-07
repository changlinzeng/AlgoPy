from typing import List, Optional, Set


class TrieNode:
    def __init__(self, val: str = None):
        self.val = val
        self.children: List[Optional[TrieNode]] = [None for _ in range(26)]
        self.word_end = False


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    rows, cols = len(board), len(board[0])

    def _add_words(root: TrieNode, words: Set[str]) -> None:
        for word in words:
            par = root
            for c in word:
                index = ord(c) - ord('a')
                if par.children[index] is None:
                    par.children[index] = TrieNode(c)
                par = par.children[index]
            par.word_end = True

    def _dfs(board: List[List[str]],
             root: TrieNode,
             row: int,
             col: int,
             word: str,
             found: List[str],
             visited: List[List[bool]]) -> None:
        if visited[row][col] or board[row][col] != root.val:
            return
        visited[row][col] = True
        word += board[row][col]
        if root.word_end:
            found.append(word)
            # remove word from trie
            root.word_end = False

        if row + 1 < rows:
            child = root.children[ord(board[row + 1][col]) - ord('a')]
            if child is not None:
                # use copy of visited as one cell can be used more than once by different words
                # so each word should have its own copy of visited
                _dfs(board, child, row + 1, col, word, found, [[v for v in r] for r in visited])
        if row - 1 >= 0:
            child = root.children[ord(board[row - 1][col]) - ord('a')]
            if child is not None:
                _dfs(board, child, row - 1, col, word, found, [[v for v in r] for r in visited])
        if col + 1 < cols:
            child = root.children[ord(board[row][col + 1]) - ord('a')]
            if child is not None:
                _dfs(board, child, row, col + 1, word, found, [[v for v in r] for r in visited])
        if col - 1 >= 0:
            child = root.children[ord(board[row][col - 1]) - ord('a')]
            if child is not None:
                _dfs(board, child, row, col - 1, word, found, [[v for v in r] for r in visited])

    word_set = set(words)
    matched = []
    for i in range(rows):
        for j in range(cols):
            root = TrieNode()
            _add_words(root, word_set)
            child = root.children[ord(board[i][j]) - ord('a')]
            if child is not None:
                found = []
                _dfs(board, child, i, j, '', found, [[False for _ in range(cols)] for _ in range(rows)])
                matched += found
                for w in found:
                    word_set.remove(w)
    return matched
