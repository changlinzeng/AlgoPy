from typing import List


def wordBreak(s: str, wordDict: List[str]) -> List[str]:

    def _search(s: str, word_dict: List[str], sentence: str, all: List[str]) -> None:
        if s == '':
            all.append(sentence)
            return
        for word in word_dict:
            if s.startswith(word):
                next = word if sentence == '' else f'{sentence} {word}'
                _search(s[len(word):], word_dict, next, all)

    words = []
    _search(s, wordDict, '', words)
    return words


if __name__ == '__main__':
    print(wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"]))
