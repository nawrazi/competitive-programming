# https://leetcode.com/problems/recover-binary-search-tree/

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def order(node):
            if node:
                order(node.left)
                nodes.append(node)
                order(node.right)

        nodes = [TreeNode(float('-inf'))]
        order(root)
        nodes.append(TreeNode(float('inf')))

        swapped = [None, None]
        i = 1
        while i < len(nodes)-1:
            if nodes[i].val > nodes[i-1].val and nodes[i].val > nodes[i+1].val:
                if not swapped[0]:
                    swapped[0] = nodes[i]

            elif nodes[i].val < nodes[i-1].val and nodes[i].val < nodes[i+1].val:
                swapped[1] = nodes[i]

            i += 1

        swapped[0].val, swapped[1].val = swapped[1].val, swapped[0].val

        return root
