# https://leetcode.com/problems/longest-word-in-dictionary/

class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def __init__(self):
        self.parent = Node()
        self.longest = []
        
    def addWord(self, word):
        node = self.parent
        cur_word = []
        for i, c in enumerate(word):
            if c not in node.children:
                if i < len(word) - 1:
                    return
                node.children[c] = Node()
            cur_word.append(c)
            node = node.children[c]
        node.end = True
        
        if len(cur_word) > len(self.longest):
            self.longest = cur_word
            
    def longestWord(self, words: List[str]) -> str:
        for word in sorted(words):
            self.addWord(word)
            
        return ''.join(self.longest)
        
