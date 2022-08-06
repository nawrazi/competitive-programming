# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def search(node, run_sum):
            if not node:
                return run_sum

            right_sum = search(node.right, run_sum)
            node.val += right_sum
            left_sum = search(node.left, node.val)

            return left_sum

        search(root, 0)
        return root
    
