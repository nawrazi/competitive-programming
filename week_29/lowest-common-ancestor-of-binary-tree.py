# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class Solution:
    def __init__(self):
        self.first_found = False
        self.paths = {}
        
    def search(self, node, target):
        if not node:
            return False

        if node.val == target.val:
            if not self.first_found:
                self.paths[target.val].add(node)
            else:
                self.paths[target.val].append(node)
            return True
        
        found = self.search(node.left, target) or self.search(node.right, target)

        if found:
            if not self.first_found:
                self.paths[target.val].add(node)
            else:
                self.paths[target.val].append(node)
                
        return found
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.paths[p.val] = set()
        self.search(root, p)
        self.first_found = True
        
        self.paths[q.val] = []
        self.search(root, q)
        
        for node in self.paths[q.val]:
            if node in self.paths[p.val]:
                return node
            
