# https://leetcode.com/problems/extra-characters-in-a-string/

class Node:
    def __init__(self):
        self.word = ''
        self.char = 'root'
        self.children = {}

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = Node()
        
        for word in dictionary:
            node = root
            for c in word:
                if not c in node.children:
                    node.children[c] = Node()
                node = node.children[c]
                node.char = c
            node.word = word
        
        @cache
        def search(idx):
            if idx >= len(s):
                return 0
            
            node = root
            org = idx
            extra = len(s) - org
            while idx < len(s):
                if s[idx] not in node.children:
                    return min(extra, 1 + search(org + 1))
                
                node = node.children[s[idx]]
                idx += 1
                
                if node.word:
                    extra = min(extra, search(idx))
            
            return min(extra, 1 + search(org + 1))
        
        return search(0)
    
