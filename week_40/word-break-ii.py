# https://leetcode.com/problems/word-break-ii/

class Node:
    def __init__(self):
        self.word = ''
        self.children = {}

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = Node()
        
        for word in wordDict:
            node = root
            for c in word:
                if not c in node.children:
                    node.children[c] = Node()
                node = node.children[c]   
            node.word = word
            
        ans = []
        cur = []
        def search(idx):
            node = root
            
            while idx < len(s):
                if s[idx] not in node.children:
                    return
                
                node = node.children[s[idx]]
                idx += 1
                
                if node.word:
                    cur.append(node.word)
                    search(idx)
                    cur.pop()
                    
            if node.word:
                cur.append(node.word)
                ans.append(' '.join(cur))
                cur.pop()
        
        search(0)
        return ans
    
