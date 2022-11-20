# https://leetcode.com/problems/maximum-width-of-binary-tree/

class Solution:
    def search(self, node, level, position, extremes):
        if node is None:
            return
        
        extremes[level][0] = min(extremes[level][0], position)
        extremes[level][1] = max(extremes[level][1], position)
        
        self.search(node.left, level + 1, (position * 2) - 1, extremes)
        self.search(node.right, level + 1, position * 2, extremes)
        
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        extremes = defaultdict(lambda: [inf, -inf])
        self.search(root, 1, 1, extremes)
        
        widest = 0
        for minimum, maximum in extremes.values():
            width = maximum - minimum + 1
            widest = max(width, widest)
            
        return widest
    
