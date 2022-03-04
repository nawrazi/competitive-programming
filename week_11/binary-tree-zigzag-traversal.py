# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, 0)])
        traversals = []

        while q:
            node, level = q.popleft()

            if not node: continue

            if level >= len(traversals):
                traversals.append([node.val])
            else:
                traversals[-1].append(node.val)

            q.append((node.left, level+1))
            q.append((node.right, level+1))

        for i in range(len(traversals)):
            if i % 2 != 0:
                print(traversals[i])
                traversals[i].reverse()

        return traversals
