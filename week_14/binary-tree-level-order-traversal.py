# https://leetcode.com/problems/binary-tree-level-order-traversal/

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final = []
        q = deque([(root, 0)])

        while q:
            node, level = q.popleft()

            if not node:
                continue

            if level < len(final):
                final[level].append(node.val)
            else:
                final.append([node.val])

            q.append((node.left, level + 1))
            q.append((node.right, level + 1))

        return final
