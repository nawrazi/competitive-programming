# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def search(node, depth):
            if not node:
                return depth - 1

            left = search(node.left, depth + 1)
            right = search(node.right, depth + 1)

            return max(left, right)

        return search(root, 1)
        
