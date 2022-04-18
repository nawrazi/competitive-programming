# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def iot(node):
            if node.left:
                iot(node.left)
            count[0] += 1
            if count[0] == k:
                kth[0] = node.val
            if node.right:
                iot(node.right)
            
        kth = [None]
        count = [0]
        iot(root)
        return kth[0]
