# https://leetcode.com/problems/camelcase-matching/

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.word = ""
        
class Trie:
    def __init__(self, words):
        self.root = Node()
        for word in words:
            self.add(word)
        
    def add(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.word = word
        
class Solution(object):
    def camelMatch(self, queries, pattern):
        trie = Trie(queries)
        result = {}
        
        isCapital = lambda c : ord('A') <= ord(c) <= ord('Z')
        
        def search(node, index, clean, seen):
            if node.word:
                result[node.word] = clean and index == len(pattern) - 1 and seen == len(pattern)
                
            for c in node.children:
                if not clean or (isCapital(c) and c != pattern[index]):
                    search(node.children[c], index, False, seen)
                    
                elif index < len(pattern) - 1 and c == pattern[index]:
                    search(node.children[c], index + 1, clean, seen + 1)
                    
                else:
                    temp = seen
                    if isCapital(c) or (index == len(pattern) - 1 and pattern[index] == c):
                        temp += 1
                    search(node.children[c], index, clean, temp)
                    
        search(trie.root, 0, True, 0)
        
        return [result[q] for q in queries]
    
