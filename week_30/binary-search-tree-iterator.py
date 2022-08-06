# https://leetcode.com/problems/binary-search-tree-iterator/

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.traversal = []
        self.search(root)
        self.iter = -1

    def search(self, node):
        if not node:
            return
        
        self.search(node.left)
        self.traversal.append(node.val)
        self.search(node.right)
        
        
    def next(self) -> int:
        self.iter += 1
        return self.traversal[self.iter]

    def hasNext(self) -> bool:
        return self.iter < len(self.traversal) - 1
    
