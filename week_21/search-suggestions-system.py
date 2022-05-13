# https://leetcode.com/problems/search-suggestions-system/

class Node:
    def __init__(self):
        self.children = {}
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
            
        node.word = word
        
    def suggest(self, phrase):
        node = self.root
        suggestions = []
        
        for c in phrase:
            if c not in node.children:
                return []
            node = node.children[c]
        
        def search(node):
            if node.word:
                suggestions.append(node.word)
                
            for c in sorted(node.children):
                if len(suggestions) < 3:
                    search(node.children[c])
            
        search(node)
        return suggestions

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie(products)
            
        result = []
        for i in range(len(searchWord)):
            suggestions = trie.suggest(searchWord[:i+1])
            result.append(suggestions)
            
        return result
    
