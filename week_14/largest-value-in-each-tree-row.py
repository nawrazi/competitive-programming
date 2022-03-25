# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([(root, 0)])
        level_max = {}

        while q:
            node, level = q.popleft()

            if not node:
                continue

            if level in level_max:
                level_max[level] = max(node.val, level_max[level])
            else:
                level_max[level] = node.val

            q.append((node.left, level + 1))
            q.append((node.right, level + 1))

        return level_max.values()
    
