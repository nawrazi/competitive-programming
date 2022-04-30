# https://leetcode.com/problems/map-sum-pairs/

class Node:
    def __init__(self, val):
        self.children = {}
        self.val = val
        self.final = False

class MapSum:
    def __init__(self):
        self.root = Node(0)
        self.inserted = {}

    def insert(self, key: str, val: int) -> None:
        node = self.root
        val -= self.inserted.get(key, 0)
        self.inserted[key] = val + self.inserted.get(key, 0)
        for c in key:
            if c in node.children:
                node.children[c].val += val
            else:
                node.children[c] = Node(val)
            node = node.children[c]
            
        node.final = True

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
            
        return node.val
