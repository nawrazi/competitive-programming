# https://leetcode.com/problems/replace-words/

class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def build(self, d):
        for word in d:
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.end = True
            
    def isCompound(self, word):
        node = self.root
        prefix = ""
        for c in word:
            if node.end:
                break
            if c in node.children:
                prefix += c
                node = node.children[c]
            elif node.children:
                return ""
            
        return prefix

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        trie.build(dictionary)
        words = sentence.split()
        
        for i, word in enumerate(words):
            prefix = trie.isCompound(word)
            if prefix:
                words[i] = prefix

        return ' '.join(words)
