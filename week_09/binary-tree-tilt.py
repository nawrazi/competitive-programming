# https://leetcode.com/problems/binary-tree-tilt/

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def find(node):
            if not node: return 0

            left_sum = find(node.left)  if node.left else 0
            right_sum = find(node.right) if node.right else 0

            tilt = abs(right_sum - left_sum)
            nonlocal tilts
            tilts+=tilt

            return node.val + left_sum + right_sum

        tilts = 0
        find(root)
        return tilts
