# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def getGSum(node):
            gsum = 0
            if node.left:
                if node.left.left:
                    gsum+=node.left.left.val
                if node.left.right:
                    gsum+=node.left.right.val
            if node.right:
                if node.right.left:
                    gsum+=node.right.left.val
                if node.right.right:
                    gsum+=node.right.right.val
            return gsum

        def search(node):
            if not node: return

            if node.val%2==0:
                gsum = getGSum(node)
                nonlocal total
                total+=gsum

            search(node.left)
            search(node.right)

        total = 0
        search(root)
        return total
