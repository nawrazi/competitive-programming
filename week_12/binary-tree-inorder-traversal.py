# https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node):
            if node:
                traverse(node.left)
                output.append(node.val)
                traverse(node.right)

        output = []
        traverse(root)

        return output
