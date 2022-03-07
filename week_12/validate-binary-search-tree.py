# https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, upper, lower):
            if not node:
                return True

            if node.val >= upper or node.val <= lower:
                return False

            validate_right = validate(node.right, upper, max(lower,node.val))
            validate_left = validate(node.left, min(upper,node.val), lower)

            return validate_right and validate_left

        return validate(root, float('inf'), float('-inf'))
