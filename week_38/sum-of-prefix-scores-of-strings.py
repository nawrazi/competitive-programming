# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

class Node:
    def __init__(self):
        self.children = {}
        self.pres = 0

class Trie:
    def __init__(self, words):
        self.root = Node()
        self.words = words
        self.build()
        
    def build(self):
        for word in self.words:
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
                node.pres += 1
                
    def getPres(self):
        pres = []
        for word in self.words:
            cur_pres = 0
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
                cur_pres += node.pres
                
            pres.append(cur_pres)
            
        return pres
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        return Trie(words).getPres()
    
