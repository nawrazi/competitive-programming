# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node:
    def __init__(self):
        self.end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
         self.root = Node()
        
    def addWord(self, word: str) -> None:
        node = self.root
        
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children[letter]
            
        node.end = True
        
    def search(self, word, node = None, index = 0) -> bool:
        if not node: 
            node = self.root
        
        if index == len(word):
            return node.end
        
        if word[index] != '.' and word[index] not in node.children:
            return False
        
        if word[index] == ".":
            for c in node.children:
                if self.search(word, node.children[c], index + 1):
                    return True
            return False
        
        return self.search(word, node.children[word[index]], index + 1)
