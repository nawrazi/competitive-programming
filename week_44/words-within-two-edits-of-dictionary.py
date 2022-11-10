# https://leetcode.com/problems/words-within-two-edits-of-dictionary/

class Node:
    def __init__(self):
        self.children = {}
        
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        trie = Node()
        
        for word in dictionary:
            node = trie
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
                
        def match(node, word, idx, edits):
            if edits > 2:
                return False
            if idx >= len(word):
                return True
            
            for letter, child in node.children.items():
                if letter == word[idx] and match(child, word, idx + 1, edits):
                    return True
                if letter != word[idx] and match(child, word, idx + 1, edits + 1):
                    return True
        
        matched = []
        for word in queries:
            if match(trie, word, 0, 0):
                matched.append(word)
                
        return matched
    
