# https://leetcode.com/problems/same-tree/

class Solution:
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        q = deque([(root1, root2)])

        while q:
            node1, node2 = q.popleft()

            if not node1 and not node2:
                continue

            if not node1 or not node2 or node1.val != node2.val:
                return False

            q.append((node1.left, node2.left))
            q.append((node1.right, node2.right))

        return True
