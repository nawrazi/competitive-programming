# https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def check(node, row, col):
            if not node:
                return True
            
            if last[row] != col - 1:
                return False
            
            last[row] = col
            left = check(node.left, row + 1, 2 * col - 1)
            right = check(node.right, row + 1, 2 * col)
            return left and right
        
        last = defaultdict(int)
        if not check(root, 1, 1):
            return False
        
        incomplete = False
        for row, col in sorted(last.items()):
            if col != pow(2, row - 1) and incomplete:
                return False
            incomplete = col != pow(2, row - 1)
            
        return True
    
