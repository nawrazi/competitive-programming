# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-2, -2)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def putFirst(self, node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        self.remove(node)
        self.putFirst(node)
        return self.map[key].val
    
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.putFirst(node)
        else:
            node = Node(key, value)
            self.map[key] = node
            self.putFirst(node)
            self.cap -= 1
            
        if self.cap < 0:
            tail = self.tail.prev
            self.remove(tail)
            self.tail.prev = tail.prev
            del self.map[tail.key]
            self.cap += 1
            
