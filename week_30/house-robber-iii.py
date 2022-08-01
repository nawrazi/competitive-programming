# https://leetcode.com/problems/house-robber-iii/

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def collect(node, safe):
            if not node:
                return 0
            
            if not safe:
                return max(
                    collect(node.left, not safe) + collect(node.right, not safe),
                    collect(node.left, safe) + collect(node.right, safe),
                    collect(node.left, not safe) + collect(node.right, safe),
                    collect(node.left, safe) + collect(node.right, not safe)
                )
            
            else:
                return node.val + collect(node.left, not safe) + collect(node.right, not safe)
            
        return max(collect(root, True), collect(root, False))
    
