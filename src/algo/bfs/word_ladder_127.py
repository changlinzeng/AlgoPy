from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    def _next_word(word: str, word_list: List[str]) -> List[str]:
        next_words = []
        for w in word_list:
            diff = 0
            for c1, c2 in zip(word, w):
                if c1 != c2:
                    diff += 1
                if diff > 1:
                    break
            if diff == 1:
                next_words.append(w)
        return next_words

    ladder = 1
    visited = set()
    q = [beginWord]
    while len(q) > 0:
        size = len(q)
        for _ in range(size):
            w = q.pop(0)
            if w in visited:
                continue
            visited.add(w)
            for n in _next_word(w, wordList):
                if n == endWord:
                    return ladder + 1
                q.append(n)
        ladder += 1

    return 0


if __name__ == '__main__':
    print(ladderLength('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
