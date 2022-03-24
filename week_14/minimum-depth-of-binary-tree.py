# https://leetcode.com/problems/minimum-depth-of-binary-tree/

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def search(node, depth):
            if not node:
                return depth - 1

            left = search(node.left, depth + 1)
            right = search(node.right, depth + 1)

            return min(left, right) if node.left and node.right else max(left, right)

        return search(root, 1)
