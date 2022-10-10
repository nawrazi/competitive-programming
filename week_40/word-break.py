# https://leetcode.com/problems/word-break/

class Node:
    def __init__(self, val):
        self.val = val
        self.word = ''
        self.children = {}

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = Node()
        
        for word in wordDict:
            node = root
            for c in word:
                if not c in node.children:
                    node.children[c] = Node(c)
                node = node.children[c]   
            node.word = word
            
        @cache
        def search(idx):
            node = root
            
            while idx < len(s):
                if s[idx] not in node.children:
                    return False
                
                node = node.children[s[idx]]
                idx += 1
                
                if node.word and search(idx):
                    return True
                
            return node.word != ''
        
        return search(0)
    
