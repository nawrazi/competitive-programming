# https://leetcode.com/problems/path-sum/submissions/

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def sums(node, cur_sum):
            if not node: return False

            cur_sum += node.val
            if isLeaf(node):
                return cur_sum==targetSum

            return sums(node.left, cur_sum) or sums(node.right, cur_sum)

        isLeaf = lambda node : not node.left and not node.right

        return sums(root, 0)
