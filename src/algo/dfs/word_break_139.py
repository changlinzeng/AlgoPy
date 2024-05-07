from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:

    def _search(s: str, word_dict: List[str], start: int, memo: List[int]) -> bool:
        if start >= len(s):
            return True
        if memo[start] != 0:
            return memo[start] == 1
        for word in word_dict:
            if s.find(word, start) == start:
                if _search(s, word_dict, start + len(word), memo):
                    memo[start] = 1
                    break
                memo[start] = -1
        return memo[start] == 1

    return _search(s, wordDict, 0, [0] * len(s))


if __name__ == '__main__':
    print(wordBreak('leetcode', ['leet', 'code']))
    print(wordBreak('catsandog', ['sand', 'cat', 'cats', 'dog']))
