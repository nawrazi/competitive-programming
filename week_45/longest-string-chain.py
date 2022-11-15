# https://leetcode.com/problems/longest-string-chain/

class Node:
    def __init__(self):
        self.children = {}
        self.word = ''

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        trie = Node()
        
        for word in words:
            node = trie
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.word = word
            
        def search(word, idx, node, added):
            if added and idx == len(word) and node.word:
                graph[word].add(node.word)
                return
            
            for char, child in node.children.items():
                if not added and idx == len(word):
                    search(word, idx + 1, child, True)
                elif idx < len(word) and char == word[idx]:
                    search(word, idx + 1, child, added)
                if not added:
                    search(word, idx, child, True)
        
        graph = defaultdict(set)
        for word in words:
            search(word, 0, trie, False)
            
        @cache
        def longestChain(word):
            chain = 0
            for successor in graph[word]:
                chain = max(chain, longestChain(successor))
                
            return chain + 1
        
        chain = 0
        for word in sorted(words, key=len):
            chain = max(chain, longestChain(word))
            
        return chain
    
