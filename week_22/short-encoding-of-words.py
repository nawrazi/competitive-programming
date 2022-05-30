# https://leetcode.com/problems/short-encoding-of-words/

class Node:
    def __init__(self):
        self.children = {}
        self.wordlen = 0
        self.last = False
        
class Trie:
    def __init__(self, words):
        self.root = Node()
        for word in words:
            self.add(word)
            
    def add(self, word):
        node = self.root
        for c in reversed(word):
            if c not in node.children:
                node.children[c] = Node()
            node.last = False
            node = node.children[c]
            
        node.wordlen = len(word)
        node.last = len(node.children) == 0

class Solution(object):
    def minimumLengthEncoding(self, words):
        trie = Trie(words)
        encoding = []
        
        def search(node):
            if node.wordlen and node.last:
                encoding.append(node.wordlen)
                
            for c in node.children:
                search(node.children[c])
                
        search(trie.root)
        
        return sum(encoding) + len(encoding)
    
