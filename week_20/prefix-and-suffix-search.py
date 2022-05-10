# https://leetcode.com/problems/prefix-and-suffix-search/

class Node:
    def __init__(self):
        self.children = {}
        self.prefixes = []
        self.suffixes = set()
        

class Trie:
    def __init__(self, isPrefixTrie):
        self.root = Node()
        self.isPrefixTrie = isPrefixTrie
        
    def addWord(self, word, idx):
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
                
            node = node.children[c]
            
            if self.isPrefixTrie:
                node.prefixes.append(idx)
            else:
                node.suffixes.add(idx)
        
    def build(self, words):
        for idx, word in enumerate(words):
            if not self.isPrefixTrie:
                word = reversed(word)
                
            self.addWord(word, idx)
            
    def findIndices(self, phrase):
        if not self.isPrefixTrie:
            phrase = reversed(phrase)
            
        node = self.root
        
        for c in phrase:
            if c not in node.children:
                return [] if self.isPrefixTrie else set()
            node = node.children[c]
            
        return node.prefixes if self.isPrefixTrie else node.suffixes
    

class WordFilter:
    def __init__(self, words: List[str]):
        self.prefixTrie = Trie(True)
        self.suffixTrie = Trie(False)
        
        self.prefixTrie.build(words)
        self.suffixTrie.build(words)

    def f(self, prefix: str, suffix: str) -> int:
        starters = self.prefixTrie.findIndices(prefix)
        enders = self.suffixTrie.findIndices(suffix)
        
        for i in range(len(starters) - 1, -1, -1):
            if starters[i] in enders:
                return starters[i]
                
        return -1
