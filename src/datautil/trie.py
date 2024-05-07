from typing import List


class TrieNode:
    def __init__(self, ch: str = None):
        self.val = ch
        self.children = [None] * 26
        self.word_end = False


class Trie:
    @staticmethod
    def build(words: List[str]) -> TrieNode:
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                index = ord(c) - ord('a')
                if cur.children[index] is None:
                    cur.children[index] = TrieNode(c)
                cur = cur.children[index]
            cur.word_end = True
        return root


if __name__ == '__main__':
    root = Trie.build(['abc', 'def', 'abb'])
