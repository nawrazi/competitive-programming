# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def search(node,level):
            nonlocal final
            if not node:
                return 0

            if isLeaf(node):
                return level

            leftMax = search(node.left, level+1)
            rightMax = search(node.right, level+1)
            maxLevel = max(leftMax, rightMax)

            if maxLevel > final[0]:
                if leftMax==0:
                    final = (maxLevel,node.right)
                elif rightMax==0:
                    final = (maxLevel,node.left)
                else:
                    final = (maxLevel,node)

            elif leftMax==rightMax and maxLevel>=final[0]:
                final = (maxLevel,node)

            return maxLevel


        final = (0,root)
        isLeaf = lambda node : not node.left and not node.right
        search(root,1)

        return final[1]
