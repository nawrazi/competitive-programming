# https://binarysearch.com/problems/Inorder-Successor/

class Solution:
    def solve(self, root, t):
        self.prev = -inf
        self.successor = 0
        
        def search(node):
            if not node:
                return False
            
            if search(node.left):
                return True
            if self.prev == t:
                self.successor = node.val
                return True
            self.prev = node.val
            if search(node.right):
                return True
            
        search(root)
        return self.successor
    
