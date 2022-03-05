# https://leetcode.com/problems/search-in-a-binary-search-tree/

class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        while root and root.val!=target:
            root = root.left if root.val>target else root.right
        return root
