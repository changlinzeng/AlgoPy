from typing import List


class WordDictionary:

    class TrieNode:
        def __init__(self, val: str = None):
            self.val = val
            self.children: List[__class__] = [None] * 26
            self.word_end = False

    def __init__(self):
        self.root = WordDictionary.TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                node.children[index] = WordDictionary.TrieNode(c)
            node = node.children[index]
        node.word_end = True

    def search(self, word: str) -> bool:
        return self._search(word, self.root, 0)

    def _search(self, word: str, node: TrieNode, start: int) -> bool:
        for i in range(start, len(word)):
            c = word[i]
            if c == '.':
                for n in node.children:
                    if n is not None:
                        if self._search(word, n, i + 1):
                            return True
                return False
            index = ord(c) - ord('a')
            if node.children[index] is None:
                return False
            if c != '.':
                node = node.children[index]
        return node.word_end


if __name__ == '__main__':
    word_dict = WordDictionary()
    word_dict.addWord('bad')
    word_dict.addWord('dad')
    word_dict.addWord('mad')
    print(word_dict.search('pad'))
    print(word_dict.search('bad'))
    print(word_dict.search('.ad'))
    print(word_dict.search('b..'))
