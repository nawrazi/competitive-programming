# https://leetcode.com/problems/top-k-frequent-words/

class Node:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.word = ''
        
class Trie:
    def __init__(self, words):
        self.root = Node()
        for word in words:
            self.addWord(word)
        
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            
        node.count += 1
        node.word = word
        
    def getWords(self):
        def get(node):
            if node.count > 0:
                heappush(words, (-node.count, node.word))
            for c in node.children:
                get(node.children[c])
            
        words = []
        get(self.root)
        return words

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trie = Trie(words)
        result = trie.getWords()
        
        return [heappop(result)[1] for _ in range(k)]
    
