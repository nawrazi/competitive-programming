# https://leetcode.com/problems/implement-trie-prefix-tree/

class Node:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.final = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            bit = ord(c) - ord('a')
            if not node.children[bit]:
                node.children[bit] = Node()
            node = node.children[bit]

        node.final = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            bit = ord(c) - ord('a')
            if node.children[bit]:
                node = node.children[bit]
            else:
                return False

        return node.final

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            bit = ord(c) - ord('a')
            if node.children[bit]:
                node = node.children[bit]
            else:
                return False

        return True
