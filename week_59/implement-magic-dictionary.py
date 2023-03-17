# https://leetcode.com/problems/implement-magic-dictionary/description/

class Node:
    def __init__(self):
        self.children = {}
        self.final = False
        
class MagicDictionary:

    def __init__(self):
        self.root = Node()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.insert(word)

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            
        node.final = True

    def find(self, word, idx, node, changed):
        if idx >= len(word):
            return node.final and changed
        
        cur = word[idx]
        if cur in node.children and self.find(word, idx + 1, node.children[cur], changed):
            return True
        
        if changed:
            return False
        
        for nex, child in node.children.items():
            if nex != cur and self.find(word, idx + 1, child, True):
                return True
        
    def search(self, searchWord: str) -> bool:
        return self.find(searchWord, 0, self.root, False)
    
