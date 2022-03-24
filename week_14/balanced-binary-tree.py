# https://leetcode.com/problems/balanced-binary-tree/

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def search(node, level):
            if not node:
                return (level, True)

            left = search(node.left, level + 1)
            right = search(node.right, level + 1)

            return (max(left[0], right[0]), abs(left[0] - right[0]) <= 1 and left[1] and right[1])

        return search(root, 0)[1]
