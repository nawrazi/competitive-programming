# https://leetcode.com/problems/symmetric-tree/submissions/

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftque = deque([root.left])
        rightque = deque([root.right])

        while leftque:
            curleft = leftque.popleft()
            curright = rightque.popleft()

            if not curright and not curleft: continue
            if not curright or not curleft: return False

            if curright.val != curleft.val:
                return False

            if curleft:
                leftque.append(curleft.left)
                leftque.append(curleft.right)
            if curright:
                rightque.append(curright.right)
                rightque.append(curright.left)

        return True
